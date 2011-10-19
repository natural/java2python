#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.block -> Visitors combined with templates. """
##
# This module defines classes which combine AST walking with source
# generation.  We've put these two behaviors into separate modules,
# java2python.compiler.template for creating source code, and
# java2python.compiler.visitor for walking ANTLR trees.
#
# Each of the classes depends on the behavior of its counterpart.
# This means they're very tightly coupled and that the classes are not
# very reusable.  The module split does allow for grouping of related
# methods and does hide some of the cluttered code.

from sys import modules
from java2python.compiler import template, visitor


def newType(className, factoryTypeName):
    """ Creates a class derived from template.className and visitor.className """
    bases = (getattr(template, className), getattr(visitor, className))
    return type(className, bases, dict(factoryTypeName=factoryTypeName))


def addTypeToModule((cn, ftn)):
    """ Adds a new type to this module. """
    setattr(modules[__name__], cn, newType(cn, ftn))


map(addTypeToModule, (
    ('Annotation', 'at'),
    ('Class', 'klass'),
    ('Comment', 'comment'),
    ('Enum', 'enum'),
    ('Expression', 'expr'),
    ('Interface', 'interface'),
    ('Method', 'method'),
    ('MethodContent', 'methodContent'),
    ('Module', 'module'),
    ('Statement', 'statement'),
))
