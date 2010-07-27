#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.template -> Base classes for writing Python source. """
##
# This module defines base template types.  Each base class provides
# string representation methods (__str__, __repr__, dump, dumps) for
# serializing instances as source code.  The base types also provide
# many utility methods.
#
# The Factory class is used by the BaseTemplate class to provide
# runtime lookup of concrete classes; this was necessary to
# accommodate splitting the behavior of the blocks package into
# multiple modules.  So-called patterns are usually a sign of a bad
# design and/or language limitations, and this case is no exception.
#
from functools import partial
from itertools import chain, ifilter
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
    isClass = isComment = isExpression = isMethod = isModule = False

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
	if self.isMethod:
	    self.parameters.append(self.makeParam('self', 'object'))

    def insertChild(self, child, index=-1):
	self.children.insert(index, child)
	child.parent = self

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
	for handler in self.config.last(name, ()):
	    if isinstance(handler, (basestring, )):
		def wrapper(*args, **kwds):
		    yield handler
		yield wrapper
	    else:
		yield handler

    def configTransformers(self, visitor):
	name = visitor.factoryTypeName
	name = '{0}Transformers'.format(name[0].lower() + name[1:])
	return name, self.config.handlers(name, ())

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	indent, isNotNone = level * self.indent, lambda x:x is not None
	for line in ifilter(isNotNone, self.iterPrologue()):
	    line = '{0}{1}\n'.format(indent, line)
	    fd.write(line if line.strip() else '\n')
	for item in self.iterBody():
	    item.dump(fd, level+1)
	for line in ifilter(isNotNone, self.iterEpilogue()):
	    line = '{0}{1}\n'.format(indent, line)
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
	yield None

    def iterBody(self):
	""" Yields the items in the body of this template. """
        return iter(self.children)

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	yield None

    def makeParam(self, name, type):
	""" Creates a parameter as a mapping. """
	return dict(name=name, type=type)

    def parents(self, pred=lambda v:True):
	""" Yield each parent in the family tree. """
	while self:
	    if pred(self):
		yield self
	    self = self.parent

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	return self.__class__.__name__.lower()


class BaseExpression(Base):
    """ BaseExpression -> base class for formatting Python expressions.

    """
    isExpression = True

    def __init__(self, config, left='', right='', fs=FS.lr, parent=None, tail=''):
	super(BaseExpression, self).__init__(config, parent=parent)
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
	    parts.append(white('tail:') + yellow(self.tail))
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
	    return self.left.startswith('#')
	except (AttributeError, ):
	    return False


class BaseComment(BaseExpression):
    """ BaseComment -> base class for formatting Python comments. """

    def __repr__(self):
	""" Returns the debug string representation of this comment. """
	parts = [white(self.typeName+':'),
		 black(self.left) + black(self.right) + black(self.tail), ]
	return ' '.join(parts)



class BaseStatement(Base):
    """ BaseStatement -> base class for formatting Python statements. """

    def __init__(self, config, keyword, fs=FS.lr, parent=None):
	super(BaseStatement, self).__init__(config, parent=parent)
	self.keyword = keyword
	self.expr = self.factory.expr(left=keyword, fs=fs)
	self.expr.parent = self

    def __repr__(self):
	""" Returns the debug string representation of this statement. """
	parts = [green(self.typeName), white('keyword:')+cyan(self.keyword)]
	return ' '.join(parts)


class Module(Base):
    """ Module -> formatting for Python modules. """
    isModule = True

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	return chain(*(h(self) for h in self.configHandlers('Prologue')))

    def iterBody(self):
	""" Yields the items in the body of this template. """
	get = lambda o, n:getattr(o, n, None)
	children, prev = self.children, None
	blank = self.factory.expr(left='\n')
	def pred(c, p):
	    return p and get(c, 'isClass') and not get(c, 'isComment') \
		   and not get(p, 'isClass')
	for child in children:
	    if pred(child, prev):
		yield blank
	    yield child
	    prev = child

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	return chain(*(h(self) for h in self.configHandlers('Epilogue')))


