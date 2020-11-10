# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pydobiss',
    version='0.1.0',
    description='python interface to the dobiss developer api',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Kester Aernoudt',
    author_email='kesteraernoudt@yahoo.com',
    url='https://github.com/kesteraernoudt/pydobiss',
    license=license,
    packages=find_packages()
)

