from setuptools import setup, find_packages

setup(
    name='sigmoidpythonlib', 
    version='0.1.0',
    author='Rishabh Verma',
    description='Python Library to read file and load in Pandas DataFrames',  
    packages=find_packages(include=['mypythonlib']),  
    install_requires=[
        'pandas'  
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='tests', 
)
