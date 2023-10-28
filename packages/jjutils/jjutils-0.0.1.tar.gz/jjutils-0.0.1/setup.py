"""
This is the way to create a python package.

Run in the repo: pip3 install --editable ./ 

"""

from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()


setup(
    name="jjutils",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements,
    description="A collection of utilities",
    author="JJ Espinoza",
    author_email="jj.espinoza.la@gmail.com",
)
