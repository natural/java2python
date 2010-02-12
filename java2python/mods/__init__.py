#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import sub as rxsub
from java2python.blocks import Expression
from functools import partial


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(block):
    yield '""" generated source for %s' % block.name
    yield ''
    yield '"""'


def simpleModuleImports(block):
    for value, static, star in block.imports:
	yield value


def outputSubs(block, text):
    subsname = '{0}OutputSubs'.format(block.className.lower())
    subs = block.config.all(subsname, [])
    for sub in subs:
	for pattern, repl in sub:
	    text = rxsub(pattern, repl, text)
    return text


scriptTemplate = """\n
if __name__ == '__main__':
{indent}import sys
{indent}{name}.main(sys.argv)"""


def scriptMainStanza(module):
    def filterClass(x):
	return x.isClass and x.name==module.name

    def filterMethod(x):
	return x.isMethod and x.isPublic and x.isStatic and \
	       x.isVoid and x.name=='main'

    for cls in [c for c in module.children if filterClass(c)]:
	if [m for m in cls.children if filterMethod(m)]:
	    yield scriptTemplate.format(indent=module.indent, name=module.name)
	    break


def defaultClassBase(block):
    return iter(block.type or ['object'])


def noClassBase(block):
    yield None


def enumConstantSelector(block):
    selection = enumConstantStrings
    ctors = [c for c in block.children if c.isMethod]
    if ctors:
	selection = enumConstantInstances
    for value in selection(block):
	yield value


def enumConstantInstances(block):
    yield None

def enumConstantStrings(block):
    for c in block.enumConstants:
	yield "{0}.{1} = '{1}'".format(block.name, c, )
    yield ''


def enumConstantInts(block):
    for i, c in enumerate(block.enumConstants):
	yield "{0}.{1} = {2}".format(block.name, c, i, )
    yield ''



def simpleInterfaces(module):
    mkExpr = partial(Expression, module.config,
		     format='raise NotImplementedError({left})')
    for iface in module.interfaces:
	for method in iface.methods:
	    expr = mkExpr(left='"Method \'%s\' is abstract"' % method.name)
	    method.children.insert(0, expr)

def abcInterfaces(module):
    abcImport = 'from abc import ABCMeta, abstractmethod'
    ifaces = list(module.interfaces)
    if ifaces:
	module.addImport(abcImport)
	mkExpr = partial(Expression, module.config, format='{left}')
	for iface in ifaces:
	    iface.children.insert(0, mkExpr(left='__metaclass__ = ABCMeta'))
	    for method in iface.methods:
		method.addDecorator('abstractmethod')


def zopeInterfaces(module):
    ziImport = 'from zope.interface import Interface, implements'
    ifaces = list(module.interfaces)
    if ifaces:
	module.addImport(ziImport)
	for iface in ifaces:
	    iface.type = 'Interface'
	    for method in iface.methods:
		method.requiresFirstParam = False

	inames = [iface.name for iface in ifaces]
	mkExpr = partial(Expression, module.config, format='{left}')

	for cls in module.classes:
	    ctypes = list(cls.type)
	    imps = []
	    for base in ctypes:
		if base in inames:
		    imps.append(base)
		    cls.delType(base)
	    if imps:
		imp = ', '.join(imps)
		cls.children.insert(0, mkExpr(left='implements({0})'.format(imp)))
