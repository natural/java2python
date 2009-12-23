#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial
from itertools import count, dropwhile
from operator import not_
from string import Template


def expression(left='', right='', format='', **kwds):
    """ Sugar for creating a formatting value dictionary.

    """
    return dict(left=left, right=right, format=format, **kwds)


passExpr = partial(expression, left='pass', right='', format='$left')


def parameter(ident='', type='', modifiers='', variadic='', format='$ident', **kwds):
    if variadic:
        format = '*' + format
    return dict(
        ident=ident,
        type=type,
        modifiers=modifiers,
        variadic=variadic,
        format=format,
        param=True,
    )


clsParam = partial(parameter, ident='cls', type='object')
selfParam = partial(parameter, ident='self', type='object')


def variable(ident='', cls=False, local=False, **kwds):
    """ Sugar for creating a property dictionary representing a
        variable
    """
    return dict(ident=ident, cls=cls, local=local, **kwds)


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


def formatFloatLiteral(value):
    """ Turns a java float into a syntactically correct python float.

    """
    if value.startswith('.'):
        value = '0' + value
    if value.endswith(('f', 'd')):
        value = value[:-1]
    elif value.endswith(('l', 'L')):
        value = value[:-1] + 'L'
    return value


nameCounter = count(0).next


def findKey(mapping, key):
    """ Returns the value of the specified key from a nested dictionary

    """
    if isDict(mapping):
        try:
            return mapping[key]
        except (KeyError, ):
            for k in mapping:
                v = findKey(mapping[k], key)
                if v is not None:
                    return v


def formatParameter(p):
    return Template(p['format']).substitute(p)
