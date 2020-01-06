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

import re
from logging import warn

import keyword
import types

from java2python.lang import tokens


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


def syntaxSafeDecimalLiteral(node, config):
    """ Ensures a Java decimal literal is a valid Python decimal literal. """
    value = node.token.text
    if value.endswith(('l', 'L')):
        value = value[:-1]
    node.token.text = value


def syntaxSafeFloatLiteral(node, config):
    """ Ensures a Java float literal is a valid Python float literal. """
    value = node.token.text
    if value.startswith('.'):
        value = '0' + value
    if value.lower().endswith(('f', 'd')):
        value = value[:-1]
    node.token.text = value


def lengthToLen(node, config):
    """ Transforms expressions like 'value.length()' to 'len(value)'.

    This method changes AST branches like this:

        METHOD_CALL [start=45, stop=49]
            DOT . [line=4, start=45, stop=47]
                IDENT foo [line=4, start=45]
                IDENT length [line=4, start=47]
            ARGUMENT_LIST [line=4, start=48, stop=49]

    Into branches like this:

        IDENT len(foo) [line=4, start=45]

    Notice that the resulting IDENT node text is invalid.  We can't use a
    METHOD_CALL token because those are always bound to a class or instance.
    It would be best to add a new token type, and that option will be explored
    if we run into this problem again.

    """
    dot = node.parent
    method = dot.parent

    ident = dot.firstChildOfType(tokens.IDENT)
    ident.token.text = 'len({})'.format(ident.text)

    expr = method.parent
    expr.children.remove(method)
    expr.addChild(ident)


def formatSyntaxTransf(match):
    """ Helper function for formatString AST transform.

        Translates the Java Formatter syntax into Python .format syntax.

        This function gets called by re.sub which matches all the %...$... groups
        inside a format specifier string.
    """
    groups = match.groupdict()
    if groups['convers'] == 'n':
        # Means platform-specific line separator
        return '\\n' # Py converts \n to os.linesep

    result = '{'
    thous_sep = ''

    if(groups['idx']):
        idx = int(groups['idx'][:-1])
        result += str(idx - 1) # Py starts count from 0
    result += ':'

    if(groups['flags']):
        if ',' in groups['flags']:
            thous_sep = ','
        if '+' in groups['flags']:
            result += '+'
        elif ' ' in groups['flags']:
            result += ' '
        if '#' in groups['flags']:
            result += '#'
        if '0' in groups['flags']:
            result += '0'

    if(groups['width']):
        result += groups['width']
    result += thous_sep

    if(groups['precision']):
        result += groups['precision']

    result += groups['convers'] + '}'

    return result

def formatString(node, config):
    """ Transforms string formatting like 'String.format("%d %2$s", i, s)'
        into '"{:d} {2:s}".format(i, s)'.
    """
    dot = node.parent
    method = dot.parent
    arg_list = method.firstChildOfType(tokens.ARGUMENT_LIST)
    call_args = [arg for arg in arg_list.childrenOfType(tokens.EXPR)]
    args = [arg.firstChildOfType(tokens.IDENT) for arg in call_args[1:]]

    # Translate format syntax (if format == string_literal)
    format = call_args[0].firstChildOfType(tokens.STRING_LITERAL)
    if format:
        format.token.text =  \
            re.sub(r'%(?P<idx>\d+\$)?(?P<flags>[-+# 0,]+)?(?P<width>[0-9]+)?(?P<precision>\.[0-9]+)?(?P<convers>[scdoxefgn])',
                    formatSyntaxTransf,
                    format.token.text,
                    flags=re.IGNORECASE)
    else:
        # Translation should happen at runtime
        format = call_args[0].firstChild()
        if format.type == tokens.IDENT:
            # String variable
            warn('Formatting string %s is not automatically translated.'
                % str(format.token.text))
        else:
            # Function that returns String
            warn('Formatting string returned by %s() is not automatically translated.'
                % str(format.firstChildOfType(tokens.IDENT).token.text))

    left_ident = dot.children[0]
    right_ident = dot.children[1]

    # Change AST
    arg_list.children.remove(format.parent)
    dot.children.remove(left_ident)
    dot.children.remove(right_ident)
    dot.addChild(format)
    dot.addChild(right_ident)


def typeSub(node, config):
    """ Maps specific, well-known Java types to their Python counterparts.

    See the `java2python.config.default` module for the default type
    mapping and further discussion.
    """
    ident = node.token.text
    for subs in reversed(config.every('typeSubs', {})):
        if ident in subs:
            node.token.text = subs[ident]
            return
