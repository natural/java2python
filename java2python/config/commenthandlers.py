#!/usr/bin/env python
# -*- coding: utf-8 -*-

## needs to lookup config for prefix
from java2python.parser import JavaLexer


def simple(block, text, typ):
    lines = ()
    if typ == JavaLexer.COMMENT:
        lines = formatMultiLineComment(text)
    elif typ == JavaLexer.LINE_COMMENT:
        lines = formatLineComment(text)
    for line in lines:
        block.addComment(line, end=False)


def formatMultiLineComment(rawComment):
    rawComment = rawComment.strip()[2:-2]
    for line in rawComment.split('\n'):
        line = line.strip()
        if line.startswith('*'):
            line = line[1:]
        if line.endswith('*'):
            line = line[:-1]
        yield line.strip()


def formatLineComment(rawComment):
    yield rawComment[2:].strip()
