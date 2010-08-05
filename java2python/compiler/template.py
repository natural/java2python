#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.template -> Base classes for writing Python source. """
##
# This module defines templates, blocks of Python source code, that
# can be easily manipulated and written.  Each base provides string
# methods (__str__, dump, dumps) serializing instances as source code.
# The base types also provide many utility methods.
#
# The Factory class is used to to provide runtime lookup of concrete
# classes; this was necessary to accommodate splitting the behavior of
# the compiler subpackage into multiple modules.  So-called patterns
# are usually a sign of a bad design and/or language limitations, and
# this case is no exception.

from functools import partial
from itertools import chain, ifilter, imap
from StringIO import StringIO

from java2python.lang import tokens
from java2python.lib import FS
from java2python.lib.colortools import *


class Factory(object):
    """ Factory -> creates pre-configured callables for new block instances. """
    types = {}

    def __init__(self, config):
	self.config =  config

    def __getattr__(self, name):
	try:
	    return partial(self.types[name], self.config)
	except (KeyError, ):
	    raise AttributeError('Factory missing "{0}" type.'.format(name))


class FactoryTypeDetector(type):
    """ FactoryTypeDetector -> detects factory-creatable types as they are defined.

    """
    def __init__(cls, name, bases, namespace):
	try:
	    Factory.types[cls.factoryTypeName] = cls
	except (AttributeError, ):
	    pass


class Base(object):
    """ Base -> base class for formatting Python output.

    """
    __metaclass__ = FactoryTypeDetector
    isAnnotation = isClass = isComment = isEnum = isExpression = \
    isInterface = isMethod = isModule = isStatement = False

    def __init__(self, config, name=None, type=None, parent=None):
	self.bases = []
	self.children = []
	self.config = config
	self.decorators = []
	self.factory = Factory(config)
	self.modifiers = []
	self.name = name
	self.parameters = []
	self.parent = parent
	self.type = type
	self.variables = []
	if parent:
	    parent.children.append(self)

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	name = white('name:') + cyan(self.name) if self.name else ''
	parts = [green(self.typeName), name]
	if self.type:
	    parts.append(white('type:') + cyan(self.type))
	if self.modifiers:
	    parts.append(white('modifiers:') + cyan(','.join(self.modifiers)))
	return ' '.join(parts)

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	handlers = self.configHandlers('Output')
	return reduce(lambda v, func:func(self, v), handlers, self.dumps(-1))

    def adopt(self, child, index=-1):
	""" Adds child to this objecs children and sets the childs parent. """
	self.children.insert(index, child)
	child.parent = self

    def altIdent(self, name):
	""" Returns an alternate identifier for the one given. """
	for klass in self.parents(lambda v:v.isClass):
	    if name in klass.variables:
		method = self.parents(lambda v:v.isMethod).next()
		if name in [p['name'] for p in method.parameters]:
		    return name
		return ('cls' if method.isStatic else 'self') + '.' + name
	return name

    def configHandler(self, part, suffix='Handler', default=None):
	""" Returns the config handler for this type of template. """
	name = '{0}{1}{2}'.format(self.typeName, part, suffix)
	return self.config.last(name, default)

    def configHandlers(self, part, suffix='Handlers'):
	""" Returns config handlers for this type of template """
	name = '{0}{1}{2}'.format(self.typeName, part, suffix)
	return imap(self.toIter, self.config.last(name, ()))

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	indent, isNotNone = level * self.indent, lambda x:x is not None
	lineFormat = '{0}{1}\n'.format
	for line in ifilter(isNotNone, self.iterPrologue()):
	    line = lineFormat(indent, line)
	    fd.write(line if line.strip() else '\n')
	for item in ifilter(isNotNone, self.iterHead()):
	    item.dump(fd, level+1)
	for item in self.iterBody():
	    item.dump(fd, level+1)
	for line in ifilter(isNotNone, self.iterEpilogue()):
	    line = lineFormat(indent, line)
	    fd.write(line if line.strip() else '\n')

    def dumps(self, level=0):
	""" Dumps this template to a string. """
	fd = StringIO()
	self.dump(fd, level)
	return fd.getvalue()

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	indent, default = self.indent, lambda x, y:None
	fd.write('{0}{1!r}\n'.format(indent*level, self))
	for child in ifilter(None, self.children):
	    getattr(child, 'dumpRepr', default)(fd, level+1)

    @property
    def indent(self):
	""" Returns the indent string for this item. """
	return self.config.last('indentPrefix', '    ')

    @property
    def isPublic(self):
	""" True if this item is static. """
	return 'public' in self.modifiers

    @property
    def isStatic(self):
	""" True if this item is static. """
	return 'static' in self.modifiers

    @property
    def isVoid(self):
	""" True if this item is void. """
	return 'void' == self.type

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	return chain(*(h(self) for h in self.configHandlers('Prologue')))

    def iterHead(self):
	""" Yields the items in the head of this template. """
	items = chain(*(h(self) for h in self.configHandlers('Head')))
	return imap(self.toExpr, items)

    def iterBody(self):
	""" Yields the items in the body of this template. """
        return iter(self.children)

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	return chain(*(h(self) for h in self.configHandlers('Epilogue')))

    def makeParam(self, name, type, **kwds):
	""" Creates a parameter as a mapping. """
	param = dict(name=name, type=type)
	if 'default' in kwds:
	    param['default'] = kwds['default']
	return param

    def parents(self, pred=lambda v:True):
	""" Yield each parent in the family tree. """
	while self:
	    if pred(self):
		yield self
	    self = self.parent

    @property
    def className(self):
	""" Returns the name of the class of this item. """
	return self.__class__.__name__

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	return self.className.lower()

    def toExpr(self, value):
	""" Returns an expression for the given value if it is a string. """
	try:
	    return self.factory.expr(left=value+'')
	except (TypeError, ):
	    return value

    def toIter(self, value):
	""" Returns an iterator for the given value if it is a string. """
	try:
	    value + ''
	except (TypeError, ):
	    return value
	else:
	    def wrapper(*a, **b):
		yield value
	    return wrapper


