#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks -> AST visitors combined with python syntax templates.

"""
from itertools import chain

from java2python.block.template import BaseExpressionTemplate, BaseStatementTemplate, BaseTemplate
from java2python.block.visitor import BaseVisitor
from java2python.lib import FS
from java2python.parser import tokens


class ModuleTemplate(BaseTemplate):
    """ ModuleTemplate -> formatting for Python modules. """

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	for handler in self.configHandlers('PrologueHandlers'):
	    for line in handler(self):
		yield line

    def iterBody(self):
	""" Yields the items in the body of this template. """
	get = lambda o, n:getattr(o, n, None)
	children, prev = self.children, None
	space = [self.factory.expr(), self.factory.expr()]
	for index, child in enumerate(children):
	    if prev and not get(child, 'isComment') and not get(prev, 'isClass') and get(child, 'isClass'):
		for line in space:
		    yield line
	    yield child
	    prev = child

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	for handler in self.configHandlers('EpilogueHandlers'):
	    for line in handler(self):
		yield line


class ModuleVisitor(BaseVisitor):
    """ ModuleVisitor -> accepts AST branches for module-level objects. """


class ClassTemplate(BaseTemplate):
    """ ClassTemplate -> formatting for Python classes. """
    isClass = True

    def __init__(self, config, name=None, type=None, parent=None):
	super(ClassTemplate, self).__init__(config, name, type, parent)
	self.bases = []

    def iterPrologue(self):
	""" Yields the items in the prologue of this template. """
	handler = self.configHandler('BaseHandler', lambda b:b)
	bases = [b for b in handler(self) if b is not None]
        bases = '({0})'.format(', '.join(bases)) if bases else ''
	yield 'class {0}{1}:'.format(self.name, bases)

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def iterDocString():
	    for handler in self.configHandlers('DocStringHandlers'):
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
	body = list(super(ClassTemplate, self).iterBody())
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, iter(body) if more else intersperseLines(body), more)

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	for handler in self.configHandlers('EpilogueHandlers'):
	    for line in handler(self):
		yield line


class ClassVisitor(BaseVisitor):
    """ ClassVisitor -> accepts AST branches for class-level objects. """

    def acceptVarDeclaration(self, node, memo):
	""" Creates a new expression for a variable declaration. """
	mods = node.childrenOfType(tokens.MODIFIER_LIST)
	decl = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for vard in decl.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = vard.firstChildOfType(tokens.IDENT)
	    self.variables.append(ident.text)
    	    expr = vard.firstChildOfType(tokens.EXPR)
	    child = self.factory.expr(left=ident.text, parent=self)
	    assgn = child.pushRight(' = ')
	    if expr:
		assgn.walk(expr, memo)
	    else:
		typ = node.firstChildOfType(tokens.TYPE)
		typ = typ.children[0].text
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self

    def acceptConstructorDecl(self, node, memo):
	""" Accept and process a constructor declaration. """
	return self.factory.method(name='__init__', type=self.name, parent=self)

    def acceptExtendsClause(self, node, memo):
	""" Accept and process an extends clause. """
	names = (n.text for n in node.findChildrenOfType(tokens.IDENT))
	self.bases.append('.'.join(names))

    def acceptFunctionMethodDecl(self, node, memo):
	""" Accept and process a typed method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	type = node.firstChildOfType(tokens.TYPE).children[0].text
	return self.factory.method(name=ident.text, type=type, parent=self)

    def acceptVoidMethodDecl(self, node, memo):
	""" Accept and process a void method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	return self.factory.method(name=ident.text, type='void', parent=self)


class EnumTemplate(ClassTemplate):
    """ EnumTemplate -> formatting for enums converted to Python classes. """


class EnumVisitor(ClassVisitor):
    """ EnumVisitor -> accepts AST branches for Java enums. """

    def acceptEnumTopLevelScope(self, node, memo):
	""" Accept and process an enum scope """
	idents = node.childrenOfType(tokens.IDENT)
	expr = self.factory.expr
	clsset = lambda v:'{0}.{1} = {2}'.format(self.name, v, self.name)
	handler = self.configHandler('ValueHandler')

	for index, ident in enumerate(idents):
	    if list(ident.findChildrenOfType(tokens.ARGUMENT_LIST)):
		call = expr(left=clsset(ident), parent=self.parent)
		call.right = arg = expr(fs='('+FS.lr+')')
		argl = ident.firstChildOfType(tokens.ARGUMENT_LIST)
		exprs = list(argl.findChildrenOfType(tokens.EXPR))
		for ex in exprs:
		    arg.left = expr(fs=FS.r + (', ' if ex != exprs[-1] else ''))
		    arg.left.walk(ex, memo)
		    arg.right = arg = expr()
	    else:
		value = expr(fs=ident.text+' = '+FS.r, parent=self)
		value.pushRight(handler(self, index, ident.text))
	return self


class MethodTemplate(BaseTemplate):
    """ MethodTemplte -> formatting for Python methods. """
    isMethod = requiresFirstParam = True

    def __init__(self, config, name=None, type=None, parent=None):
	super(MethodTemplate, self).__init__(config, name, type, parent)
	self.decorators = []
	self.parameters = [self.makeParam('self', 'object')]

    def makeParam(self, name, type):
	return {'name':name, 'type':type}

    def iterDecorators(self):
	""" Yields decorators for this method. """
	def iterLines():
	    for handler in self.configHandlers('PrologueHandlers'):
		for line in handler(self):
		    yield line
	def iterOtherDecos():
	    for handler in self.configHandlers('ExtraDecoratorHandlers'):
		for line in handler(self):
		    yield line
	return chain(self.decorators, iterOtherDecos(), iterLines())

    def iterBody(self):
	""" Yields the items in the body of this template. """
	def iterDocString():
	    for handler in self.configHandlers('DocStringHandlers'):
		for line in handler(self):
		    yield self.factory.expr(left=line)
	body = list(super(MethodTemplate, self).iterBody())
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, body, more)

    def iterPrologue(self):
	""" Yields items in this method declaration, maybe with decorators. """
	for deco in self.iterDecorators():
	    yield '@{0}'.format(deco)
	params = ', '.join(p['name'] for p in self.parameters)
	yield 'def {0}({1}):'.format(self.name, params)


class MethodContentVisitor(BaseVisitor):
    """ MethodContentVisitor -> accepts trees for blocks within methods. """

    def acceptCatch(self, node, memo):
	""" Accept and process a catch statement. """
	decl = node.firstChildOfType(tokens.FORMAL_PARAM_STD_DECL)
	dtype = decl.firstChildOfType(tokens.TYPE)
	tnames = dtype.findChildrenOfType(tokens.IDENT)
	cname = '.'.join(n.text for n in tnames)
	cname = self.config.combined('exceptionSubMap').get(cname, cname)
	cvar = decl.firstChildOfType(tokens.IDENT)
	block = node.firstChildOfType(tokens.BLOCK_SCOPE)
	self.expr.fs = FS.lsrc
	self.expr.right = Expression(self.config, fs=FS.l+' as '+FS.r, left=cname, right=cvar)
	self.walk(block, memo)

    def acceptAssert(self, node, memo):
	""" Accept and process an assert statement. """
	assertStat = self.factory.statement('assert', fs=FS.lsr, parent=self)
	assertStat.expr.walk(node.firstChild(), memo)

    def acceptIf(self, node, memo):
	""" Accept and process an if statement. """
	ifStat = self.factory.statement('if', fs=FS.lsrc, parent=self)
	ifStat.expr.walk(node.firstChildOfType(tokens.PARENTESIZED_EXPR), memo)
	blockNodes = node.childrenOfType(tokens.BLOCK_SCOPE)
	ifBlock = self.factory.methodContent(parent=self)
	ifBlock.walk(blockNodes[0], memo)
	if len(blockNodes) == 2:
	    elseStat = self.factory.statement('else', fs=FS.lc, parent=self)
	    elseBlock = self.factory.methodContent(parent=self)
	    elseBlock.walk(blockNodes[1], memo)

    def acceptThrow(self, node, memo):
	""" Accept and process a throw statement. """
	throw = self.factory.statement('raise', fs=FS.lsr, parent=self)
	throw.expr.walk(node.children[0], memo)

    def acceptTry(self, node, memo):
	""" Accept and process a try/catch block. """
	children = node.children
	tryNode = children[0]
	if len(children) == 3:
	    catchClausesNode, finNode = children[1:3]
	elif len(children) == 2:
	    catchClausesNode = finNode = None
	    if children[1].type == tokens.CATCH_CLAUSE_LIST:
		catchClausesNode = children[1]
	    else:
		finNode = children[1]
        tryStat = self.factory.statement('try', fs=FS.lc, parent=self)
	tryStat.walk(tryNode, memo)
	if catchClausesNode:
	    for catchNode in catchClausesNode.children:
		exStat = self.factory.statement('except', fs=FS.lsrc, parent=self)
		exStat.walk(catchNode, memo)
	if finNode:
	    finStat = self.factory.statement('finally', fs=FS.lc, parent=self)
	    finStat.walk(finNode, memo)

    def acceptExpr(self, node, memo):
	""" Creates a new expression. """
	if node.parentType == tokens.BLOCK_SCOPE: # wrong
	    return self.factory.expr(parent=self)

    def acceptReturn(self, node, memo):
	""" Creates a new return expression. """
	if node.parentType == tokens.BLOCK_SCOPE: # wrong
	    expr = self.factory.expr(left='return', parent=self)
	    if node.children:
		expr.fs, expr.right = FS.lsr, self.factory.expr(parent=expr)
		expr.right.walk(node, memo)

    def acceptVarDeclaration(self, node, memo):
	""" Creates a new expression for a variable declaration. """
	mods = node.childrenOfType(tokens.MODIFIER_LIST)
	decl = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for vard in decl.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = vard.firstChildOfType(tokens.IDENT)
    	    expr = vard.firstChildOfType(tokens.EXPR)
	    child = self.factory.expr(left=ident.text, parent=self)
	    assgn = child.pushRight(' = ')
	    ## also might be an array
	    array = vard.firstChildOfType(tokens.ARRAY_INITIALIZER)
	    if expr:
		assgn.walk(expr, memo)
            elif array:
		assgn.left = self.factory.expr(fs='['+FS.l+', '+FS.r)
		assgn.left.walk(array, memo)
	    else:
		typ = node.firstChildOfType(tokens.TYPE)
		typ = typ.children[0].text
		val = assgn.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self

    def acceptForEach(self, node, memo):
	""" Accept and process a for (each style) statement. """
	forEach = self.factory.statement('for', fs=FS.lsrc, parent=self)
	identExpr = forEach.expr.right = self.factory.expr(fs=FS.l+' in '+FS.r)
	identExpr.walk(node.firstChildOfType(tokens.IDENT), memo)
	inExpr = identExpr.right = self.factory.expr()
	inExpr.walk(node.firstChildOfType(tokens.EXPR), memo)
	forBlock = self.factory.methodContent(parent=self)
	forBlock.walk(node.firstChildOfType(tokens.BLOCK_SCOPE), memo)

class MethodVisitor(MethodContentVisitor):
    """ MethodVisitor -> accepts AST branches for method-level objects. """

    def acceptModifierList(self, node, memo):
	""" Accept and process method modifiers. """
	if node.parentType in tokens.methodTypes:
	    self.modifiers.extend(n.text for n in node.children)
	    if self.isStatic:
		self.parameters[0]['name'] = 'cls'
	return self

    def acceptFormalParamStdDecl(self, node, memo):
	""" Accept and process a single parameter declaration. """
	ident = node.firstChildOfType(tokens.IDENT)

        # wrong, wrong, wrong.
	ptype = list(node.findChildrenOfType(tokens.TYPE))[0]
	try:
	    ptype = list(ptype.findChildrenOfType(tokens.IDENT))[0].text
	except:
	    ptype = ptype.firstChild().text
	ptype = self.config.combined('typeSubstitutionMap').get(ptype, ptype)
	self.parameters.append(self.makeParam(ident.text, ptype))
	return self

    def acceptFormalParamVarargDecl(self, node, memo):
	""" Accept and process a var arg declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	param = {'name':'*{0}'.format(ident.text), 'type':'A'}
	self.parameters.append(param)
	return self


