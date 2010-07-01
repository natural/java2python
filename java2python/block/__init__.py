#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import *
from StringIO import StringIO

from java2python.lib import colortools
from java2python.parser import tokens


def nodeChildren(node, pred=lambda c:True):
    """ Returns all children of the node that meet the predicate. """
    return [c for c in node.children if pred(c)]


def nodeChildrenOfType(node, type):
    """ Returns all children of the node that are of the given type. """
    return nodeChildren(node, lambda c:c.type==type)


def nodeFirstChild(node, pred=lambda c:True, default=None):
    """ Returns the first child of the node that meets the predicate. """
    try:
	return [c for c in node.children if pred(c)][0]
    except (IndexError, ):
	return default


def nodeFirstChildOfType(node, type):
    """ Returns the first child of the node that is of the given type. """
    return nodeFirstChild(node, lambda c:c.type==type)


def nodeParentType(node):
    """ Returns the type of the parent node. """
    return node.parent.type


def walkAST(ast, visitor):
    """ Depth-first visiting of the given AST. """
    block = visitor.accept(ast)
    if block:
	for child in ast.children:
	    walkAST(child, block)


class PythonTemplate(object):
    """ PythonTemplate -> Base class for writing Python source code.

    """
    def __init__(self):
	self.name = self.parent = self.type = None
	self.children = []
	self.modifiers = []
	self.indent = '    '

    def __repr__(self):
	""" x.__repr__() <==> repr(x)

	Returns the debug string representation of this template.
	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(colortools.black('['), colortools.green(self.typeName))
	add(' ', colortools.white('name:'), colortools.cyan(self.name))
	if self.type:
	    add(' ', colortools.white('type:'), colortools.cyan(self.type))
	mods = self.modifiers
	if mods:
	    add(' ', colortools.white('modifiers:'), colortools.cyan(','.join(mods)))
	add(colortools.black(']'))
	return ''.join(parts)

    def __str__(self):
	""" x.__str__() <==> str(x)

	Returns the Python source code representation of this templtae.
	"""
	strfd = StringIO()
	self.dump(strfd, -1)
	source = strfd.getvalue()
	for handler in ():# self.getHandlers('OutputHandlers'):
	    source = handler(self, source)
	return source

    @classmethod
    def build(cls, parent, name=None, type=None):
	""" Alternate constructor for this template type. """
	obj = cls()
	obj.name, obj.parent, obj.type = name, parent, type
	parent.children.append(obj)
	return obj

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file.

	The basic form of dumped lines looks like this:

	    # prologue
	        # child 1
                # child n
            # epilogue

	For modules, the prologue contains the docstring.  The
	epilogue contains the main script stanza (if any).

	For classes and methods, the prologue contains decorators and
	the declaration statement.  The docstring is contained within
	the children.  Enum constants are contained in the class
	epilogue.
	"""
	indent, isNotNone = level * self.indent, lambda x:x is not None
	for line in ifilter(isNotNone, self.iterPrologue()):
	    fd.write('{0}{1}\n'.format(indent, line))
	for item in self.iterBody():
	    item.dump(fd, level+1)
	for line in ifilter(isNotNone, self.iterEpilogue()):
	    fd.write('{0}{1}\n'.format(indent, line))

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	indent = self.indent
	fd.write('{0}{1!r}\n'.format(indent*level, self))
	for child in [o for o in self.children if o]:
	    dumper = getattr(child, 'dumpRepr', lambda x, y:None)
	    dumper(fd, level+1)

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	yield None

    def iterBody(self):
	""" Yields the items in the body of this template. """
	## TODO:  account for docstrings
	if self.children:
	    return iter(self.children)
	return iter([Expression(left='pass')])

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	yield None

    @property
    def isStatic(self):
	""" True if this item is static. """
	return 'static' in self.modifiers

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	return self.__class__.__name__.lower()


