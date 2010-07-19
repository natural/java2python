#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.compiler.block -> Visitors combined with templates. """
##
# This module defines classes which combine AST walking with source
# generation.  We've put these two behaviors into separate modules,
# java2python.compiler.template for creating source code, and
# java2python.compiler.visitor for walking Antlr trees.
#
# Each of the base classes depends on the behavior of its counterpart.
# This means they're very tightly coupled and that the classes are not
# very reusable.  The module split does allow for grouping of related
# methods and does hide some of the cluttered code.
#
# The template base class defines a factory for creating new block
# instances.  This was necessary to avoid lookups to the module
# namespace for classes that weren't there.  The factory also makes
# creating block instances a bit easier.
#
from itertools import chain, ifilter

from java2python.compiler import template, visitor
from java2python.lang import tokens
from java2python.lib import FS


class ModuleTemplate(template.BaseTemplate):
    """ ModuleTemplate -> formatting for Python modules. """
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


class TypeDeclVisitorMixin(object):
    """ TypeDeclVisitorMixin -> shared visitor methods for type declarations """

    def makeAcceptType(ft):
	def accept(self, node, memo):
	    name = node.firstChildOfType(tokens.IDENT).text
	    self.variables.append(name)
	    return getattr(self.factory, ft)(name=name, parent=self)
	return accept

    acceptAt = makeAcceptType('at')
    acceptClass = makeAcceptType('klass')
    acceptEnum = makeAcceptType('enum')
    acceptInterface = makeAcceptType('interface')


class ModuleVisitor(TypeDeclVisitorMixin, visitor.BaseVisitor):
    """ ModuleVisitor -> accepts AST branches for module-level objects. """


class ClassTemplate(template.BaseTemplate):
    """ ClassTemplate -> formatting for Python classes. """
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
	body = list(super(ClassTemplate, self).iterBody())
	docs = list(iterDocString())
	more = [self.factory.expr(left='pass')] if not (body or docs) else []
	return chain(docs, iter(body) if more else intersperseLines(body), more)

    def iterEpilogue(self):
	""" Yields the items in the epilogue of this template. """
	return chain(*(h(self) for h in self.configHandlers('Epilogue')))


