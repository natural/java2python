#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.sourcetypes.block import Block, maybeAttr


class Class(Block):
    """ Class -> specialized block type

    """
    def __init__(self, parent=None, name=None):
        Block.__init__(self, parent, name)
        self.addSource('pass')

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        config = self.config

        ## move this next chunk of code to and override of addSource;
        ## don't like modifications during write
        if config.last('fixPropMethods'):
            self.fixPropMethods()
        if config.last('fixOverloadMethods'):
            self.fixOverloadMethods()
        if config.last('sortClassMethods'):
            def methodsorter(x, y):
                if maybeAttr(x, 'isMethod') and maybeAttr(y, 'isMethod'):
                    return cmp(x.name, y.name)
                return 0
            self.lines.sort(methodsorter)

        ## write the decorators and modifiers
        name = self.name
        offset = self.I(indent)
        for mod in self.modifiers:
            isdeco = mod.startswith("@")
            if config.last('writeModifiersComments') or isdeco:
                fs = "%s## %s\n" if isdeco else '%s## modifier: %s\n'
                output.write(fs % (offset, mod))

        ## write the docstring
        offset = self.I(indent+1)
        output.write('%s%s\n' % (self.I(indent), self.formatDecl()))
        if config.last('writeClassDocString'):
            output.write('%s""" generated source for %s\n\n' % (offset, name))
            output.write('%s"""\n' % (offset, ))

        ## write the lines
        Block.dump(self, output, indent+1)

    @property
    def className(self):
        """

        """
        return self.name

    @property
    def isClass(self):
        """ True if this instance is a Class

        """
	return True

    @property
    def extraVars(self):
        """ extra variable names from base classes (defined externally)

        @return sequence of variable names
        """
        extras = []
        comb = self.config.combined
        for base in self.bases:
            extras.extend(comb('baseClassMembers').get(base, []))
        return extras

    def addBaseClass(self, name):
        """ add a base class by name

        @param name base class name as string
        @return None
        """
        if name and (name not in self.bases):
            #name = self.formatExpression(name) ## just for now -- fix me later!
            self.bases.append(name)

    def addModifier(self, name):
        """ add a modifier to this source block

        @param name value of modifier, as a string
        @return None
        """
	## check 2vs3 and adjust -- class decos not supported in 2.x.
        self.modifiers.append(name)

    def fixDecl(self, *args):
        """ fixes variable names that are class members

        @varparam args names to fix
        @return fixed name or names
        """
        ret = list(args)
        for i, arg in enumerate(args):
            if self.name != arg:
                ret[i] = Block.fixDecl(self, arg)
        if len(ret) > 1:
            return ret
        else:
            return ret[0]

    def formatDecl(self):
        """ generates a class statement accounting for base types

        @return class declaration as string
        """
        bases = self.bases
        name = self.name
        if not bases and self.config.last('classesInheritObject'):
            bases = ('object', )
        if bases:
            decl = 'class %s(%s):' % (name, str.join(', ', bases))
        else:
            decl = 'class %s:' % (name, )
        return decl

    def newClass(self):
        """ creates a new Class object as a child of this block

        This implementation accounts for inner classes; i.e., when
        classes are defined within classes, they are moved to the
        beginning of the block.  This allows the rest of the (outer)
        class definition to reference the inner class.

        @keyparam name=None name of new method
        @return Class instance
        """
        c = Class(parent=self, name=None)
        if self.config.last('bubbleInnerClasses'):
            self.addSourceBefore(c, 0)
        else:
            self.addSource(c)
        return c

    def fixPropMethods(self):
        """ convert methods that look like accessors into properties

        Given input methods F() and F(x), this routine renames them to
        get_F(self) and set_F(self, arg), and includes them as a
        property definition in the class, i.e., F = property(get_F, set_F)

        @return None
        """
	skips = [lambda x:x.name!='__init__', lambda x:'@overloaded' not in x.preamble, ]
        mapping = [(m.name, len(m.parameters)) for m in self.blockMethods]
        propmap = {}
        for meth in self.blockMethods:
            name = meth.name
	    pred = [x(meth) for x in skips]
            if all(pred) and (name, 1) in mapping and (name, 2) in mapping:
                argc = len(meth.parameters)
                methmap = propmap.setdefault(name, {1:None, 2:None})
                methmap[argc] = meth
                meth.name = ('get_%s' if argc==1 else 'set_%s') % name
        lines = self.lines
        for name, meths in propmap.items():
            lines.remove(meths[1])
            lines.remove(meths[2])
        format = '%s = property(%s, %s)'
        for name, meths in propmap.items():
            lines.append(meths[1])
            lines.append(meths[2])
            lines.append(format % (name, meths[1].name, meths[2].name))

    def fixOverloadMethods(self):
        """ adds the overloaded decorator to methods with the same name

        Given input methods F(int a), F(boolean b), this routine creates:

            @overloaded
            def F(...)

            @F.register(bool)
            def F_0(...)

        @return None
        """
        overloads = {}
        for method in self.blockMethods:
            name = method.name
            overloads[name] = 1 + overloads.setdefault(name, 0)
        for name in [n for n, c in overloads.items() if c>1]:
            renames = [m for m in self.blockMethods if m.name == name]
            first, remainder = renames[0], renames[1:]
            first.preamble.append('@overloaded')
            firstname = first.name
            for index, method in enumerate(remainder):
                params = str.join(', ', [p[0] for p in method.parameters])
                method.preamble.append('@%s.register(%s)' % (firstname, params))
                method.name = '%s_%s' % (method.name, index)

    def fixCtor(self):
        """Declare class member vars in init method

        """
        found = False
        for meth in self.methods:
            if meth.name == '__init__':
                found = True
                break
        if not found and len(list(self.instanceMembers)) > 0:
            meth = self.newMethod('__init__')
            meth.calledSuperCtor = False
            meth.calledOtherCtor = False
        for meth in self.methods:
            if meth.name == '__init__':
                if not (meth.calledSuperCtor or meth.calledOtherCtor):
                    meth.addSourceBefore("super(%s, self).__init__()" % meth.outerClassName, 0)
                    meth.stmtAfterSuper = meth.newStatementAbove("if", 1)
                if not meth.calledOtherCtor:
                    stmt = meth.stmtAfterSuper
                    meth.addSourceBefore("# begin of instance variables", stmt)
                    for v in self.variables:
                        if not v.isStatic:
                            meth.addSourceBefore(
                                ("self.%s = %s", (("%s", v.name), v.expr)),
                                stmt)
                    idx = meth.lines.index(stmt)
                    meth.lines[idx] = "# end of instance variables"

