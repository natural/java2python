#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insertModifiersAsComments(block):
    comment = block.config.last('commentPrefix', '#')
    mcomment = '%s modsifiers: %s' % (comment, str.join(', ', block.modifiers))
    block.preamble.insert(0, mcomment)


def insertReturnComment(block):
    comment = block.config.last('commentPrefix', '#')
    typ = block.formatExpression(block.type)
    block.preamble.insert(0, '%s returns: %s' % (comment, typ))
