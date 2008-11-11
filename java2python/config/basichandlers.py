#!/usr/bin/env python
# -*- coding: utf-8 -*-
def insertDocString(block):
    # for now, just put in something not very useful
    block.lines = [
        '""" generated source for %s\n' % (block.name, ),
        '',
        '"""',
        ] + ([] if block.lines == ['pass'] else block.lines)
