#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from logging import warn
from java2python import ev
from java2python.parser import JavaLexer


def simpleComments(block, text, typ):
    ## config prefix is used for comments via addComment
    def simpleMultiFormat(rawComment):
        rawComment = rawComment.strip()[2:-2]
        for line in rawComment.split('\n'):
            line = line.strip()
            if line.startswith('*'):
                line = line[1:]
            if line.endswith('*'):
                line = line[:-1]
            yield line.strip()

    def simpleSingleFormat(rawComment):
        yield rawComment[2:].strip()

    lines = ()
    if typ == JavaLexer.COMMENT:
        lines = simpleMultiFormat(text)
    elif typ == JavaLexer.LINE_COMMENT:
        lines = simpleSingleFormat(text)
    for line in lines:
        block.addComment(line, 0)


def commentImport(block, decl, isStatic, isStar):
    """ import handler that creates formatted comments

    """
    nm = block.top.formatExpression(decl)
    if isStatic:
        if isStar:
            comment = 'from %s import *' % nm
        else:
            nms = nm.split('.')
            comment = 'from %s import %s' % ('.'.join(nms[:-1]), nms[-1])
    else:
        comment = 'import %s' % nm
    block.top.addComment(comment)


def setupToolsPackage(block, decl, comment=False):
    """ package handler that adds a call to namespace_packages

    """
    val = "namespace_packages('%s')"
    val %= block.top.formatExpression(decl)
    call = block.top.addComment if comment else block.top.addSource
    return call(val)


setupToolsPackageComment = partial(setupToolsPackage, comment=True)


def commentPackage(block, decl):
    block.top.addComment('%s' % block.top.formatExpression(decl))


def simpleDocString(block):
    # for now, just put in something not very useful
    block.lines = [
        '""" generated source for %s\n' % (block.name, ),
        '',
        '"""',
        ] + ([] if block.lines == ['pass'] else block.lines)


def getBsrSrc():
    from inspect import getsource
    from java2python.mods.includes import bsr
    return getsource(bsr)


def functionBsr(stack, left, right):
    src = getBsrSrc()
    if src not in stack.bottom:
        stack.bottom.addSource(src, 0)
    return ev(left, right, 'bsr($left, $right)')


def functionBsrAssign(stack, left, right):
    src = getBsrSrc()
    if src not in stack.bottom:
        stack.bottom.addSource(src, 0)
    return ev(left, right, '$left = bsr($left, $right)')


def getSyncDecoSrc():
    from inspect import getsource
    from java2python.mods.includes import synchronized
    return "from threading import RLock\n%s" getsource(synchronized)


def synchronizedDeco(stack):
    src = getSyncDecoSrc()
    if src not in stack.bottom:
        stack.bottom.addSource(src, 0)
    return ev(left, right, '$left = bsr($left, $right)')
