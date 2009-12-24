#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from logging import warn
from java2python import expression, maybeAttr
from java2python.parser import JavaLexer


def simpleCommentLineFormatter(raw):
    yield raw[2:].strip()


def simpleCommentMultiLineFormatter(raw):
    raw = raw.strip()[2:-2]
    for line in raw.split('\n'):
        line = line.strip()
        if line.startswith('*'):
            line = line[1:]
        if line.endswith('*'):
            line = line[:-1]
        yield line.strip()


def simpleCommentUnknownFormatter(raw):
    return ()

simpleCommentFormatters = {
    JavaLexer.LINE_COMMENT : simpleCommentLineFormatter,
    JavaLexer.COMMENT      : simpleCommentMultiLineFormatter,
    None                   : simpleCommentUnknownFormatter,
}


def simpleComments(block, text, typ):
    """ A very simple comment writer.

    """
    formatter = simpleCommentFormatters.get(typ, simpleCommentFormatters[None])
    for line in reversed(list(formatter(text))):
        block.addComment(line)


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
    call = block.top.addComment if comment else block.top.append
    return call(val)


setupToolsPackageComment = partial(setupToolsPackage, comment=True)


def commentPackage(block, decl):
    block.top.addComment('%s' % block.top.formatExpression(decl))


def simpleDocString(block):
    # for now, just put in something not very useful
    doc = [
        '""" generated source for %s\n' % (block.name, ),
        '',
        '"""',
        ]
    for line in reversed(doc):
        block.insert(0, line)


def methodRename(block):
    renames = block.config.combined('methodRenames')
    if block.name in renames:
	block.name = renames[block.name]


def getBsrSrc():
    from inspect import getsource
    from java2python.mods.includes import bsr
    return getsource(bsr)


def functionBsr(stack, left, right):
    src = getBsrSrc()
    if src not in stack.bottom:
        stack.bottom.insert(0, src)
    return expression(left, right, 'bsr($left, $right)')


def functionBsrAssign(stack, left, right):
    src = getBsrSrc()
    if src not in stack.bottom:
        stack.bottom.insert(0, src)
    return expression(left, right, '$left = bsr($left, $right)')


def getSyncDecoSrc():
    from inspect import getsource
    from java2python.mods.includes import synchronized
    return 'from threading import RLock\n%s' % getsource(synchronized)


def synchronizedDeco(stack):
    src = getSyncDecoSrc()
    if src not in stack.bottom:
        stack.bottom.insert(0, src)
    return expression(left, right, '$left = bsr($left, $right)')


