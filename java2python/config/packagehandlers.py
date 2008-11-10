#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Some package declaration handlers.  See java2python.config.default for use.

"""
from functools import partial


def ns_pkgs(self, decl, comment):
    """ package handler that adds a call to namespace_packages

    """
    val = "namespace_packages('%s')"
    val %= self.top.formatExpression(decl)
    call = self.top.addComment if comment else self.top.addSource
    return call(val)


pysetuptools = partial(ns_pkgs, comment=False)
pysetuptools_comments = partial(ns_pkgs, comment=True)


def pycomments(self, decl):
    self.top.addComment('%s' % self.top.formatExpression(decl))
