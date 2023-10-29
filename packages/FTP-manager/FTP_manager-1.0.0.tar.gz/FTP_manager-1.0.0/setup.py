from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='FTP_manager',  
    version='1.0.0', 
    packages=find_packages(),  
    author='Mo Gutale',  
    author_email='mgutale@me.com', 
    description='A Python package for FTP file management.', 
    long_description=long_description, 
    long_description_content_type="text/markdown", 
    url='https://github.com/mgutale/FTP_manager',
    classifiers=[ 
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pandas',
    ],
)
