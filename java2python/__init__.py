#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import dropwhile
from operator import not_


def ev(left='', right='', format='', **kwds):
    """ Sugar for creating a formatting value dictionary.

    """
    d = dict(left=left, right=right, format=format, )
    d.update(kwds)
    return d


def import_name(name, reloaded=False):
    """ import_name(name) -> import and return a module by name in dotted form

    Copied from the Python lib docs.

    @param name module or package name in dotted form
    @return module object
    """
    mod = __import__(name)
    if reloaded:
        reload(mod)
    for comp in name.split('.')[1:]:
        mod = getattr(mod, comp)
        if reloaded:
            reload(mod)
    return mod


def import_item(name, reloaded=False):
    """ import an item from a module by dotted name

    @param name module and attribute string, i.e., foo.bar.baz
    @return value of name from module
    """
    names = name.split('.')
    modname, itemname = names[0:-1], names[-1]
    mod = import_name(str.join('.', modname), reloaded=reloaded)
    return getattr(mod, itemname)


def maybeattr(obj, name, default=None):
    """ Returns named attribute or default.

    """
    return getattr(obj, name, default)


def maybeimport(obj):
    if isinstance(obj, (basestring, )):
        return import_item(obj)
    return obj

def trimlines(lines):
    """ Removes empty lines from the end of given sequence.

    @return lines without trailing empty lines
    """
    return list(reversed(list(dropwhile(not_, reversed(lines)))))
