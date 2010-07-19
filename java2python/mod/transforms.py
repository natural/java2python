#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types
from keyword import kwlist


def renameIdents():
    typs = [getattr(types, n) for n in dir(types) if not n.startswith('_')]
    names = [t.__name__ for t in typs if isinstance(t, type)]
    return ['None', 'True', 'False', ] + names + kwlist


renameIdents = renameIdents()


def keywordSafeIdent(node):
    ident = node.token.text
    if ident in renameIdents:
	node.token.text = '%s_' % ident


def constXform(v):
    def xform(node):
	node.token.text = v
    return xform


null2None = constXform('None')
false2False = constXform('False')
true2True = constXform('True')


def syntaxSafeFloatLiteral(node):
    value = node.token.text
    if value.startswith('.'):
	value = '0' + value
    if value.endswith(('f', 'd')):
	value = value[:-1]
    elif value.endswith(('l', 'L')):
	value = value[:-1] + 'L'
    node.token.text = value


