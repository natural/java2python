#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import maybeattr


def fixBaseClasses(block):
    bases = block.bases
    if not bases:
        block.bases = ('object', )
    ## could/should map java to python base classes where possible.


def fixOverloadMethods(block):
    """ adds the overloaded decorator to methods with the same name

    Given input methods F(int a), F(boolean b), this routine creates:

        @overloaded
        def F(...)

        @F.register(bool)
        def F_0(...)

    @return None
    """
    overloads = {}
    for method in block.blockMethods():
        name = method.name
        overloads[name] = 1 + overloads.setdefault(name, 0)
    for name in [n for n, c in overloads.items() if c>1]:
        renames = [m for m in block.blockMethods() if m.name == name]
        first, remainder = renames[0], renames[1:]
        first.preamble.append('@overloaded')
        firstname = first.name
        for index, method in enumerate(remainder):
            params = str.join(', ', [p[0] for p in method.parameters])
            method.preamble.append('@%s.register(%s)' % (firstname, params))
            method.name = '%s_%s' % (method.name, index)


def fixCtor(block):
    """ Declare class member vars in init method

    """
    found = False
    for meth in block.methods:
        if meth.name == '__init__':
            found = True
            break
    if not found and len(list(block.instanceMembers())) > 0:
        meth = block.makeMethod('__init__')
        meth.calledSuperCtor = False
        meth.calledOtherCtor = False
    for meth in block.methods:
        if meth.name == '__init__':
            if not (meth.calledSuperCtor or meth.calledOtherCtor):
                meth.addSourceBefore("super(%s, self).__init__()" % meth.outerClassName(), 0)
                meth.stmtAfterSuper = meth.makeStatementBefore("placeholder", 1) # wtf
            if not meth.calledOtherCtor:
                stmt = meth.stmtAfterSuper
                meth.addSourceBefore("# begin of instance variables", stmt)
                for v in block.variables:
                    if not v.isStatic:
                        meth.addSourceBefore(
                            meth.formatExpression(dict(left=v.name, right=v.expr,
                                 format="self.$left = $right")),
                            stmt)
                idx = meth.lines.index(stmt)
                meth.lines[idx] = "# end of instance variables"


def fixPropMethods(block):
    """ convert methods that look like accessors into properties

    Given input methods F() and F(x), this routine renames them to
    get_F(self) and set_F(self, arg), and includes them as a
    property definition in the class, i.e., F = property(get_F, set_F)

    @return None
    """
    skips = [lambda x:x.name!='__init__', lambda x:'@overloaded' not in x.preamble, ]
    mapping = [(m.name, len(m.parameters)) for m in block.blockMethods()]
    propmap = {}
    for meth in block.blockMethods():
        name = meth.name
        pred = [x(meth) for x in skips]
        if all(pred) and (name, 1) in mapping and (name, 2) in mapping:
            argc = len(meth.parameters)
            methmap = propmap.setdefault(name, {1:None, 2:None})
            methmap[argc] = meth
            meth.name = ('get_%s' if argc==1 else 'set_%s') % name
    lines = block.lines
    for name, meths in propmap.items():
        lines.remove(meths[1])
        lines.remove(meths[2])
    format = '%s = property(%s, %s)'
    for name, meths in propmap.items():
        lines.append(meths[1])
        lines.append(meths[2])
        lines.append(format % (name, meths[1].name, meths[2].name))


def sortClassMethods(block):
    def methodsorter(x, y):
        if maybeattr(x, 'isMethod') and maybeattr(y, 'isMethod'):
            return cmp(x.name, y.name)
        return 0
    block.lines.sort(methodsorter)


def insertModifiers(block):
    prefix = block.prefix
    for mod in block.modifiers:
        isdeco = mod.startswith("@")
        fs = "## %s\n" if isdeco else '## modifier: %s\n'
        prefix.append(fs % (mod, ))