class ExpressionTemplate(BaseExpressionTemplate):
    """ ExpressionTemplate -> formatting for Python expressions. """


class ExpressionVisitor(BaseVisitor):
    """ ClassVisitor -> accepts trees for expression objects. """

    def textExpression(self, node, memo):
	""" Assigns node text to the left side of this expression. """
	self.left = node.text

    acceptCharacterLiteral = textExpression
    acceptStringLiteral = textExpression
    acceptFloatingPointLiteral = textExpression
    acceptDecimalLiteral = textExpression
    acceptHexLiteral = textExpression
    acceptOctalLiteral = textExpression
    acceptTrue = textExpression
    acceptFalse = textExpression
    acceptNull = textExpression

    def equalityExpression(self, node, memo):
	""" Accept and processes an equality expression. """
	expr = self.factory.expr
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = expr(self.config, parent=self), expr(self.config)
	self.zipWalk(node.children, (self.left, self.right), memo)

    acceptEqual = equalityExpression
    acceptGreaterOrEqual = equalityExpression
    acceptGreaterThan = equalityExpression
    acceptLessOrEqual = equalityExpression
    acceptLessThan = equalityExpression
    acceptNotEqual = equalityExpression

    def assignExpression(self, node, memo):
	""" Accept and processes an assignment expression (Python statement). """
	expr = self.factory.expr
	self.fs = FS.l + ' ' + node.text + ' ' + FS.r
	self.left, self.right = expr(self.config, parent=self), expr(self.config)
	self.zipWalk(node.children, (self.left, self.right), memo)

    acceptAssign = assignExpression
    acceptPlusAssign = assignExpression
    acceptMinusAssign = assignExpression
    acceptStarAssign = assignExpression
    acceptDivAssign = assignExpression
    acceptAndAssign = assignExpression
    acceptOrAssign = assignExpression
    acceptXorAssign = assignExpression
    acceptModAssign = assignExpression
    acceptShiftLeftAssign = assignExpression
    acceptShiftRightAssign = assignExpression

    def acceptExpr(self, node, memo):
	""" Create a new expression within this one. """
	return self.pushRight()

    def acceptIdent(self, node, memo):
	""" Accept and process an ident expression. """
	name = self.lookupIdent(node.text)
	self.left = name

    def acceptClassConstructorCall(self, node, memo):
	""" Accept and process a class constructor call. """
	self.acceptMethodCall(node, memo) # probably wrong

    def acceptMethodCall(self, node, memo):
	""" Accept and process a method call. """
	expr = self.factory.expr
	self.fs = FS.l + '(' + FS.r + ')'
	self.left, self.right = expr(parent=self), expr(parent=self)
	self.left.walk(node.firstChild(), memo)
	self.right.walk(node.firstChildOfType(tokens.ARGUMENT_LIST), memo)

    def acceptDot(self, node, memo):
	""" Accept and process a dotted expression. """
	expr = self.factory.expr
	self.fs = FS.l + '.' + FS.r
	self.left, self.right = expr(parent=self), expr(parent=self)
	self.zipWalk(node.children, (self.left, self.right), memo)

    def acceptThis(self, node, memo):
	self.pushRight('self')

    def acceptQuestion(self, node, memo):
	""" Accept and process a terinary expression. """
	expr = self.factory.expr
	self.fs = FS.l + ' if ' + FS.r
	self.left = expr(parent=self)
	self.right = expr(fs=FS.l+' else '+FS.r, parent=self)
        self.right.left = expr(parent=self.right)
	self.right.right = expr(parent=self.right)
	self.zipWalk(node.children, (self.right.left, self.left, self.right.right), memo)

    def pushRight(self, value=''):
	""" Creates a new right expression, sets it, and returns it. """
	self.right = self.factory.expr(left=value, parent=self)
	return self.right