class Expression(Base):
    """ Expression -> formatting for Python expressions.

    """
    isExpression = True

    def __init__(self, config, left='', right='', fs=FS.lr, parent=None, tail=''):
	super(Expression, self).__init__(config, parent=parent)
	self.left, self.right, self.fs, self.tail = left, right, fs, tail

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts, parent, showfs = [blue(self.typeName)], self.parent, True
	if isinstance(self.left, (basestring, )) and self.left:
	    parts.append(white('left:') + yellow(self.left))
	    showfs = False
	if isinstance(self.right, (basestring, )) and self.right:
	    parts.append(white('right:') + yellow(self.right))
	    showfs = False
	if showfs:
	    parts.append(white('format:') + yellow(self.fs))
	if self.tail:
	    parts.append(white('tail:') + black(self.tail))
	return ' '.join(parts)

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	return self.fs.format(left=self.left, right=self.right) + self.tail

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	line = '{0}{1}\n'.format(self.indent*level, self)
	fd.write(line if line.strip() else '\n')

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	fd.write('{0}{1!r}\n'.format(self.indent*level, self))
	for obj in (self.left, self.right):
	    dumper = getattr(obj, 'dumpRepr', lambda x, y:None)
	    dumper(fd, level+1)

    @property
    def isComment(self):
	""" True if this expression is a comment. """
	try:
	    return self.left.strip().startswith('#')
	except (AttributeError, ):
	    return False


class Comment(Expression):
    """ Comment -> formatting for Python comments.

    """
    isComment = True

    def __init__(self, config, left='', right='', fs=FS.lr, parent=None, tail=''):
	super(Comment, self).__init__(config, left, right, fs, parent, tail)
	if False:# not fs.strip().startswith('#'): # wha?
	    prefix = self.config.last('commentPrefix', '# ')
	    self.fs = prefix + self.fs

    def __repr__(self):
	""" Returns the debug string representation of this comment. """
	parts = [white(self.typeName+':'),
		 black(self.left) + black(self.right) + black(self.tail), ]
	return ' '.join(parts)



