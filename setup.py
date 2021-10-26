#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='asamp',
      version='0.1',
      description='Structure disassembly tree finder',
      author='Sam Wilcock',
      author_email='el18sw@leeds.ac.uk',
      url='https://swilcock0.github.io/',
      packages=find_packages('asamp'),
      package_dir={'': '.'},
      include_package_data=True,
     )