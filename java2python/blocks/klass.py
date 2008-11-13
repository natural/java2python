#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.blocks.block import Block


class Class(Block):
    """ Class -> specialized block type

    """
    def __init__(self, parent=None, name=None):
        Block.__init__(self, parent, name)
        self.addSource('pass')
        self.isClass = True

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        for handler in self.config.handlers('classHandlers'):
            handler(self)
        offset = self.I(indent)
        for line in self.prefix:
            output.write('%s%s\n' % (offset, line))
        output.write('%s%s\n' % (offset, self.formatDecl()))
        Block.dump(self, output, indent+1)

    @property
    def className(self):
        """

        """
        return self.name

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
        if bases:
            bases = [self.formatExpression(b) for b in bases]
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
