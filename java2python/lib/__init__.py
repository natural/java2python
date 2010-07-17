#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getModule(name, reloaded=False):
    """ getModule(name) -> import and return a module by name in dotted form

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


def getModuleValue(name, reloaded=False):
    """ import an item from a module by dotted name

    @param name module and attribute string, i.e., foo.bar.baz
    @return value of name from module
    """
    names = name.split('.')
    modname, itemname = names[0:-1], names[-1]
    mod = getModule(str.join('.', modname), reloaded=reloaded)
    return getattr(mod, itemname)


class FS(object):
    l = '{left}'
    r = '{right}'
    c = ':'
    lc = l + c
    lr = l + r
    lsr = l + ' ' + r
    lsrc = lsr + c

    #instance = 'isinstance(' + l + ', (' + t + ', ))'
    @classmethod
    def op(cls, op):
	if op == '>>>':
	    return '({left} & (2**32+{left})) >> {right}'
	if op == '>>>=':
	    return '{left} = bsr({left}, {right})'
	return cls.l + ' ' + op + ' ' + cls.r
