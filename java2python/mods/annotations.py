#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logging import warn
from sys import version_info


def classDecoratorsSupported():
    major, minor = version_info[0:2]
    return not (major == 2 and minor < 6)


def warnClassDecorators(block):
    """

    """
    if not classDecoratorsSupported() and block.decorators:
	warn('Class decorators not supported by this version of python. '
	     'Output may have invalid syntax.')



def filterClassDecorators(block):
    if not classDecoratorsSupported() and block.decorators:
	block.decorators = []
