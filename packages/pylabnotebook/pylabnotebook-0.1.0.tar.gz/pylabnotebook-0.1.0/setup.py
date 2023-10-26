from setuptools import setup, find_packages
from labnotebook import __version__

setup(
    name='pylabnotebook',
    version=__version__,
    description="This package provides functions to write an automated labnotebook using git.",

    author="Matteo Miotto",
    author_email="miotsdata@gmail.com",
    
    packages=find_packages(),
    package_data={'labnotebook': ['templates/*']},
    entry_points={
        'console_scripts': [
            'labnotebook = labnotebook.main:main',
        ],
    },
    install_requires=[
        "argparse",
    ],
)