class Visitor(object):
    """ Visitor -> Base class for AST visitors.

    """
    def accept(self, node):
	""" Accept a node, possibly creating a child visitor. """
        token, default = node.token, lambda node:self
	tokenType = tokens.map.get(token.type)
	typeTitle = tokens.title(tokenType)
	method = default
	if tokenType:
	    method = getattr(self, 'accept%s' % typeTitle, default)
	return method(node)

    def acceptClass(self, node):
	""" Creates a new class.  Called on Module and Class templates. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	return Class.build(self, name=ident.text)

    def acceptVarDeclaration(self, node):
	""" Creates a new expression for a variable declaration.

	This method really only gets called on Class and Method
	templates, but it's not worth a separate mixin class for just
	one method, so we have it pushed up one level here.
	"""
	mods = nodeChildrenOfType(node, tokens.MODIFIER_LIST)
	decl = nodeFirstChildOfType(node, tokens.VAR_DECLARATOR_LIST)
	for vard in nodeChildrenOfType(decl, tokens.VAR_DECLARATOR):
	    ident = nodeFirstChildOfType(vard, tokens.IDENT)
    	    expr = nodeFirstChildOfType(vard, tokens.EXPR)
	    child = Expression.build(self, left=ident.text)
	    assgn = child.pushRight(' = ')
	    if expr:
		walkAST(expr, assgn)
	    else:
		typ = nodeFirstChildOfType(node, tokens.TYPE)
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ.children[0].text) # wrong
	return self


class ModuleTemplate(PythonTemplate):
    """ ModuleTemplate -> represents a Python module. """


class ModuleVisitor(Visitor):
    """ ModuleVisitor -> accepts AST branches for module-level objects. """


class ClassTemplate(PythonTemplate):
    """ ClassTemplate -> represents a Python class.

    """
    def iterPrologue(self):
	bases = ''
	handler = None # self.getHandler('BaseLookup')
	if handler:
	    bases = [b for b in handler(self) if b is not None]
	    bases = '({0})'.format(', '.join(bases)) if bases else ''
	yield 'class {0}{1}:'.format(self.name, bases)


class ClassVisitor(Visitor):
    """ ClassVisitor -> accepts AST branches for class-level objects.

    """
    def acceptVoidMethodDecl(self, node):
	""" Accept and process a void method declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	method = Method.build(self, name=ident.text, type='void')
	return method

    def acceptFunctionMethodDecl(self, node):
	""" Accept and process a typed method declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	type = nodeFirstChildOfType(node, tokens.TYPE).children[0].text
	method = Method.build(self, name=ident.text, type=type)
	return method


class MethodTemplate(PythonTemplate):
    """ MethodTemplte -> represents a Python method.

    """
    def __init__(self):
	PythonTemplate.__init__(self)
	self.decorators = []
	self.parameters = []
	self.requiresFirstParam = True

    def iterDecorators(self):
	""" Yields decorators for this method. """
	def maybeHandlers():
	    for handler in ():# self.getHandlers('PrologueHandlers'):
		for line in handler(self):
		    yield line
	def maybeClassMethodDeco():
	    if self.isStatic and 'classmethod' not in self.decorators:
		yield 'classmethod'
	return chain(self.decorators, maybeClassMethodDeco(), maybeHandlers())

    def iterPrologue(self):
	""" Yields items in this method declaration, maybe with decorators. """
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	if self.requiresFirstParam:
	    first = ['cls' if self.isStatic else 'self']
	else:
	    first = []
	params = ', '.join(first + [p['name'] for p in self.parameters])
	yield 'def {0}({1}):'.format(self.name, params)


class MethodVisitor(Visitor):
    """ MethodVisitor -> accepts AST branches for method-level objects.

    """
    def acceptModifierList(self, node):
	""" Accept and process method modifiers. """
	if nodeParentType(node) in tokens.methodTypes:
	    self.modifiers = [n.text for n in nodeChildren(node)]
	return self

    def acceptFormalParamStdDecl(self, node):
	""" Accept and process a single parameter declaration. """
	ident = nodeFirstChildOfType(node, tokens.IDENT)
	param = {'name':ident.text}
	self.parameters.append(param)
	return self

    def acceptExpr(self, node):
	""" Creates a new expression. """
	if nodeParentType(node) == tokens.BLOCK_SCOPE:
	    return Expression.build(self)

    def acceptReturn(self, node):
	""" Creates a new return expression. """
	if nodeParentType(node) == tokens.BLOCK_SCOPE:
	    expr = Expression.build(self)
	    expr.left = 'return'
	    if node.children:
		expr.format = '{left} {right}'
		expr.right = Expression.build(expr)
		walkAST(node, expr.right)



class ExpressionTemplate(PythonTemplate):
    """ ExpressionTemplate -> represents a Python expression.

    """
    def __init__(self, left='', right='', format='{left}{right}'):
	PythonTemplate.__init__(self)
	self.left, self.right, self.format = left, right, format

    def __repr__(self):
	""" x.__repr__() <==> repr(x)

	Returns the debug string representation of this template.
	"""
	parts = []
	add = lambda *x:parts.extend(x)
	add(colortools.black('['))
	add(colortools.blue(self.typeName))
	for name, obj in (('left', self.left), ('right', self.right)):
	    ## types other than strings are not formatted; dumpRepr
	    ## handles them directly.
	    if obj and isinstance(obj, (basestring, )):
		#add(' ', colortools.white(name+':'), colortools.yellow(obj))
		add(' ', colortools.yellow(obj))
	add(colortools.black(']'))
	return ''.join(parts)

    def __str__(self):
	""" x.__str__() <==> str(x)

	Returns the Python source code representation of this templtae.
	"""
	return self.format.format(left=self.left, right=self.right)

    @property
    def typeName(self):
	""" Returns the name of this template type. """
	parent = self.parent
	if isinstance(parent, (Expression, )):
	    if self is parent.left:
		return 'left'
	    if self is parent.right:
		return 'right'
	return self.__class__.__name__.lower()

    @classmethod
    def build(cls, parent, name=None, left='', right='', format=None):
	""" Alternate constructor for this template type. """
	obj = cls()
	obj.name, obj.parent = name, parent
	obj.left, obj.right = left, right
	if format:
	    obj.format = format
	parent.children.append(obj)
	return obj

    def dump(self, fd, level=0):
	""" Writes the Python source code for this template to the given file. """
	fd.write('{0}{1}\n'.format(self.indent*level, self))

    def dumpRepr(self, fd, level=0):
	""" Writes a debug string for this template to the given file. """
	fd.write('{0}{1!r}\n'.format(self.indent*level, self))
	for obj in (self.left, self.right):
	    dumper = getattr(obj, 'dumpRepr', lambda x, y:None)
	    dumper(fd, level+1)


class ExpressionVisitor(Visitor):
    """ ClassVisitor -> accepts AST branches for expression objects.

    """


    def assignNodeTextLeft(self, node):
	""" Assigns node text to the left side of this expression. """
	self.left = node.text
    ## accept and process identifiers and constants
    acceptIdent = assignNodeTextLeft
    acceptCharacterLiteral = assignNodeTextLeft
    acceptStringLiteral = assignNodeTextLeft
    acceptFloatingPointLiteral = assignNodeTextLeft
    acceptDecimalLiteral = assignNodeTextLeft
    acceptHexLiteral = assignNodeTextLeft
    acceptOctalLiteral = assignNodeTextLeft
    acceptTrue = assignNodeTextLeft
    acceptFalse = assignNodeTextLeft
    acceptNull = assignNodeTextLeft

    def acceptExpr(self, node):
	""" Create a new expression within this one. """
	return self.pushRight()

    def acceptClassConstructorCall(self, node):
	""" Accept and process a class constructor call. """
	self.acceptMethodCall(node) # probably wrong

    def acceptMethodCall(self, node):
	""" Accept and process a method call. """
	self.format = '{left}({right})'
	self.left = Expression.build(self)
	self.right = Expression.build(self)
	walkAST(nodeFirstChild(node), self.left)
	walkAST(nodeFirstChildOfType(node, tokens.ARGUMENT_LIST), self.right)

    def acceptDot(self, node):
	""" Accept and process a dotted expression. """
	self.format = '{left}.{right}'
	self.left = Expression.build(self)
	self.right = Expression.build(self)
	first, second = nodeChildren(node)
	walkAST(first, self.left)
	walkAST(second, self.right)

    def acceptQuestion(self, node):
	""" Accept and process a terinary expression.

	Turns 'CHECK ? TRUE-COND : FALSE-COND' into 'TRUE-COND if CHECK else FALSE-COND'

	CHECK is the first child of node, TRUE-COND is second, and FALSE-COND is third.
	"""
	self.format = '{left} if {right}'
	self.left = Expression.build(self)
	self.right = Expression.build(self, format='{left} else {right}')
        self.right.left = Expression.build(self.right)
	self.right.right = Expression.build(self.right)
	children = nodeChildren(node)
	walkAST(children[0], self.right.left)
	walkAST(children[1], self.left)
	walkAST(children[2], self.right.right)

    def pushRight(self, value=''):
	""" """
	self.right = Expression.build(self, left=value)
	return self.right


class Module(ModuleTemplate, ModuleVisitor):
    """ Module -> Block representing a Python module. """


class Class(ClassTemplate, ClassVisitor):
    """ Class -> Block representing a Python class. """


class Method(MethodTemplate, MethodVisitor):
    """ Method -> Block representing a Python method. """


class Expression(ExpressionTemplate, ExpressionVisitor):
    """ Expression -> Block representing a Python expression. """
