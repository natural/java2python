#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from itertools import ifilter
from StringIO import StringIO

from java2python.lib import FS
from java2python.lib.colortools import *


class Factory(object):
    """ Factory -> creates pre-configured callables for new factory type instances.

    """
    types = {}

    def __init__(self, config):
	self.config =  config

    def __getattr__(self, name):
	return partial(self.types.get(name), self.config)


class FactoryTypeDetector(type):
    """ FactoryTypeDetector -> detects factory-creatable types as they are defined.

    """
    def __init__(cls, name, bases, namespace):
	try:
	    Factory.types[cls.factoryTypeName] = cls
	except (AttributeError, ):
	    pass


class BaseTemplate(object):
    """ BaseTemplate -> base class for formatting Python output.

    """
    __metaclass__ = FactoryTypeDetector
    isClass = isComment = isExpression = isMethod = isModule = False

    def __init__(self, config, name=None, type=None, parent=None):
	self.config = config
	self.name = name
	self.type = type
	self.parent = parent
	self.children = []
	self.modifiers = []
	self.variables = []
	self.factory = Factory(config)
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

    def configHandler(self, part, suffix='Handler', default=None):
	""" Returns the config handler for this type of template. """
	name = '{0}{1}{2}'.format(self.typeName, part, suffix)
	return self.config.handler(name, default)

    def configHandlers(self, part, suffix='Handlers', default=None):
	""" Returns config handlers for this type of template """
	name = '{0}{1}{2}'.format(self.typeName, part, suffix)
	return self.config.handlers(name, default)

    def dumps(self, level=0):
	""" Dumps this template to a string. """
	fd = StringIO()
	self.dump(fd, level)
	return fd.getvalue()

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	indent, isNotNone = level * self.indent, lambda x:x is not None
	for line in ifilter(isNotNone, self.iterPrologue()):
	    fd.write('{0}{1}\n'.format(indent, line))
	for item in self.iterBody():
	    item.dump(fd, level+1)
	for line in ifilter(isNotNone, self.iterEpilogue()):
	    fd.write('{0}{1}\n'.format(indent, line))

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	indent, default = self.indent, lambda x, y:None
	fd.write('{0}{1!r}\n'.format(indent*level, self))
	for child in ifilter(None, self.children):
	    getattr(child, 'dumpRepr', default)(fd, level+1)

    @property
    def indent(self):
	""" Returns the indent string for this item. """
	return self.config.last('leadingIndent', '    ')

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

    def renameIdent(self, name):
	isClass = lambda v:v.isClass
	isMethod = lambda v:v.isMethod
	for klass in self.parents(isClass):
	    if name in klass.variables:
		method = self.parents(isMethod).next()
		if name in [p['name'] for p in method.parameters]:
		    return name
		return ('cls' if method.isStatic else 'self') + '.' + name
	return name

    def parents(self, pred=lambda v:True):
	while self:
	    if pred(self):
		yield self
	    self = self.parent

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	return self.__class__.__name__.lower()


class BaseExpressionTemplate(BaseTemplate):
    """ BaseExpressionTemplate -> base class for formatting Python expressions.

    """
    isExpression = True

    def __init__(self, config, left='', right='', fs=FS.lr, parent=None, tail=''):
	super(BaseExpressionTemplate, self).__init__(config, parent=parent)
	self.left, self.right, self.fs, self.tail = left, right, fs, tail

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts = [blue(self.typeName)]
	if isinstance(self.left, (basestring, )) and self.left:
	    parts.append(white('left:')+yellow(self.left))
	if isinstance(self.right, (basestring, )) and self.right:
	    parts.append(white('right:')+yellow(self.right))
	if self.tail:
	    parts.append(white('tail:')+yellow(self.tail))
	return ' '.join(parts)

    def __str__(self):
	""" Returns the Python source code representation of this template. """
	return self.fs.format(left=self.left, right=self.right) + self.tail

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	fd.write('{0}{1}\n'.format(self.indent*level, self))

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


class BaseCommentTemplate(BaseExpressionTemplate):
    def __repr__(self):
	parts = [white(self.typeName+':'),
		 black(self.left) + black(self.right) + black(self.tail)]
	return ' '.join(parts)


class BaseStatementTemplate(BaseTemplate):
    """ BaseStatementTemplate -> base class for formatting Python statements.

    """
    def __init__(self, config, keyword, fs=FS.lr, parent=None):
	super(BaseStatementTemplate, self).__init__(config, parent=parent)
	self.keyword = keyword
	self.expr = self.factory.expr(left=keyword, fs=fs)

    def __repr__(self):
	""" Returns the debug string representation of this template. """
	parts = [green('statement'), white('keyword:')+cyan(self.keyword)]
	return ' '.join(parts)
