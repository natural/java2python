#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Various enum handlers.  See the java2python.config.default for usage.

"""
from collections import defaultdict
from itertools import count

intmap = defaultdict(lambda: count(0).next)


def noop(self, decl):
    """ enum handler that does nothing """


def minjava(self):
    vf = self.current.newMethod('values')
    vf.addModifier('static')
    vf.addSource('return [v for v in cls.__dict__.values() if isinstance(v, type)]')

    vf = self.current.newMethod('valueOf')
    vf.addModifier('static')
    vf.addParameter('string', 'key')
    vf.addComment('propegate AttributeError (not IllegalArgumentExcption)')
    vf.addSource('return getattr(cls, key)')


def pystrings(self, decl):
    """ string enums, e.g., A, B, C; becomes A, B, C = ('A', 'B', 'C')

    """
    const = decl['id']
    self.current.addSource("%s = '%s'" % (const, const))


def pyints(self, decl):
    """ range enums, e.g,. A, B, C; becomes A, B, C = (0, 1, 2)

    """
    const = decl['id']
    next = intmap[self.current.name]
    self.current.addSource('%s = %s' % (const, next()))


def subclasser(classname):
    """

    """
    def subclassAdder(self, decl):
        pass
    return subclassAdder
