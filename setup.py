# coding=utf-8
from setuptools import setup, find_packages
import os

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()

setup(
    name='pyKeyring',
    version='0.1',
    description='A simple and secure tool to store passwords',
    author='Gabriel Leopoldino',
    author_email='gabrielperes97@gmail.com',
    url='https://github.com/gabrielperes97/pyKeyring',
    install_requires=['tinydb', 'cryptography'],
    license = "MIT",
    long_description=read('README.md'),
    project_urls={
        'Issues': 'https://github.com/gabrielperes97/pyKeyring/issues',
    },
    packages = find_packages(exclude=['test']),
)