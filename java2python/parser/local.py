#!/usr/bin/env python
# -*- coding: utf-8 -*-

from antlr3 import CommonTokenStream
from antlr3.tree import CommonTreeAdaptor, TreeParser

from java2python import maybeAttr
from java2python.blocks import BlockStack
from java2python.parser import JavaLexer


class LocalTreeParser(TreeParser):
    """ Replacement tree parser base class.

    """
    def __init__(self, input, state=None):
	super(LocalTreeParser, self).__init__(input, state=state)
        self.commentHandler = self.sourceStack = None

    def __getattr__(self, name):
        """ Defer failed attribute lookups to the source stack object.

        """
        return getattr(self.sourceStack, name)

    def beginJavaSource(self, module):
        """ Called by the tree parser when walking begins.

        """
        self.commentHandler = self.makeCommentHandler()
        self.sourceStack = BlockStack(module)


    def endJavaSource(self):
        pass

    def makeCommentHandler(self):
        """ Makes and returns a function for handling comments.

            The returned function defers actual comment handling to the
            callables defined in the configuration modules.
        """
        def handler(start):
	    start_idx = start.tokenStartIndex
            stop_idx = start.tokenStopIndex
            tokens = self.input.tokens.tokens[start_idx:stop_idx]
            comments = [(t, maybeAttr(t, 'comments')) for t in tokens]
            comments = [(t, c) for t, c in comments if c]
            for token, comment_set in reversed(comments):
                token.comments = None
                for typ, val in reversed(comment_set):
                    for handler in self.sourceStack.commentHandlers:
                        handler(self.sourceStack.previousOrTop, val, typ)
        return handler


class LocalTokenStream(CommonTokenStream):
    """ Token stream subclass that saves comment sequences in lexed
        tokens.

    """
    commentTargetTypes = [
        JavaLexer.IDENT,
        JavaLexer.CLASS,
        JavaLexer.FUNCTION_METHOD_DECL,
        JavaLexer.CLASS_TOP_LEVEL_SCOPE,
        JavaLexer.VOID_METHOD_DECL,
        JavaLexer.FUNCTION_METHOD_DECL,
        JavaLexer.EXPR,
	JavaLexer.VAR_DECLARATION,
	JavaLexer.LOCAL_MODIFIER_LIST
    ]

    def skipOffTokenChannels(self, start):
        stop = start
        try:
            while self.tokens[stop].channel != self.channel:
                stop += 1
        except (IndexError, ):
            pass
        self.maybeSaveComments(start, stop)
        return stop

    def maybeSaveComments(self, start, stop):
        vals = [(t.getType(), t.getText()) for t in self.tokens[start:stop]]
        vals = [(typ, txt) for typ, txt in vals if txt.strip()]
        cursor = start
        try:
            ## seek backward to a suitable token
            while self.tokens[cursor].getType() not in self.commentTargetTypes:
                if not cursor: break
                cursor -= 1
        except (IndexError, ):
            pass
        if not cursor:
            cursor = start
            ## no suiltable token found looking backward, seek forward
            ## instead (this happens with comments before initial
            ## declaration in input source)
            while self.tokens[cursor].getType() not in self.commentTargetTypes:
                cursor += 1
	if vals:
	    self.reallySaveComments(vals, cursor, stop)

    def reallySaveComments(self, values, start, stop):
        comments = maybeAttr(self.tokens[start], 'comments')
        if comments is None:
            self.tokens[start].comments = values[:]
        else:
            for comment in values:
                if comment not in comments:
                    comments.append(comment)

