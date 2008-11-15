#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.blocks.base -> basic building block of output source code.

"""
from cStringIO import StringIO
from itertools import chain
from logging import debug, warn, exception
from re import sub as rxsub
from string import Template

from java2python import maybeattr
from java2python.config import Config


class BlockPropShard:
    @property
    def blockMethods(self):
        """ all source objects that are methods """
        return (m for m in self.lines if maybeattr(m, 'isMethod'))

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


class BlockAddingShard:
    # The next set of functions are for configuring and filling the
    # block.

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
        if lines == ['pass']:
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
        if isinstance(obj, Variable):
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
    ## anonymousClassCount = 0 # what did this provide?
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
        self.prefix = []
        self.type = None
        self.variables = []
        self.methods = []
        self.extraVars = []

    def __iter__(self):
        for line in self.lines:
            yield line

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

    def fixDecl(self, *args):
        """ fixes variable names that are class members

        @varparam args names to fix
        @return fixed name or names
        """
        fixed = list(args)
        methodvars = list(self.methodVars)
        membervars = list(chain(self.instanceMembers, self.instanceMethods))
        staticvars = list(chain(self.staticMembers, self.staticMethods))
        mapping = self.config.combined('identRenames')
        format = self.declFormat
        for i, arg in enumerate(args):
            if arg in methodvars:
                arg = mapping.get(arg, arg)
                fixed[i] = arg
            elif arg in staticvars:
                arg = mapping.get(arg, arg)
                fixed[i] = "%s.%s" % (self.nameOrClassName, arg)
            elif arg in membervars:
                arg = mapping.get(arg, arg)
                fixed[i] = format % (arg, )
            else:
                fixed[i] = mapping.get(arg, arg)
        if len(fixed) == 1:
            return fixed[0]
        else:
            return tuple(fixed)

    def formatExpression(self, obj):
        """ format an expression set by the tree walker

        Expressions are either strings or nested two-tuples of
        format strings and their arguments.

        @param obj string or two-tuple
        @return interpolated, fixed expression as string
        """
        if isinstance(obj, tuple):
            raise Exception(str(obj))
            expr = str(obj)
        elif isinstance(obj, list):
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
            #renames = self.config.combined('identRenames')
            #expr = renames.get(obj, obj)
            expr = obj
        return expr

    def alternateName(self, name, key='renameAnyMap'):
        """ returns an alternate for given name

        @param name any string
        @return alternate for name if found; if not found, returns name
        """
        mapping = self.config.combined(key)
        try:
            return mapping[name]
        except (KeyError, ):
            return name


class CruftiesFromPreviousImplementation:
    def init():
        ## ug.
        self.postIncDecInExprFixed = False
        self.postIncDecVars = []
        self.postIncDecCount= 0



    def fixAssignInExpr(self, needFix, expr, left):
        if not needFix: return expr
        if self.name == 'if':
            self.parent.addSource(expr, self)
        elif self.name == 'while':
            self.addSource(expr)
        elif isinstance(self, Method):
            self.addSource(expr)
        return left

    def fixPostIncDecInExpr(self, needFix, expr, left, op):
        if not needFix: return expr
        if self.name == 'if':
            avar = "_%s0" % left[1]
            self.postIncDecVars.append((avar, left, op))
            self.postIncDecInExprFixed = True
            return '%s', avar
        else:
            self.postIncDecVars.append((left, op))
            self.postIncDecInExprFixed = True
            return '%s', left

    def fixPostIncDecInExprAfter(self, expr):
        if not self.postIncDecInExprFixed: return expr
        if self.name == 'if':
            for var in self.postIncDecVars:
                self.parent.addSource((var[0] + ' = %s', var[1]), self)
            for var in self.postIncDecVars:
                self.parent.addSource(('%s ' + var[2] + '= 1', var[1]), self)
        else:
            for var in self.postIncDecVars:
                left, op = var
                self.addSource(('%s ' + op + "= 1", left))
        self.postIncDecVars = []
        self.postIncDecInExprFixed = False
        return expr

    def hasAssignInExpr(self, expr):
        from lexer import ASSIGN, INC, DEC, POST_INC, POST_DEC, BAND_ASSIGN, SL_ASSIGN, BSR_ASSIGN, SR_ASSIGN, MOD_ASSIGN, DIV_ASSIGN, STAR_ASSIGN, MINUS_ASSIGN, PLUS_ASSIGN
        if expr.getType() in (ASSIGN, INC, DEC, POST_INC, POST_DEC, BAND_ASSIGN, SL_ASSIGN, BSR_ASSIGN, SR_ASSIGN, MOD_ASSIGN, DIV_ASSIGN, STAR_ASSIGN, MINUS_ASSIGN, PLUS_ASSIGN):
            return True
        child = expr.getFirstChild()
        while child:
            ret = self.hasAssignInExpr(child)
            if ret: return True
            child = child.getNextSibling()
        return False

    def allVars(self):
        """ all variables in this instance and its ancestors """
        for obj in self.family:
            for v in obj.variables:
                yield v.name
            for v in obj.methods:
                yield v.name
            for v in obj.extraVars:
                yield v


    def old_formatExpression(self, v):
        fixdecl = self.fixDecl
        fixdecl = lambda x:x
        if isinstance(expr, basestring):
            return expr # fixdecl(expr)
        format = self.formatExpression
        first, second = expr
        debug("%s::%s %s::%s", type(first).__name__, first, type(second).__name__, second, )
        try:
            if isinstance(first, basestring) and isinstance(second, basestring):
                debug("str+str")
                return first % second
                #return fixdecl(first) % fixdecl(second)
            elif isinstance(first, basestring) and isinstance(second, tuple):
                debug("str+tuple")
                return first % format(second)
                return fixdecl(first) % format(second)
            elif isinstance(first, tuple) and isinstance(second, basestring):
                debug("tuple+str")
                return format(first) % fixdecl(second)
            elif isinstance(first, tuple) and isinstance(second, tuple):
                debug("tuple+tuple")
                return (format(first), format(second))
            else:
                #return str(expr)
                raise NotImplementedError('Unhandled expression type:  %s' % expr)
        except (Exception, ):
            exception("unhandled expression %s %s", first, second)
