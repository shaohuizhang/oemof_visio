#! /usr/bin/env python

"""oemof_visio
"""

from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='oemofvisio',
      version='v0.0.1',
      author='oemof developing group',
      author_email='oemof@rl-institut.de',
      description='The open energy modelling framework',
      url='https://oemof.org/',
      namespace_package=['oemofvisio'],
      long_description=read('README.rst'),
      install_requires=['matplotlib'])
