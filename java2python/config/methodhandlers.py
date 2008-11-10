#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.sourcetypes.block import maybeattr


def insertDocString(block):
    # for now, just put in something not very useful
    block.lines = [
        '""" generated source for %s\n' % (block.name, ),
        '',
        '"""',
        ] + block.lines


def insertModifiers(block):
    prefix = block.prefix
    prefix.append(
        '## modifiers: %s' % (str.join(', ', block.modifiers))
    )



