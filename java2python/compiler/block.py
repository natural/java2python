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

from java2python.compiler import template, visitor


def makeType(name, ftn=None):
    bases = (getattr(template, name), getattr(visitor, name))
    namespace = dict(factoryTypeName=ftn if ftn else name.lower())
    return type(name, bases, namespace)


Annotation = makeType('Annotation', 'at')
Class = makeType('Class', 'klass')
Comment = makeType('Comment')
Enum = makeType('Enum')
Expression = makeType('Expression', 'expr')
Interface = makeType('Interface')
Method = makeType('Method')
MethodContent = makeType('MethodContent', 'methodContent')
Module = makeType('Module')
Statement = makeType('Statement')