class ClassVisitor(TypeDeclVisitorMixin, visitor.BaseVisitor):
    """ ClassVisitor -> accepts AST branches for class-level objects. """

    def acceptAt(self, node, memo):
	""" Accept and ignore an annotation declaration. """
	## this overrides the TypeDeclVisitorMixin implementation and
	## ignores AT tokens; they're sent within the class modifier
	## list and we have to use for them here.

    def acceptAnnotationMethodDecl(self, node, memo):
	""" Accept and process a typed method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	type = node.firstChildOfType(tokens.TYPE).children[0].text
	return self.factory.method(name=ident.text, type=type, parent=self)

    def acceptConstructorDecl(self, node, memo):
	""" Accept and process a constructor declaration. """
	method = self.factory.method(name='__init__', type=self.name, parent=self)
	superCalls = node.findChildrenOfType(tokens.SUPER_CONSTRUCTOR_CALL)
	if not any(superCalls) and any(self.bases):
	    ## from the java tutorial:
	    # Note: If a constructor does not explicitly invoke a
	    # superclass constructor, the Java compiler automatically
	    # inserts a call to the no-argument constructor of the
	    # superclass.
	    fs = 'super(' + FS.r + ', self).__init__()'
	    self.factory.expr(fs=fs, right=self.name, parent=method)
	return method

    def acceptExtendsClause(self, node, memo):
	""" Accept and process an extends clause. """
	names = (n.text for n in node.findChildrenOfType(tokens.IDENT))
	self.bases.extend(names)

    def acceptFunctionMethodDecl(self, node, memo):
	""" Accept and process a typed method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	type = node.firstChildOfType(tokens.TYPE).children[0].text
	return self.factory.method(name=ident.text, type=type, parent=self)

    acceptImplementsClause = acceptExtendsClause

    def acceptModifierList(self, node, memo):
	for mod in node.children:
	    if mod.type == tokens.AT:
		## needs args, too
		self.decorators.append(mod.firstChildOfType(tokens.IDENT).text)
	    else:
		self.modifiers.append(mod.text)
	return self

    def acceptVarDeclaration(self, node, memo):
	""" Creates a new expression for a variable declaration. """
	#mods = node.childrenOfType(tokens.MODIFIER_LIST)
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

    def acceptVoidMethodDecl(self, node, memo):
	""" Accept and process a void method declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	return self.factory.method(name=ident.text, type='void', parent=self)


class AnnotationTemplate(ClassTemplate):
    """ AnnotationTemplate -> formatting for annotations converted to Python classes. """


class AnnotationVisitor(ClassVisitor):
    """ AnnotationVisitor -> accepts AST branches for Java annotations. """


class EnumTemplate(ClassTemplate):
    """ EnumTemplate -> formatting for enums converted to Python classes. """


class EnumVisitor(ClassVisitor):
    """ EnumVisitor -> accepts AST branches for Java enums. """

    def acceptEnumTopLevelScope(self, node, memo):
	""" Accept and process an enum scope """
	idents = node.childrenOfType(tokens.IDENT)
	expr = self.factory.expr
	clsset = lambda v:'{0}.{1} = {2}'.format(self.name, v, self.name)
	handler = self.configHandler('Value')
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


class InterfaceTemplate(ClassTemplate):
    """ InterfaceTemplate -> formatting for interfaces converted to Python classes. """


class InterfaceVisitor(ClassVisitor):
    """ InterfaceVisitor -> accepts AST branches for Java interfaces. """


class MethodTemplate(template.BaseTemplate):
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


class MethodContentVisitor(visitor.BaseVisitor):
    """ MethodContentVisitor -> accepts trees for blocks within methods. """

    def acceptWhile(self, node, memo):
	""" Accept and process a while block. """
	# WHILE - PARENTESIZED_EXPR - BLOCK_SCOPE
	parNode, blkNode = node.children
	whileStat = self.factory.statement('while', fs=FS.lsrc, parent=self)
	whileStat.expr.walk(parNode, memo)
	whileStat.walk(blkNode, memo)

    def acceptDo(self, node, memo):
	""" Accept and process a do-while block. """
	# DO - BLOCK_SCOPE - PARENTESIZED_EXPR
	blkNode, parNode = node.children
	whileStat = self.factory.statement('while', fs=FS.lsrc, parent=self)
	whileStat.expr.right = 'True'
	whileStat.walk(blkNode, memo)
	fs = FS.l+ ' ' + 'not ({right}):'
	ifStat = self.factory.statement('if', fs=fs, parent=whileStat)
	ifStat.expr.walk(parNode, memo)
	breakStat = self.factory.statement('break', parent=ifStat)

    def acceptSwitch(self, node, memo):
	""" Accept and process a switch block. """
	# This implementation needs a lot of work to handle case
	# statements without breaks, out-of-order default labels, etc.
	# Given the current size and complexity, consider growing a
	# Case block type.
	parNode = node.firstChildOfType(tokens.PARENTESIZED_EXPR)
	lblNode = node.firstChildOfType(tokens.SWITCH_BLOCK_LABEL_LIST)
	caseNodes = lblNode.children
        ## empty switch statement
	if not len(caseNodes):
	    return
	## we have at least one node...
	parExpr = self.factory.expr()
	parExpr.walk(parNode)
	eqFs = FS.l + '==' + FS.r
	for caseIdx, caseNode in enumerate(caseNodes):
	    isDefault, isFirst = caseNode.type==tokens.DEFAULT, caseIdx==0

	    if isFirst:
   	        caseExpr = self.factory.statement('if', fs=FS.lsrc, parent=self)
	    elif not isDefault:
		caseExpr = self.factory.statement('elif', fs=FS.lsrc, parent=self)
	    elif isDefault:
		caseExpr = self.factory.statement('else', fs=FS.lc, parent=self)

	    if not isDefault:
		right = self.factory.expr()
		right.walk(caseNode.firstChildOfType(tokens.EXPR))
		caseExpr.expr.right = self.factory.expr(left=parExpr, right=right, fs=eqFs)
		caseContent = self.factory.methodContent(parent=self)
		for child in caseNode.children[1:]:
		    caseContent.walk(child, memo)
		if not caseNode.children[1:]:
		    self.factory.expr(left='pass', parent=caseContent)
	    if isDefault:
		if isFirst:
		    caseExpr.expr.right = 'True'
		caseContent = self.factory.methodContent(parent=self)
		for child in caseNode.children:
		    caseContent.walk(child, memo)
		if not caseNode.children:
		    self.factory.expr(left='pass', parent=caseContent)

    def acceptCatch(self, node, memo):
	""" Accept and process a catch statement. """
	decl = node.firstChildOfType(tokens.FORMAL_PARAM_STD_DECL)
	dtype = decl.firstChildOfType(tokens.TYPE)
	tnames = dtype.findChildrenOfType(tokens.IDENT)
	cname = '.'.join(n.text for n in tnames)
	cvar = decl.firstChildOfType(tokens.IDENT)
	block = node.firstChildOfType(tokens.BLOCK_SCOPE)
	self.expr.fs = FS.lsrc
	self.expr.right = self.factory.expr(fs=FS.l+' as '+FS.r, left=cname, right=cvar)
	self.walk(block, memo)

    def acceptAssert(self, node, memo):
	""" Accept and process an assert statement. """
	assertStat = self.factory.statement('assert', fs=FS.lsr, parent=self)
	assertStat.expr.walk(node.firstChild(), memo)

    def acceptIf(self, node, memo):
	""" Accept and process an if statement. """
	## the parser will feed us one of three forms:
	## bare if:          PARENTESIZED_EXPR - BLOCK_SCOPE
	## if with else:     PARENTESIZED_EXPR - BLOCK_SCOPE - BLOCK_SCOPE
	## if with else if:  PARENTESIZED_EXPR - BLOCK_SCOPE - IF
	children = node.children
	ifStat = self.factory.statement('if', fs=FS.lsrc, parent=self)
	ifStat.expr.walk(children[0], memo)
	ifBlock = self.factory.methodContent(parent=self)
	ifBlock.walk(node.children[1], memo)
	if len(children) == 3:
	    nextNode = children[2]
	    nextType = nextNode.type
	    while nextType == tokens.IF:
		nextStat = self.factory.statement('elif', fs=FS.lsrc, parent=self)
		nextStat.expr.walk(nextNode.children[0], memo)
		nextBlock = self.factory.methodContent(parent=self)
		nextBlock.walk(nextNode.children[1], memo)
		try:
		    nextNode = nextNode.children[2]
		    nextType = nextNode.type
		except (IndexError, ):
		    nextType = None
	    if nextType == tokens.BLOCK_SCOPE:
		self.factory.statement('else', fs=FS.lc, parent=self)
		self.factory.methodContent(parent=self).walk(nextNode, memo)

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
	goodParents = (tokens.BLOCK_SCOPE, tokens.CASE, tokens.DEFAULT, tokens.FOR_EACH)
	if node.parentType in goodParents: # wrong
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
	varDecls = node.firstChildOfType(tokens.VAR_DECLARATOR_LIST)
	for varDecl in varDecls.childrenOfType(tokens.VAR_DECLARATOR):
	    ident = varDecl.firstChildOfType(tokens.IDENT)
	    identExp = self.factory.expr(left=ident.text, parent=self)
	    assgnExp = identExp.pushRight(' = ')
	    declExp = varDecl.firstChildOfType(tokens.EXPR)
	    declArr = varDecl.firstChildOfType(tokens.ARRAY_INITIALIZER)
	    if declExp:
		assgnExp.walk(declExp, memo)
            elif declArr:
		assgnExp.right = exp = self.factory.expr(fs='['+FS.lr+']')
		children = list(declArr.childrenOfType(tokens.EXPR))
		for child in children:
		    fs = FS.lr if child is children[-1] else FS.lr + ', '
		    exp.left = self.factory.expr(fs=fs)
		    exp.left.walk(child, memo)
		    exp.right = exp = self.factory.expr()
	    else:
		typ = node.firstChildOfType(tokens.TYPE)
		typ = typ.children[0].text
		val = assgnExp.pushRight()
		val.left = '{0}()'.format(typ) # wrong
	return self

    def acceptForEach(self, node, memo):
	""" Accept and process a 'for each' style statement. """
	forEach = self.factory.statement('for', fs=FS.lsrc, parent=self)
	identExpr = forEach.expr.right = self.factory.expr(fs=FS.l+' in '+FS.r)
	identExpr.walk(node.firstChildOfType(tokens.IDENT), memo)
	inExpr = identExpr.right = self.factory.expr()
	inExpr.walk(node.firstChildOfType(tokens.EXPR), memo)
	forBlock = self.factory.methodContent(parent=self)
	#print '############', [tokens.map[n.type] for n in node.children]
	#forBlock.walk(node.firstChildOfType(tokens.BLOCK_SCOPE), memo)
	forBlock.walk(node.children[4], memo)

    def acceptFor(self, node, memo):
	""" Accept and process a 'for' statement. """
	self.walk(node.firstChildOfType(tokens.FOR_INIT))
	whileStat = self.factory.statement('while', fs=FS.lsrc, parent=self)
	whileStat.expr.walk(node.firstChildOfType(tokens.FOR_CONDITION))
	whileBlock = self.factory.methodContent(parent=self)
	whileBlock.walk(node.firstChildOfType(tokens.BLOCK_SCOPE))
	updateStat = self.factory.expr(parent=whileBlock)
	updateStat.walk(node.firstChildOfType(tokens.FOR_UPDATE))


class MethodVisitor(MethodContentVisitor):
    """ MethodVisitor -> accepts AST branches for method-level objects. """

    def acceptModifierList(self, node, memo):
	""" Accept and process method modifiers. """
	if node.parentType in tokens.methodTypes:
	    self.modifiers.extend(n.text for n in node.children) ## wrong
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
	#ptype = self.config.last('typeSubs').get(ptype, ptype)
	self.parameters.append(self.makeParam(ident.text, ptype))
	return self

    def acceptFormalParamVarargDecl(self, node, memo):
	""" Accept and process a var arg declaration. """
	ident = node.firstChildOfType(tokens.IDENT)
	param = {'name':'*{0}'.format(ident.text), 'type':'A'}
	self.parameters.append(param)
	return self


class ExpressionTemplate(template.BaseExpressionTemplate):
    """ ExpressionTemplate -> formatting for Python expressions. """


class ExpressionVisitor(visitor.BaseVisitor):
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
	self.left, self.right = visitors = expr(parent=self), expr()
	self.zipWalk(node.children, visitors, memo)

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
	self.left, self.right = visitors = expr(parent=self), expr()
	self.zipWalk(node.children, visitors, memo)

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
	self.left = name = self.altIdent(node.text)

    def acceptClassConstructorCall(self, node, memo):
	""" Accept and process a class constructor call. """
	self.acceptMethodCall(node, memo) # probably wrong

    def acceptMethodCall(self, node, memo):
	""" Accept and process a method call. """
	## note: this creates one too many expression levels.
	expr = self.factory.expr
	self.fs = FS.l + '(' + FS.r + ')'
	self.left = expr(parent=self)
	self.left.walk(node.firstChild(), memo)
	self.right = arg = expr(parent=self)
	nodes = node.firstChildOfType(tokens.ARGUMENT_LIST).children
	for tree in nodes:
	    fs = FS.r + (', ' if tree is not nodes[-1] else '')
	    arg.walk(tree, memo)
	    arg.left = expr(fs=fs, parent=self)
	    arg.left.walk(tree, memo)
	    arg.right = arg = expr()

    def acceptPostInc(self, node, memo):
	""" """
	self.fs = FS.l + ' += 1'
	self.left = self.factory.expr()
	return self.left

    def makeAcceptPreFormatted(fs):
	def accept(self, node, memo):
	    expr = self.factory.expr
	    self.fs = fs
	    self.left, self.right = visitors = expr(), expr()
	    self.zipWalk(node.children, visitors, memo)
	return accept

    acceptDot = makeAcceptPreFormatted(FS.l + '.' + FS.r)
    acceptDiv = makeAcceptPreFormatted(FS.l + ' / ' +FS.r)
    acceptMinus = makeAcceptPreFormatted(FS.l + ' - ' +FS.r)
    acceptPlus = makeAcceptPreFormatted(FS.l + ' + ' +FS.r)
    acceptStar = makeAcceptPreFormatted(FS.l + ' *' +FS.r)
    acceptArrayElementAccess = makeAcceptPreFormatted(FS.l + '[' + FS.r + ']')

    def acceptSuperConstructorCall(self, node, memo):
	cls = self.parents(lambda c:c.isClass).next()
	fs = 'super(' + FS.l + ', self).__init__(' + FS.r + ')'
	self.right = self.factory.expr(fs=fs, left=cls.name)
	return self.right

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
	visitors = (self.right.left, self.left, self.right.right)
	self.zipWalk(node.children, visitors, memo)

    def pushRight(self, value=''):
	""" Creates a new right expression, sets it, and returns it. """
	self.right = self.factory.expr(left=value, parent=self)
	return self.right


class CommentTemplate(template.BaseCommentTemplate):
    """ """

class CommentVisitor(ExpressionVisitor):
    """ """


class StatementTemplate(template.BaseStatementTemplate):
    """ StatementTemplate -> formatting for Python statements. """

    def iterPrologue(self):
	""" Yields the keyword (and clause, if any) for this statement . """
	yield self.expr


class StatementVisitor(MethodContentVisitor):
    """ StatementVisitor -> accepts AST branches for statement objects. """


##
# Now we can mix the template and visitor classes to make concrete
# types.
#
##

class Annotation(AnnotationTemplate, AnnotationVisitor):
    """ Enum -> represents a Java annotation as a Python class. """
    factoryTypeName = 'at'

class Class(ClassTemplate, ClassVisitor):
    """ Class -> represents a Java class as a Python class. """
    factoryTypeName = 'klass'

class Comment(CommentTemplate, CommentVisitor):
    """ Comment -> represents a Java comment as a Python comment. """
    factoryTypeName = 'comment'

class Enum(EnumTemplate, EnumVisitor):
    """ Enum -> represents a Java enum as a Python class. """
    factoryTypeName = 'enum'

class Expression(ExpressionTemplate, ExpressionVisitor):
    """ Expression -> represents a Java expression as a Python expression. """
    factoryTypeName = 'expr'

class Interface(InterfaceTemplate, InterfaceVisitor):
    """ Interface -> represents a Java interface as a Python class. """
    factoryTypeName = 'interface'

class Method(MethodTemplate, MethodVisitor):
    """ Method -> represents a Java method as a Python method. """
    factoryTypeName = 'method'

class MethodContent(template.BaseTemplate, MethodContentVisitor):
    """ MethodContent -> represents Java block content in a Python method. """
    factoryTypeName = 'methodContent'

class Module(ModuleTemplate, ModuleVisitor):
    """ Module -> represents a Java compilation unit as a Python module. """
    factoryTypeName = 'module'

class Statement(StatementTemplate, StatementVisitor):
    """ Statement -> represents a Java statement as a Python statement. """
    factoryTypeName = 'statement'