class StatementTemplate(BaseStatementTemplate):
    """ StatementTemplate -> formatting for Python statements. """

    def iterPrologue(self):
	""" Yields the keyword (and clause, if any) for this statement . """
	yield self.expr


class StatementVisitor(MethodContentVisitor):
    """ StatementVisitor -> accepts AST branches for statement objects. """



class Module(ModuleTemplate, ModuleVisitor):
    """ Module -> represents a Java compilation unit as a Python module. """
    factoryTypeName = 'module'


class Class(ClassTemplate, ClassVisitor):
    """ Class -> represents a Java class as a Python class. """
    factoryTypeName = 'klass'


class Enum(EnumTemplate, EnumVisitor):
    """ Enum -> represents a Java enum as a Python class. """
    factoryTypeName = 'enum'


class Method(MethodTemplate, MethodVisitor):
    """ Method -> represents a Java method as a Python method. """
    factoryTypeName = 'method'


class MethodContent(BaseTemplate, MethodContentVisitor):
    """ MethodContent -> represents Java block content in a Python method. """
    factoryTypeName = 'methodContent'


class Expression(ExpressionTemplate, ExpressionVisitor):
    """ Expression -> represents a Java expression as a Python expression. """
    factoryTypeName = 'expr'


class Statement(StatementTemplate, StatementVisitor):
    """ Statement -> represents a Java statement as a Python statement. """
    factoryTypeName = 'statement'
