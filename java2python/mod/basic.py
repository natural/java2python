#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count
from logging import info, warn
from os import path
from re import sub as rxsub


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(obj):
    yield '""" generated source for {0} {1}'.format(obj.typeName, obj.name)
    yield ''
    yield '"""'


def commentedImports(module, expr):
    module.factory.comment(parent=module, left=expr, fs='import: {left}')


def simpleImports(module, expr):
    module.factory.expr(parent=module, left=expr, fs='import {left}')


def commentedPackages(module, expr):
    module.factory.comment(parent=module, left=expr, fs='package: {left}')


def namespacePackages(module, expr):
    source = module.sourceFilename
    if not source:
	warn('namespace package not created; source input not named.')
	return
    initname = path.join(path.dirname(source), '__init__.py')
    if path.exists(initname):
	warn('namespace package not created; __init__.py exists.')
	return
    with open(initname, 'w') as initfile:
	initfile.write('from pkgutil import extend_path\n')
	initfile.write('__path__ = extend_path(__path__, __name__)\n')
	# wrong
	initfile.write('\nfrom {0} import {0}\n'.format(module.name))
    info('created __init__.py file for package %s.', expr)


def enumConstInts(enum, index, name):
    return str(index)


def enumConstStrings(enum, index, name):
    return repr(name)


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


def overloadedClassMethods(method):
    """
    NB: this implementation does not handle overloaded static (or
    class) methods, only instance methods.
    """
    cls = method.parent
    methods = [o for o in cls.children if o.isMethod and o.name==method.name]
    if len(methods) == 1:
        return
    for i, m in enumerate(methods[1:]):
        args = [p['type'] for p in m.parameters]
	args = ', '.join(args)
        m.decorators.append('@{0}.register({1})'.format(method.name, args))
        m.name = '{0}_{1}'.format(method.name, i)
    # for this one only:
    yield '@overloaded'


def maybeClassMethod(method):
    if method.isStatic and 'classmethod' not in method.decorators:
	yield '@classmethod'

def maybeAbstractMethod(method):
    if method.parent and method.parent.isInterface:
	yield '@abstractmethod'


def globalNameCounter(original, counter=count()):
    return '__{0}_{1}'.format(original, counter.next())


def getBsrSrc():
    from inspect import getsource
    from java2python.mod.includes import bsr
    return getsource(bsr)


def maybeBsr(module):
    if getattr(module, 'needsBsrFunc', False):
	for line in getBsrSrc().split('\n'):
	    yield line


def classContentSort(obj):
    obj.children.sort(lambda x, y:-1 if x.isClass else 1)


def zopeInterfaceMethodMutator(obj):
    for method in [c for c in obj.children if c.isMethod]:
	if method.parameters and method.parameters[0]['name'] == 'self':
	    method.parameters.pop(0)

