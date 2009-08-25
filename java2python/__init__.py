#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import dropwhile
from operator import not_


def expression(left='', right='', format='', **kwds):
    """ Sugar for creating a formatting value dictionary.

    """
    return dict(left=left, right=right, format=format, **kwds)


def parameter(ident='', typ='', modifiers='', variadic='', format='$id', **kwds):
    return dict(
        id=ident,
        type=typ,
        modifiers=modifiers,
        variadic=variadic,
        format='$id',
    )


def importModule(name, reloaded=False):
    """ importModule(name) -> import and return a module by name in dotted form

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


def importValue(name, reloaded=False):
    """ import an item from a module by dotted name

    @param name module and attribute string, i.e., foo.bar.baz
    @return value of name from module
    """
    names = name.split('.')
    modname, itemname = names[0:-1], names[-1]
    mod = importModule(str.join('.', modname), reloaded=reloaded)
    return getattr(mod, itemname)


def isDeco(s):
    return s.startswith('@') if isinstance(s, basestring) else False


def isDict(v):
    return isinstance(v, (dict, ))


def maybeAttr(obj, name, default=None):
    """ Returns named attribute or default.

    """
    return getattr(obj, name, default)


def maybeImport(obj):
    if isinstance(obj, (basestring, )):
        return importValue(obj)
    return obj


def trimStrings(strings):
    """ Removes empty strings from the end of given sequence.

    @return list of strings without trailing empty strings
    """
    return list(reversed(list(dropwhile(not_, reversed(strings)))))




