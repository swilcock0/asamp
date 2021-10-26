#!/usr/bin/env python

from setuptools import setup, find_packages
import asamp

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='asamp',
      version=asamp.__version__,
      description='Assembly Sequence and Motion Planning package',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Sam Wilcock',
      author_email='el18sw@leeds.ac.uk',
      url='https://swilcock0.github.io/',
      packages=["asamp"],
      include_package_data=True,
     )