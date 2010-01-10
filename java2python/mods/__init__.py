#!/usr/bin/env python
# -*- coding: utf-8 -*-


def simpleShebang(module):
    return [
	'#!/usr/bin/env python',
	'# -*- coding: utf-8 -*-',
    ]


def simpleDocString(block):
    return [
	'""" generated source for %s' % block.getName(),
	'',
	'"""'
    ]


def newLine(block):
    ## ["\n"] doesn't work and it's annoying.
    return []