class Statement(Base):
    """ Statement -> formatting for Python statements.

    """
    isStatement = True

    def __init__(self, config, keyword, fs=FS.lr, parent=None):
	super(Statement, self).__init__(config, parent=parent)
	self.keyword = keyword
	self.expr = self.factory.expr(left=keyword, fs=fs)
	self.expr.parent = self

    def __repr__(self):
	""" Returns the debug string representation of this statement. """
	parts = [green(self.typeName), white('keyword:')+cyan(self.keyword)]
	return ' '.join(parts)

    def iterPrologue(self):
	""" Yields the keyword (and clause, if any) for this statement . """
	yield self.expr


class Module(Base):
    """ Module -> formatting for Python modules.

    """
    isModule = True

    def iterBody(self):
	""" Yields the items in the body of this template. """
	blank, prev = self.factory.expr(), None
	def pred(p, c):
	    return (p and not p.isClass) and (c.isClass and not c.isComment)
	for child in super(Module, self).iterBody():
	    if pred(prev, child):
		yield blank
	    yield child
	    prev = child


class ClassMethodSharedMixin(object):
    """ ClassMethodSharedMixin -> shared methods for Class and Method types. """

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	prologue = super(ClassMethodSharedMixin, self).iterPrologue()
	return chain(prologue, self.decorators, self.iterDecl())


class Class(ClassMethodSharedMixin, Base):
    """ Class -> formatting for Python classes.

    """
    isClass = True

    def iterBases(self):
	""" Yields the base classes for this type. """
	return iter(self.bases or ['object'])

    def iterDecl(self):
	""" Yields the declaration for this type. """
        bases = ', '.join(self.iterBases())
	bases = '({0})'.format(bases) if bases else ''
	yield 'class {0}{1}:'.format(self.name, bases)

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def sprinkleBlanks(body):
	    blank, prev = self.factory.expr(), None
	    for item in body:
		if prev:
		    if type(prev) != type(item) and not prev.isComment:
			yield blank
		    elif item.isMethod and prev.isMethod:
			yield blank
		    elif prev.isClass:
			yield blank
		yield item
		prev = item
	head = any(self.iterHead())
	body = list(super(Class, self).iterBody())
	tail = () if (body or head) else [self.factory.expr(left='pass')]
	body = () if tail else sprinkleBlanks(body)
	return chain(body, tail)


class Annotation(Class):
    """ Annotation -> formatting for annotations converted to Python classes.

    """
    isAnnotation = True

    def __init__(self, config, name=None, type=None, parent=None):
	super(Annotation, self).__init__(config, name, type, parent)


class Enum(Class):
    """ Enum -> formatting for enums converted to Python classes.

    """
    isEnum = True


class Interface(Class):
    """ Interface -> formatting for interfaces converted to Python classes.

    """
    isInterface = True


class MethodContent(Base):
    """ MethodContent -> formatting for content within Python methods. """


class Method(ClassMethodSharedMixin, Base):
    """ Method -> formatting for Python methods.

    """
    isMethod = True

    def __init__(self, config, name=None, type=None, parent=None):
	super(Method, self).__init__(config, name, type, parent)
	self.parameters.append(self.makeParam('self', 'object'))

    def iterDecl(self):
	""" Yields the declaration for this method template. """
	def formatParam(p):
	    if 'default' in p:
		return '{0}={1}'.format(p['name'], p['default'])
	    return p['name']
	params = ', '.join(formatParam(param) for param in self.parameters)
	yield 'def {0}({1}):'.format(self.name, params)

    def iterBody(self):
	""" Yields the items in the body of this method template. """
	head = any(self.iterHead())
	body = list(super(Method, self).iterBody())
	tail = () if (body or head) else [self.factory.expr(left='pass')]
	return chain(body, tail)
