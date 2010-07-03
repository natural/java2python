#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import sub as rxsub


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(obj):
    yield '""" generated source for %s' % obj.name
    yield ''
    yield '"""'


def configImports(module):
    if 0:
	yield ''


def commentedImports(module):
    if 0:
	yield ''


def commentedPackageName(module):
    if 0:
	yield ''


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


def outputSubs(obj, text):
    subsname = '{0}OutputSubs'.format(obj.typeName)
    subs = obj.config.every(subsname, [])
    for sub in subs:
	for pattern, repl in sub:
	    text = rxsub(pattern, repl, text)
    return text


def mapClassType(obj):
    bases = obj.bases or ('object', )
    for name in bases:
	yield name


