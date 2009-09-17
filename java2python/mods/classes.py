#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
from collections import defaultdict
from logging import debug, warn
from java2python import maybeAttr, isDict


def convertProperties(block):
    """ convert methods that look like accessors into properties

    Given input methods F() and F(x), this routine renames them to
    get_F(self) and set_F(self, arg), and includes them as a
    property definition in the class, i.e., F = property(get_F, set_F)

    @return None
    """
    namesArgCounts = [(m.name, len(m.parameters)) for m in block.methods]
    blockPredicates = [
        lambda x:x.name!='__init__',
        lambda x:len([n for n, argc in namesArgCounts if n==x.name]) == 2,
    ]

    propMethods = defaultdict(lambda:{1:None, 2:None})
    gettr, settr = 1, 2

    for meth in block.methods:
        name = meth.name
        tests = [predicate(meth) for predicate in blockPredicates]
        if all(tests) and (name, gettr) in namesArgCounts and (name, settr) in namesArgCounts:
            argc = len(meth.parameters)
            methmap = propMethods[name]
            methmap[argc] = meth
            meth.name = ('get_%s' if argc==gettr else 'set_%s') % name
    fs = '%s = property(%s, %s)'
    blocks = block.blocks
    for name, meths in propMethods.items():
        blocks.remove(meths[gettr])
        blocks.remove(meths[settr])
        blocks.append(meths[gettr])
        blocks.append(meths[settr])
        blocks.append(fs % (name, meths[gettr].name, meths[settr].name))


def insertModifiersAsComments(block):
    """

    """
    comment = block.config.last('commentPrefix', '#')
    fs = '%s modifier: %s\n'
    for mod in block.modifiers:
        block.preamble.append(fs % (comment, mod, ))


def overloadMethods(block):
    """ adds the overloaded decorator to methods with the same name

    Given input methods F(int a), F(boolean b), this routine creates:

        @overloaded
        def F(...)

        @F.register(bool)
        def F_0(...)

    @return None
    """
    overloads = defaultdict(lambda:0)
    for method in block.methods:
        overloads[method.name] += 1
    for name in [n for n, c in overloads.items() if c>1]:
        renames = [m for m in block.methods if m.name==name]
        first, remainder = renames[0], renames[1:]
        first.decorators.append('overloaded')
        firstname = first.name
        for index, method in enumerate(remainder):
            params = [block.renameType(p.get('type')) for p in method.parameters]
            params = str.join(', ', params)
            method.decorators.append('%s.register(%s)' % (firstname, params))
            method.name = '%s_%s' % (method.name, index)


def sortMethodsKey(item):
    """ sort key for methods:  returns method name if possible

    """
    return item.name if maybeAttr(item, 'isMethod') else item


def sortMethods(block, key=sortMethodsKey):
    """ sorts methods using given key; default key sorts by method name

    """
    block.blocks.sort(key=key)


def updateBases(block, bases=['object']):
    """ adds the specified default base classes if the base classes of
        the block are empty
    """
    if not block.bases:
        block.bases.extend(bases)


def updateConstructor(block):
    """ Declare class member vars in init method

    """
    variables = block.variables
    meth = block.initMethod
    if not meth and variables and maybeAttr(block, 'isMethod'):
        meth = block.makeMethod('__init__')
    else:
        return

    if not meth.hasSuperCall:
        meth.append("super(%s, self).__init__()" % meth.outerClassName, index=0)
    stmt = meth.blocks[-1]
    if variables:
        meth.addComment("begin instance variables")
        for v in variables:
            if not v.isStatic:
                expr = meth.formatExpression(dict(left=v.name, right=v.expr, format="self.$left"))
                meth.append(expr)
        meth.addComment('end instance variables')
    #if not meth.hasSuperCall: # and variables:

