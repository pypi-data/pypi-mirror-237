from setuptools import setup, find_packages
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='excel-productive-CLI',
    version="4.3.0",
    author="Nahidul Ekon",
    author_email="nahidekon314@gmail.com",
    py_modules=['timer'],
    description='TimeTracker-CLI is a command-line interface (CLI) application designed to help users efficiently track and manage their time spent on various tasks and projects.',
    url="https://github.com/nahid25/CLI-Excel-Productive-tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyfiglet',
        'tqdm',
        'inquirer',
        'yaspin',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'excel-productive-CLI=timer:main',
        ],
    },
)