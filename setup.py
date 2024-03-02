from setuptools import setup, find_packages
import os

packages = find_packages(
    exclude=("doc", "dist", "build", "fslpy.egg-info", "tests")
)

setup(
    name = "flatter",
    version = "0.0.1",
    description = "Retuns the dataframe for the dictionary",
    author = "Shashi Kumar",
    author_email = "skssunny30@gmail.com",
    long_description_content_type = "text/markdown",
    long_description= "This is a python package which converts a nested dictionary into pandas dataframe",
    packages = packages,
    install_requires = ["pandas"],
    license = "MIT",
    url = "https://github.com/walkershashi/flatter",

    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)