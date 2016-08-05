#!/usr/bin/env python

from __future__ import with_statement

import sys

from setuptools import setup, find_packages

from fabric_encrypt.version import get_version


with open('README.rst') as f:
    readme = f.read()

long_description = readme

install_requires=['fabric==1.11.1']


setup(
    name='Fabric-encrypt',
    version=get_version('short'),
    description='Fabric-encrypt - securely store your production secrets.',
    long_description=long_description,
    author='Jervis Whitley',
    author_email='jervisw@whit.com.au',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Clustering',
          'Topic :: System :: Software Distribution',
          'Topic :: System :: Systems Administration',
    ],
)
