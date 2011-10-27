#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest

from java2python.compiler import buildAST
from java2python.lang import tokens
from java2python.lang.selector import Token, Type
from java2python.lib import colors


def setUpModule():
    fn = os.path.join(os.path.dirname(__file__), 'Selector1.java')
    SelectorTest.tree = buildAST(open(fn).read())
    SelectorTest.tree.dump(sys.stdout)


class SelectorTest(unittest.TestCase):
    def walk(self, selector):
        return list(selector.walk(self.tree))

    def assertNodes(self, nodes, length):
        self.assertTrue(nodes)
        self.assertEqual(len(nodes), length)

    def shortDescription(self):
        fs = 'Description: {}\nSelector: {}\n'
        args = (colors.cyan(self.description), colors.yellow(self.selector))
        return fs.format(*args)

    @classmethod
    def make(cls, count):
        def t(self):
            nodes = self.walk(self.selector)
            self.assertNodes(nodes, count)
        return t


class TestIdentChildOfClass(SelectorTest):
    description = 'select one IDENT node that is a child of a CLASS node'
    selector = Type('CLASS') > Type('IDENT')
    test = SelectorTest.make(1)


class TestIdentWithText(SelectorTest):
    description = 'select two IDENT nodes with text "foo"'
    selector = Type('IDENT', 'foo')
    test = SelectorTest.make(2)


class TestTokensWithText(SelectorTest):
    description = 'select two nodes with text "foo"'
    selector = Token(text='foo')
    test = SelectorTest.make(2)


class TestTokenCallableCombo(SelectorTest):
    description = 'select BLOCK_SCOPE on line 7'
    selector = Token(type=lambda t: t.type == tokens.BLOCK_SCOPE, line=7)
    test = SelectorTest.make(1)


class TestTokenMultipleCallables(SelectorTest):
    description = 'select BLOCK_SCOPE on line 2 or 7'
    selector = Token(type=lambda t: t.type == tokens.BLOCK_SCOPE, line=lambda t:t.line in (2, 7))
    test = SelectorTest.make(2)


class TestTokenChildCallable(SelectorTest):
    description = 'select BLOCK_SCOPE with one child IDENT starting with "f"'
    selector = Token(type=lambda t: t.type == tokens.BLOCK_SCOPE) & Token(type='IDENT', text=lambda tok:tok.text.startswith('f'))
    test = SelectorTest.make(1)


class TestNthChildWithExtraChecks(SelectorTest):
    description = 'select two children of FORMAL_PARAM_STD_DECL at index 2 '
    selector = Type('FORMAL_PARAM_STD_DECL')[2]

    def test(self):
        nodes = self.walk(self.selector)
        self.assertNodes(nodes, 2)
        self.assertEquals(nodes[0].type, tokens.IDENT)
        self.assertEquals(nodes[1].type, tokens.IDENT)
        self.assertEquals(nodes[0].text, 'x')
        self.assertEquals(nodes[1].text, 'y')


class TestDirectChildren(SelectorTest):
    description = 'select two TYPE nodes that are children of a VAR_DECLARATION node'
    selector = Type('VAR_DECLARATION') > Type('TYPE')
    test = SelectorTest.make(2)


class TestSimpleSiblings(SelectorTest):
    description = 'select three IDENT nodes that are adjacent siblings of a MODIFIER_LIST'
    selector = Type('MODIFIER_LIST') + Type('IDENT')
    test = SelectorTest.make(3)


class TestSimpleAnySibling(SelectorTest):
    description = 'select three FORMAL_PARAM_LIST nodes that are non-adjacent siblings of a MODIFIER_LIST'
    selector = Type('MODIFIER_LIST') / Type('FORMAL_PARAM_LIST')
    test = SelectorTest.make(2)


class TestClassIdent(SelectorTest):
    description = 'select one IDENT node that is a child of a CLASS node'
    selector = Type('CLASS') > Type('IDENT')
    test = SelectorTest.make(1)