##
# class and class-like types


class Class(Base):
    """ Class -> formatting for Python classes. """
    isClass = True

    def iterDecorators(self):
	""" Yields decorators for this method. """
	def iterLines():
	    return chain(*(h(self) for h in self.configHandlers('Prologue')))
	def iterOtherDecos():
	    return chain(*(h(self) for h in self.configHandlers('ExtraDecorator')))
	return chain(self.decorators, iterOtherDecos(), iterLines())

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	def iterBases():
	    return chain(*(h(self) for h in self.configHandlers('Base')))
        bases = ', '.join(ifilter(None, iterBases()))
	bases = '({0})'.format(bases) if bases else ''
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	yield 'class {0}{1}:'.format(self.name, bases)

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def iterDocString():
	    for handler in self.configHandlers('DocString'):
		for line in handler(self):
		    yield self.factory.expr(left=line)
	def intersperseLines(lines):
	    get = lambda o, n:getattr(o, n, None)
	    blank, prev = self.factory.expr(), None
	    for item in lines:
		if type(item) != type(prev) and prev and not get(prev, 'isComment'):
		    yield blank
		elif get(item, 'isMethod') and get(prev, 'isMethod'):
		    yield blank
		elif get(prev, 'isClass'):
		    yield blank
		yield item
		prev = item
	body = list(super(Class, self).iterBody())
	if self.config.last('reorderClassDefs'):
	    body.sort(lambda x, y:-1 if x.isClass else 1)
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, iter(body) if more else intersperseLines(body), more)

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	return chain(*(h(self) for h in self.configHandlers('Epilogue')))


class Annotation(Class):
    """ Annotation -> formatting for annotations converted to Python classes. """
    def __init__(self, config, name=None, type=None, parent=None):
	super(Annotation, self).__init__(config, name, type, parent)

	m = self.factory.method(parent=self, name='__init__')
	m.parameters.append(self.makeParam('*args', 'list'))
	m.parameters.append(self.makeParam('**kwds', 'dict'))
	## set attributes from kwds?

	m = self.factory.method(parent=self, name='__call__')
	m.parameters.append(self.makeParam('klass', 'type'))
	self.factory.expr(parent=m, fs='setattr(klass, self.__class__.__name__, self)')
	self.factory.expr(parent=m, fs='return klass')


class Enum(Class):
    """ Enum -> formatting for enums converted to Python classes. """

class Interface(Class):
    """ Interface -> formatting for interfaces converted to Python classes. """


##
# method and method content types


class MethodContent(Base):
    """ """

class Method(Base):
    """ MethodTemplte -> formatting for Python methods. """
    isMethod = True

    def iterDecorators(self):
	""" Yields decorators for this method. """
	def iterLines():
	    return chain(*(h(self) for h in self.configHandlers('Prologue')))
	def iterOtherDecos():
	    return chain(*(h(self) for h in self.configHandlers('ExtraDecorator')))
	return chain(self.decorators, iterOtherDecos(), iterLines())

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def iterDocString():
	    for handler in self.configHandlers('DocString'):
		for line in handler(self):
		    yield self.factory.expr(left=line)
	body = list(super(Method, self).iterBody())
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, body, more)

    def iterPrologue(self):
	""" Yields items in this method declaration, maybe with decorators. """
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	params = ', '.join(p['name'] for p in self.parameters)
	yield 'def {0}({1}):'.format(self.name, params)



##
# expression and comment types


class Expression(BaseExpression):
    """ Expression -> formatting for Python expressions. """


class Comment(BaseComment):
    """ """




##
# statement types


class Statement(BaseStatement):
    """ Statement -> formatting for Python statements. """

    def iterPrologue(self):
	""" Yields the keyword (and clause, if any) for this statement . """
	yield self.expr


