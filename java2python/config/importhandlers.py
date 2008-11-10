#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Various import statement handlers.  See java2python.config.default for use.

"""
def pycomments(block, decl, isStatic, isStar):
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
