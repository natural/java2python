#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.base -> basic building block of output source code.

"""
from cStringIO import StringIO
from itertools import chain
from logging import debug, warn, exception
from re import sub as rxsub
from string import Template

from java2python import maybeAttr
from java2python.config import Config


class BlockPropShard:
    """ Block properties, sharded for easy reading.

    """
    @property
    def blockMethods(self):
        """ all source objects that are methods """
        return (m for m in self.lines if maybeAttr(m, 'isMethod'))

    @property
    def family(self):
        """ this object and its parents """
        return chain([self], self.parents)

    @property
    def instanceMembers(self):
        """ all instance members in this class """
        for obj in self.family:
	    if obj.isClass:
                for v in obj.variables:
                    if not v.isStatic:
                        yield v.name
                for v in obj.extraVars:
                    yield v

    @property
    def instanceMethods(self):
        """ all instance methods in this class """
        for obj in self.family:
	    if obj.isClass:
                for v in obj.methods:
                    if not v.isStatic:
                        yield v.name

    @property
    def isStatic(self):
        """ True if this instance is static """
        return 'static' in self.modifiers

    @property
    def methodVars(self):
        """ all vars declared in the current method """
        for obj in self.family:
            for v in obj.variables:
                yield v.name
            if obj.isMethod:
		break

    @property
    def nameOrClassName(self):
        """ the closest class name """
        for obj in self.family:
            if obj.isClass:
                return obj.name

    @property
    def outerClassName(self):
        """ the closest outer class name """
        for obj in self.parents:
            if obj.isClass:
                return obj.name

    @property
    def outerMethod(self):
        """ the closest outer method """
        for obj in self.family:
            if obj.isMethod:
                return obj

    @property
    def parents(self):
        """ generates each ancestor of this instance """
        previous = self.parent
        while previous:
            yield previous
            previous = previous.parent

    @property
    def staticMembers(self):
        """ all static members in this class """
        for obj in self.family:
	    if obj.isClass:
                for v in obj.variables:
                    if v.isStatic:
                        yield v.name

    @property
    def staticMethods(self):
        """ all static methods in this class """
        for obj in self.family:
	    if obj.isClass:
                for v in obj.methods:
                    if v.isStatic:
                        yield v.name

    @property
    def initMethod(self):
        """ returns the __init__ method from this block """
        for meth in self.methods:
            if meth.name == '__init__':
                return meth


class BlockAddingShard:
    """ Block methods for adding content.

    """
    def addComment(self, text, prefix='# ', index=None):
        """ add a comment to this source block

        @param text value of comment
        @keyparam prefix='##' value of comment prefix
        @return None
        """
        prefix = self.config.last('commentPrefix', prefix)
        self.addSource('%s%s' % (prefix, text), index)

    def addMethod(self, meth):
        self.methods.append(meth)

    def addModifier(self, name):
        """ add a modifier to this source block

        @param name value of modifier, as a string
        @return None
        """
        self.modifiers.append(name)

    def addSource(self, src, index=None):
        """ add source code to the end of this block

        @param src string, instance of BasicBlock (or subclass), or two-tuple
        @return None
        """
        lines = self.lines
        val = self.formatExpression(src) if isinstance(src, dict) else src
        if lines == ['pass'] and val:
            lines.pop()
        if index is None:
            lines.append(src)
        else:
            if index in lines:
                index = lines.index(index)
            lines.insert(index, src)

    def addVariable(self, obj, force=False):
        """ add variable name to set for tracking

        Variables are only added to Class instances unless the force
        parameter True.

        @param name variable as string
        @keyparam force=False, if True, always add to set
        @return None
        """
        from java2python.blocks import Variable
        if isinstance(obj, (Variable, )):
            var = obj
        else:
            var = Variable(obj)
            var.name = obj
        if force or (var.name and self.isClass):
            self.variables.append(var)
        return var


class BlockMakerShard:
    """ This class provides a set of alternate constructors for the
        various subclasses.

    """
    def makeClass(self, name=None):
        """ creates a new Class object as a child of this block

        @keyparam name=None name of new method
        @return Class instance
        """
        from java2python.blocks import Class
        c = Class(parent=self, name=name)
        self.addSource(c)
        return c

    def makeForEach(self):
        from java2python.blocks import Statement
        s = BasicBlock(self)
        f = Statement(self, 'for')
        self.addSource(s)
        self.addSource(f)
        return s, f

    def makeFor(self):
        """ creates a new 'for' Statement as a child of this block

        @return two-tuple of initializer Statement and block Statement
        """
        from java2python.blocks import Statement
        s = BasicBlock(self)
        f = Statement(self, 'while')
        self.addSource(s)
        self.addSource(f)
        return s, f

    def makeIf(self, ):
        from java2python.blocks import Statement
        f = Statement(self, 'if')
        e = Statement(self, 'else')
        #b, ba = BasicBlock(self), BasicBlock(self)
        self.addSource(f)
        self.addSource(e)
        #self.addSource(b)
        #self.addSource(ba)
        #return b, ba, f, e
        return f, e

    def makeMethod(self, name=None):
        """ creates a new Method object as a child of this block

        @keyparam name=None name of new method
        @return Method instance
        """
        from java2python.blocks import Method
        m = Method(parent=self, name=name)
        self.addMethod(m)
        self.addSource(m)
        return m

    def makeSwitch(self):
        """ creates a new 'if' Statement as a child of this block

        @return Statement instance
        """
        from java2python.blocks import Statement
        while_stat = Statement(self, 'while')
        while_stat.setExpression('True')
        self.addSource(while_stat)
        return while_stat

    def makeStatement(self, name):
        """ creates a new Statement as a child of this block

        @param name name of statement
        @return Statement instance
        """
        from java2python.blocks import Statement
        s = Statement(parent=self, name=name)
        self.addSource(s)
        return s

    def makeStatementBefore(self, name, stat=None):
        """ creates a new Statement as a child of this block before the last
        or the specified statement.

        @param name name of statement
        @param stat add statement before this one
        @return Statement instance
        """
        from java2python.blocks import Statement
        s = Statement(parent=self, name=name)
        self.addSource(s, index=stat)
        return s


class BasicBlock(BlockAddingShard, BlockMakerShard, BlockPropShard, ):
    """ BasicBlock -> base class for source code types.

    Instances have methods to create new child instances, e.g., makeClass
    to create a new class.

    This class contains some attributes only used by subclasses; their
    creation in this base type is strictly from laziness.

    """
    classmethodLiteral, staticmethodLiteral = '@classmethod', '@staticmethod'
    config = None
    isClass = isMethod = isVariable = False

    def __init__(self, parent=None, name=None):
        self.parent = parent
        self.name = name
        self.bases = []
        self.modifiers = []
        self.preamble = []
        self.epilogue = []
        self.lines = []
        self.type = None
        self.variables = []
        self.methods = []
        self.extraVars = []

    def __iter__(self):
        for line in self.lines:
            yield line

    def index(self, value):
        return self.lines.index(value)

    def setConfigs(self, configs):
        ## always place it on the root class so all instances of all
        ## BasicBlock types get the same object.  also means any instance
        ## of any BasicBlock type can set the config for all other
        ## instances of all BasicBlock types.  dr. seuss would have loved
        ## oop and its goop.
        BasicBlock.config = Config(configs)

    def I(self, indent):
        """ calculated indentation string

        @param indent integer indentation level
        @return string of spaces
        """
        return (' ' * self.config.last('indent', 4)) * indent

    def asString(self):
        """ asString() -> source code defined in obj

        """
        out = StringIO()
        self.dump(out, 0)
        source = out.getvalue()
        for subs in self.config.all('outputSubs', []):
            for sub in subs:
                source = rxsub(sub[0], sub[1], source)
        return source

    ## Big problem: dump is not idempotent, children do far too many
    ## state changes.  should invoke config-handlers at some other
    ## point, e.g., block complete.

    def dump(self, output, indent):
        """ Serialize this object to stream output.

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        offset = self.I(indent)
        for line in self:
            if isinstance(line, (tuple, dict)):
                line = self.formatExpression(line)
            if hasattr(line, 'dump'):
                line.dump(output, indent)
            elif line:
                output.write('%s%s\n' % (offset, line))

    def dumpConfigValues(self, output, name):
        """ writes a sequence of lines given a config attribute name

        Lines may be callable.  Refer to the config.default module for
        details.

        @param output writable file-like object
        @param name configuration module attribute
        @return None
        """
        for lines in self.config.all(name, []):
            for line in lines:
                line = line(self) if callable(line) else line
                output.write('%s\n' % (line, ))

    # Here are the dragons.  They are crisp and dreadful.  I wish they
    # were gone.

    @property
    def declFormat(self):
        """ string format for variable names in this block

        """
        # seriously, wtf.
        for parent in self.family:
            if parent.isMethod:
                preamble = parent.preamble
                if self.staticmethodLiteral in preamble:
                    return '%s'
                elif self.classmethodLiteral in preamble:
                    return '%s'
                else:
                    return 'self.%s'
        return '%s ## ERROR'

    def formatExpression(self, obj):
        """ format an expression set by the tree walker

        Expressions are either strings or nested two-tuples of
        format strings and their arguments.

        @param obj string or two-tuple
        @return interpolated, fixed expression as string
        """
        if isinstance(obj, list):
            ## still used????
            debug('formatting list object %s', obj)
            expr = ', '.join(self.formatExpression(v) for v in obj)
        elif isinstance(obj, dict):
            inner = obj.copy()
            format = inner['format']
            if 'right' in obj:
                inner['right'] = self.formatExpression(obj['right'])
            if 'left' in obj:
                inner['left'] = self.formatExpression(obj['left'])
            expr = Template(format).substitute(inner)
        else:
            expr = obj
        return expr
