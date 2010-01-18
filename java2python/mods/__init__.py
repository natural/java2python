#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(block):
    yield '""" generated source for %s' % block.name
    yield ''
    yield '"""'


def outputSubs(block, text):
    subsname = '{0}OutputSubs'.format(block.className.lower())
    subs = block.config.all(subsname, [])
    for sub in subs:
	for pattern, repl in sub:
	    text = re.sub(pattern, repl, text)
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

