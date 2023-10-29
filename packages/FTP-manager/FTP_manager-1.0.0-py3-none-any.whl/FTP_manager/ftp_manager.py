from ftplib import FTP
from io import BytesIO
import pandas as pd

def handle_ftp_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e.__class__.__name__}: {e}")
            return None  # or raise a custom exception if needed
    return wrapper

class FTPManager:
    def __init__(self, host, username, password):  
        self.host = host
        self.username = username
        self.password = password
        self.ftp = FTP(host)
        self.ftp.login(user=username, passwd=password)
        self.ftp.set_pasv(True)  # Enable passive mode
        
    @handle_ftp_error
    def list_top_level_folders(self):
        try:
            folders = self.ftp.nlst()
            top_level_folders = [folder for folder in folders if self._is_directory(folder, self.ftp)]
            return top_level_folders
        except Exception as e:
            print(f"An error occurred: {e.__class__.__name__}: {e}")
            return []

    @staticmethod
    def _is_directory(item, ftp_conn):
        try:
            current_directory = ftp_conn.pwd()
            ftp_conn.cwd(item)
            ftp_conn.cwd(current_directory)  # Restore the current directory
            return True
        except Exception:
            return False

    @handle_ftp_error
    def list_files(self, folder_path):
        self.ftp.cwd(folder_path)
        files = self.ftp.nlst()
        return files

    @handle_ftp_error
    def list_folders(self, folder_path=""):
        self.ftp.cwd(folder_path)
        items = self.ftp.nlst()
        subdirectories = [item for item in items if self._is_directory(item)]
        return subdirectories

    @handle_ftp_error
    def create_folder(self, folder_name):
        self.ftp.mkd(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
        return True

    @handle_ftp_error
    def upload_file(self, df, remote_folder, file_name):
        try:
            with self.ftp as ftp_conn:
                ftp_conn.cwd(remote_folder)
                buffer = BytesIO()
                df.to_csv(buffer, index=False)
                buffer.seek(0)
                ftp_conn.storbinary(f"STOR {file_name}.csv", buffer)
                print(f"File '{file_name}.csv' uploaded successfully to '{remote_folder}' on the FTP server.")
                return True
        except Exception as e:
            print(f"An error occurred: {e.__class__.__name__}: {e}")
            return False
        
    @handle_ftp_error
    def download_file(self, remote_folder_path, remote_file_name):
        try:
            print(f"Downloading file from: {remote_folder_path}/{remote_file_name}")
            self.ftp.cwd(remote_folder_path)
            buffer = BytesIO()
            self.ftp.retrbinary(f"RETR {remote_file_name}", buffer.write)
            buffer.seek(0)
            df = pd.read_csv(buffer)
            print(f"Download successful. DataFrame shape: {df.shape}")
            return df
        except Exception as e:
            print(f"An error occurred: {e.__class__.__name__}: {e}")
            return None
