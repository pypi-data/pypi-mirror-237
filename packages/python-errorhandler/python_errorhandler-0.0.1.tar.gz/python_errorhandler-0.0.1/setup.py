from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'This package is used for error handling you dont have to right try catch every time.just import the package and add as decorator with your function.'
LONG_DESCRIPTION = 'To import this you have to just do this ->> from python_errorhandler import error_handler'

setup(
        name="python_errorhandler", 
        version=VERSION,
        author="Nimesh Prajapati",
        author_email="prajapatin953@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['python_errorhandler'],
        install_requires=[
        "Django",  
        "djangorestframework",
    ],
)