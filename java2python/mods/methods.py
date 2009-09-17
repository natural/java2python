#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import isDeco


def insertModifiersAsComments(block):
    comment = block.config.last('commentPrefix', '#')
    mods = [m for m in block.modifiers if not isDeco(m)]
    if mods:
        mods = [block.formatExpression(m) for m in mods]
        block.preamble.insert(0, '%s mods: %s' % (comment, str.join(', ', mods)))


def insertReturnComment(block):
    comment = block.config.last('commentPrefix', '#')
    typ = block.formatExpression(block.type)
    block.preamble.insert(0, '%s returns: %s' % (comment, typ))
