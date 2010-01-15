#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(block):
    yield '""" generated source for %s' % block.getName()
    yield ''
    yield '"""'


def outputSubs(block, text):
    subsname = '{0}OutputSubs'.format(block.__class__.__name__.lower())
    subs = block.config.all(subsname, [])
    for sub in subs:
	for pattern, repl in sub:
	    text = re.sub(pattern, repl, text)
    return text


mainStanzaTemplate = """
if __name__ == '__main__':
{indent}import sys
{indent}{name}.main(sys.argv)
"""


def scriptMainStanza(module, text):
    name = module.getName()
    indent = module.getIndent()

    def filterClass(x):
	return x.isClass and x.getName()==name

    def filterMethod(x):
	return x.isMethod and x.isPublic and x.isStatic and \
	       x.isVoid and x.getName()=='main'

    for cls in [c for c in module.getChildren() if filterClass(c)]:
	if [m for m in cls.getChildren() if filterMethod(m)]:
	    return text + mainStanzaTemplate.format(indent=indent, name=name)

    return text


def defaultClassBase(block):
    bases = block.getType() or ['object']
    return iter(bases)


def noClassBase(block):
    yield None
