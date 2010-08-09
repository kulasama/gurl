#-*- coding:utf-8 -*-
#
# Copyright (C) 2008 - Olivier Lauzanne <olauzanne@gmail.com>
#
# Distributed under the BSD license, see LICENSE.txt

from setuptools import setup, find_packages
import sys, os


version = '0.1'

setup(name='gurl',
      version=version,
      description='mock gurl',
      author='kula',
      author_email='kulasama@gmail.com',
      license='BSD',
      packages = ['gurl',], 
      include_package_data=True,  
      )
