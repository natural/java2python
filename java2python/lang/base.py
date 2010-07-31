#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# ANTLR notes:
#
# recognizers: lexer, parser, treeparser
# streams: string, file name, file handle
#
# Parsers use TokenStreams (CommonTokenStream or TokenRewriteStream)
#
# Tree parsers use TreeNodeStream (CommonTreeNodeStream)
#
# Lexers emit Token objects (buffered in TokenStream objects)
#
# Parsers build trees if their output is AST.
#
# token types: CommonToken and ClassicToken.  Our tree adaptor
# creates LocalTree instances instead.
#
# Tree (CommonTree) wraps Token objects.  We provide extra functionality via
# the LocalTree class.
#
# TreeAdaptor (CommonTreeAdaptor) is used by the parser to create
# Tree objects.  Our adaptor, TreeAdaptor, creates the LocalTree
# instances.
#
##
from antlr3 import ANTLRStringStream as StringStream, CommonTokenStream as TokenStream
from antlr3.tree import CommonTreeAdaptor, CommonTree
from java2python.lib import colortools


class Tokens(object):
    """ Tokens -> simplifies token id-name and name-id mapping. """

    def __init__(self):
	self.cache, self.parserModule = {}, None

    def __getattr__(self, name):
	""" tokenname -> tokenvalue """
	return getattr(self.module, name)

    @property
    def commentTypes(self):
	""" Well-known comment types. """
	mod = self.module
	return (mod.COMMENT, mod.LINE_COMMENT, mod.JAVADOC_COMMENT, )

    @property
    def methodTypes(self):
	""" Well-known method types. """
	mod = self.module
        return (mod.VOID_METHOD_DECL, mod.FUNCTION_METHOD_DECL, )

    @property
    def map(self):
	""" tokentype -> tokenname mapping as a dictionary """
	cache, module = self.cache, self.module
	if cache:
	    return cache
	mapping = [(getattr(module, k, None), k) for k in module.tokenNames]
	mapping = [(k, v) for k, v in mapping if k is not None]
	cache.update(mapping)
	return cache

    @property
    def module(self):
	""" Provides lazy import to the parser module. """
	module = self.parserModule
	if module:
	    return module
	import java2python.lang.JavaParser as module
	self.parserModule = module
	return module

    @staticmethod
    def title(name):
	""" Returns a nice title given a token type name. """
	return ''.join(part.title() for part in name.split('_'))


## sometimes you really do only need one.
tokens = Tokens()


class TreeAdaptor(CommonTreeAdaptor):
    """ TreeAdaptor -> defered tree node creator (for parsers) """

    def __init__(self, lexer, parser):
	# CommonTreeAdaptor doesn't need to be __init__'ed
	self.lexer, self.parser = lexer, parser

    def createWithPayload(self, payload):
	""" Returns a new tree for the calling parser. """
        return LocalTree(payload, self.lexer, self.parser)


class LocalTree(CommonTree):
    """ LocalTree -> like CommonTree, but with much more stuff

    """
    colorTypeMap = {
	'CLASS'            : colortools.green,
	'JAVA_SOURCE'      : colortools.green,
	'VOID_METHOD_DECL' : colortools.green,
	'IDENT'            : colortools.yellow,
	'TYPE'             : colortools.magenta,
	'EXPR'             : colortools.blue,
	'TRUE'             : colortools.yellow,
	'FALSE'            : colortools.yellow,
	'NULL'             : colortools.yellow,
    }

    def __init__(self, payload, lexer=None, parser=None):
	super(LocalTree, self).__init__(payload)
	self.lexer, self.parser = lexer, parser

    def childrenOfType(self, type):
	""" Returns a generator yielding children of this tree of the given type. """
	return (c for c in self.children if c.type==type)

    def colorType(self, tokenType):
	""" Returns a color suitable for the given token type. """
	return self.colorTypeMap.get(tokenType, colortools.white)(tokenType)

    def colorText(self, tokenType, tokenText):
	""" Returns a colorized string from the given token type and text. """
	return self.colorTypeMap.get(tokenType, colortools.white)(tokenText)

    def colorComments(self, token):
	""" Formats, colors, and returns the comment text from the given token. """
	ttyp = tokens.map.get(token.type)
	text = token.text.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
	item = '{0} [{1}:{2}] {3}'.format(ttyp, token.start, token.stop, text)
	yield colortools.black(item)

    def dump(self, fd, level=0):
	""" Writes a debug representation of this tree to the given file. """
	extras = lambda x, y:x and (x != y)
	seen, nform = set(), '{0}{1}{2}{3}'
	def innerDump(root, offset):
	    token, indent = root.token, '    ' * offset
	    start, stop = root.tokenStartIndex, root.tokenStopIndex
	    idxes, ttyp = '', tokens.map.get(token.type, '?')
	    if start and stop and start == stop:
		idxes = ' [{0}]'.format(start)
	    elif start and stop:
	        idxes = ' [{0}:{1}]'.format(start, stop)
	    args = [indent, self.colorType(ttyp), '', idxes, '']
	    if extras(token.text, ttyp):
		args[2] = ' ' + self.colorText(ttyp, token.text)
	    for com in self.selectComments(start, seen):
		for line in self.colorComments(com):
		    print >> fd, '{0}{1}'.format(indent, line)
	    print >> fd, nform.format(*args)
	    for child in root.getChildren():
		innerDump(child, offset+1)
	    for com in self.selectComments(root.tokenStopIndex, seen):
		for line in self.colorComments(com):
		    print >> fd, '{0}{1}'.format(indent, line)
	innerDump(self, level)

    def dupNode(self):
	""" Called by the parser to create a duplicate of this tree. """
	get = lambda v:getattr(self, v, None)
	return LocalTree(self, get('lexer'), get('parser'))

    def findChildren(self, pred=lambda c:True):
	""" Depth-first search that yields nodes meeting the predicate. """
	for child in self.children:
	    if pred(child):
		yield child
	    for sub in child.findChildren(pred):
		yield sub

    def findChildrenOfType(self, type):
	""" Depth-first search that yields nodes of the given type. """
	return self.findChildren(lambda c:c.type==type)

    def firstChild(self, default=None):
	""" Returns the first child of this tree or the default. """
	try:
	    return self.children[0]
	except (IndexError, ):
	    return default

    def firstChildOfType(self, type, default=None):
	""" Returns the first child of this tree that matches the given type. """
	for child in self.children:
	    if child.type == type:
		return child
	return default

    @property
    def isJavaSource(self):
	""" True if this tree is the outer most type. """
	return self.token.type == tokens.JAVA_SOURCE

    @property
    def parentType(self):
	""" Returns the type of the parent tree. """
	return self.parent.type

    @property
    def parserTokens(self):
	""" Returns the sequence of tokens used to create this tree. """
	return self.parser.input.tokens[self.tokenStartIndex:self.tokenStopIndex]

    def selectComments(self, stop, memo):
	""" Returns the comment tokens for this tree up to the given index. """
	pred = lambda k:k.type in tokens.commentTypes and k.index not in memo
	ctoks = [t for t in self.parser.input.tokens[0:stop] if pred(t)]
	memo.update(t.index for t in ctoks)
	return ctoks

    @property
    def withinExpr(self):
	""" True if this tree is contained within an expression. """
	self = getattr(self.parent, 'parent', None) # skip first expr
	while self:
	    if self.type in (tokens.EXPR, ):
		return True
	    self = self.parent
