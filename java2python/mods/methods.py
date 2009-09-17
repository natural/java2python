#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import Template


def insertModifiersAsComments(block):
    comment = block.config.last('commentPrefix', '#')
    mods = [m for m in block.modifiers if not m.get('annotation')]
    mods = [Template(m['format']).substitute(m) for m in mods]
    mcomment = '%s modifiers: %s' % (comment, str.join(', ', mods))
    block.preamble.insert(0, mcomment)


def insertReturnTypeComment(block):
    comment = block.config.last('commentPrefix', '#')
    typ = block.formatExpression(block.type)
    block.preamble.insert(0, '%s returns: %s' % (comment, typ))
