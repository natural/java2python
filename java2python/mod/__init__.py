#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import sub as rxsub


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(obj):
    yield '""" generated source for {0} {1}'.format(obj.typeName, obj.name)
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


def mapClassType(obj):
    bases = obj.bases or ('object', )
    for name in bases:
	yield name


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
        m.decorators.append('{0}.register({1})'.format(method.name, args))
        m.name = '{0}_{1}'.format(method.name, i)
    # for this one only:
    yield 'overloaded'


def maybeClassMethod(method):
    if method.isStatic and 'classmethod' not in method.decorators:
	yield 'classmethod'


def simpleInterfaces(method):
    mkExpr = partial(Expression, module.config,
		     format='raise NotImplementedError({left})')
    for iface in module.interfaces:
	for method in iface.methods:
	    expr = mkExpr(left='"Method \'%s\' is abstract"' % method.name)
	    method.children.insert(0, expr)
