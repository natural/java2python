#!/usr/bin/env python
# -*- coding: utf-8 -*-

from antlr3 import CommonTokenStream
from antlr3.tree import CommonTreeAdaptor, TreeParser

from java2python.blocks import BlockStack
from java2python.parser import JavaLexer



class LocalTreeParser(TreeParser):
    """ Replacement tree parser base class.

    """
    def __init__(self, *a, **b):
	super(LocalTreeParser, self).__init__(*a, **b)
        self.commentHandler = self.sourceStack = None

    def onJavaSource(self, module):
        """ Called by the tree parser when walking begins.

        """
        self.commentHandler = CommentFormatter(self)
        self.sourceStack = BlockStack(module)

    def __getattr__(self, name):
        """ Defer failed attribute lookups to the source stack object.

        """
        return getattr(self.sourceStack, name)


class LocalTreeAdaptor(CommonTreeAdaptor):
    """ Replacement tree adapter that copies comment sequences from
        lexer tokens to tree tokens.

        Check the Java.g grammar file to see how this class is used.
    """
    def createWithPayload(self, payload):
	token = super(LocalTreeAdaptor, self).createWithPayload(payload)
        token.comments = getattr(payload, 'comments', None)
        return token


class LocalTokenStream(CommonTokenStream):
    """ Token stream subclass that saves comment sequences in lexed
        tokens.

    """
    commentTargetTypes = [
        JavaLexer.CLASS,
        JavaLexer.IDENT,
        JavaLexer.EXPR,
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
        self.reallySaveComments(vals, cursor)


    def reallySaveComments(self, values, cursor):
        try:
            comments = getattr(self.tokens[cursor], 'comments', None)
        except (IndexError, ):
            pass
        else:
            if comments is None:
                self.tokens[cursor].comments = values[:]
            else:
                for comment in values:
                    if comment not in comments:
                        comments.append(comment)


class CommentFormatter(object):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, start):
        input, source = self.parser.input, self.parser.sourceStack
        start_idx = input.getTreeAdaptor().getTokenStartIndex(start)
        stop_idx = input.getTreeAdaptor().getTokenStopIndex(start)
        tokens = input.tokens.tokens[start_idx:stop_idx]
        comments = [(t, getattr(t, 'comments', None)) for t in tokens]
        comments = [(t, c) for t, c in comments if c]

        for token, comment_set in reversed(comments):
            token.comments = None
            for typ, val in reversed(comment_set):
                for handler in source.top.config.handlers('commentHandlers'):
                    handler(source.top, val, typ)
