#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import maybeimport
from java2python.blocks.base import BasicBlock


class Class(BasicBlock):
    """ Class -> specialized block type

    """
    def __init__(self, parent=None, name=None):
        BasicBlock.__init__(self, parent, name)
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
        BasicBlock.dump(self, output, indent+1)

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
                ret[i] = BasicBlock.fixDecl(self, arg)
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

    def makeClass(self):
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


class Method(BasicBlock):
    """ Method -> specialized block type

    """
    instanceFirstParam = ('object', 'self')
    classFirstParam = ('type', 'cls')
    calledSuperCtor = False
    calledOtherCtor = False

    def outerClassName(self):
        for parent in self.allParents():
            if parent.isClass:
                return parent.name
        return None

    def __init__(self, parent, name):
        BasicBlock.__init__(self, parent=parent, name=name)
        self.parameters = [self.instanceFirstParam, ]
        self.addSource('pass')
        self.isMethod = True

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        for handler in self.config.handlers('methodHandlers'):
            handler(self)
        offset = self.I(indent)
        for line in self.prefix:
            output.write('%s%s\n' % (offset, line))
        output.write('%s\n' % (self.formatDecl(indent), ))
        BasicBlock.dump(self, output, indent+1)
        output.write('\n')

    def addModifier(self, name):
        """ adds named modifier to method

        If the modifier corresponds to a decorator, that decorator is
        inserted into the method preamble instead.

        @param name modifier as string
        @return None
        """
        try:
            deco = self.config.combined('modifierDecoratorMap')[name]
        except (KeyError, ):
            pass
        else:
            if deco not in self.preamble:
                self.prefix.append(deco)
                if (deco == self.classmethodLiteral) and (self.parameters) \
                       and (self.parameters[0] == self.instanceFirstParam):
                    self.parameters[0] = self.classFirstParam
        BasicBlock.addModifier(self, name)

    def addParameter(self, typ, name):
        """ adds named parameter to method

        @param typ parameter type as string
        @param name parameter name as string
        @return None
        """
        name = self.alternateName(name)
        typ = BasicBlock.alternateName(self, typ, 'typeTypeMap')
        self.parameters.append((typ, name))
        #self.addVariable(Variable(self, name))
        self.addVariable(name)

    def formatDecl(self, indent):
        """ generates a class statement accounting for base types

        @param indent indentation level of this block
        @return class declaration as string
        """
        name = self.alternateName(self.name)
        parameters = self.parameters
        minparam = self.config.last('minIndentParams', 0)
        if minparam and len(parameters) > minparam:
            first, others = parameters[0], parameters[1:]
            prefix = '%sdef %s(%s, ' % (self.I(indent), name, first[1], )
            offset = '\n' + (' ' * len(prefix))
            decl = '%s%s):' % (prefix, str.join(','+offset, [o[1] for o in others]))
        else:
            params = str.join(', ', [p[1] for p in parameters])
            decl = '%sdef %s(%s):' % (self.I(indent), name, params)
        return decl

    def alternateName(self, name):
        """ returns an alternate for given name

        @param name any string
        @return alternate for name if found; if not found, returns name
        """
        mapping = self.config.combined('renameMethodMap')
        try:
            return mapping[name]
        except (KeyError, ):
            return BasicBlock.alternateName(self, name)


class Module(BasicBlock):
    """ Module -> specialized block type

    Module instances write a preamble before writing their source
    objects.  They write an epilogue as well, and are responsible for
    writing a "if __name__ == '__main__'" block.
    """
    def __init__(self, infile, outfile):
        baseout = outfile.split('.py')[0]
        basein = infile.split('.java')[0]
        name = (baseout if baseout and baseout != '-' else basein)
        BasicBlock.__init__(self, parent=None, name=name)
        self.infile = infile
        self.outfile = outfile

    def dump(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        def doWriters(key):
            for writer in self.config.last(key, ()):
                writer = maybeimport(writer)
                writer(self, output)
        doWriters('modulePreambleWriters')
        BasicBlock.dump(self, output, indent)
        doWriters('moduleEpilogueWriters')
