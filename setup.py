#!/usr/bin/env python

from __future__ import print_function

from setuptools import setup

with open('README.rst') as infile:
    LONG_DESCRIPTION = infile.read()

install_requires = ['glue-core>=0.12.2',
                    'glue-vispy-viewers>=0.9']

setup(name='glueviz',
      version='0.12.2',
      description='Multidimensional data visualization across files',
      long_description=LONG_DESCRIPTION,
      author='Glue developers',
      author_email='glueviz@gmail.com',
      url='http://glueviz.org',
      install_requires=install_requires,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Visualization',
          'License :: OSI Approved :: BSD License'
          ],
      )
