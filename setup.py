#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""java2python:  Imperfect Translation of Java Source Code to Python

This package provides tools to (imperfectly) translate Java source
code to python source code.
"""
from distutils.core import setup


classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: OS Independent
Operating System :: POSIX
Programming Language :: Python
Programming Language :: Java
Topic :: Software Development
Topic :: Software Development :: Code Generators
"""

doclines = __doc__.split('\n')


setup(
    name = 'java2python',
    version = '0.2',
    description = doclines[0],
    author = 'Troy Melhase',
    author_email = 'troy@gci.net',
    url = 'http://code.google.com/p/java2python/',
    license = 'GNU General Public License (GPL)',
    packages = ['java2python', 'java2python/lib', ],
    scripts = ['java2python/bin/j2py', 'java2python/bin/jast_print'],
    package_data = {
        'java2python/lib':['*.g', '*.txt', ],
    },
    classifiers = filter(None, classifiers.split('\n')),
    long_description = '\n'.join(doclines[2:]),
    platforms = ['any'],
    download_url = 'http://code.google.com/p/java2python/downloads/list',
)
