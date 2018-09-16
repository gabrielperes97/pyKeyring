# coding=utf-8
from setuptools import setup, find_packages
import os

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()

if os.name == "nt":
    scripts = None
    entry_points = {
        'console_scripts': [
            'keyring.py=keyring:_main'
        ],
    }
else:
    scripts = ['keyring.py']
entry_points = None

setup(
    name='pyKeyring',
    py_modules=['keyring', 'security', 'storage', 'utils'],
    version="0.1",
    description='A simple and secure tool to store passwords',
    long_description=read('README.md'),
    url='https://github.com/gabrielperes97/pyKeyring',
    author='Gabriel Leopoldino',
    author_email='gabrielperes97@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities'
    ],
    tests_require=[],
    install_requires=[
        'tinydb',
        'cryptography'
    ],
    scripts=scripts,
    entry_points=entry_points,
)