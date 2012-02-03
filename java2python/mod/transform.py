#!/usr/bin/env python
# -*- coding: utf-8 -*-
# java2python.mod.transform -> input AST transformer functions and constants.
#
# This module provides several transformation functions which are
# simple callables that modify AST nodes.  These functions are not
# responsible for selecting nodes, only changing the node content.
# This gives us AST generation decoupled from AST traversal and
# modification.
#
# See the java2python.config.default and java2python.lang.selector modules to
# understand how and when selectors are associated with these callables.

import keyword
import types


def invalidPythonNames():
    """ Creates a list of valid Java identifiers that are invalid in Python. """
    ts = [getattr(types, n) for n in dir(types) if not n.startswith('_')]
    ns = [t.__name__ for t in ts if isinstance(t, type)]
    return ['None', 'True', 'False', ] + ns + keyword.kwlist


def keywordSafeIdent(node, config, invalid=invalidPythonNames()):
    """ Validates and possibly renames a Java identifier. """
    ident = node.token.text
    if ident in invalid:
        node.token.text = '%s_' % ident


def makeConst(v):
    """ Returns a closure that indiscriminately changes node text to a value. """
    def xform(node, config):
        node.token.text = v
    return xform


# Create transformers for mapping well-known Java idents into their
# Python counterparts:
null2None = makeConst('None')
false2False = makeConst('False')
true2True = makeConst('True')


def syntaxSafeFloatLiteral(node, config):
    """ Ensures a Java float literal is a valid Python float literal. """
    value = node.token.text
    if value.startswith('.'):
        value = '0' + value
    if value.endswith(('f', 'd')):
        value = value[:-1]
    elif value.endswith(('l', 'L')):
        value = value[:-1] + 'L'
    node.token.text = value


def typeSub(node, config):
    """ Maps specific, well-known Java types to their Python counterparts.

    See the `java2python.config.default` module for the default type
    mapping and further discussion.
    """
    ident = node.token.text
    subs = config.last('typeSubs')
    if ident in subs:
        node.token.text = subs[ident]
