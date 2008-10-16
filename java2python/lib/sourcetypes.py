#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.lib.sourcetypes -> classes for building python source code.

When used by java2python.lib.walker, the Module class below is updated
as the java AST is walked.  Refer to the java2python script for usage.

"""
from cStringIO import StringIO
import re


def import_name(name):
    """ import_name(name) -> import and return a module by name in dotted form

    Copied from the Python lib docs.

    @param name module or package name in dotted form
    @return module object
    """
    mod = __import__(name)
    for comp in name.split('.')[1:]:
        mod = getattr(mod, comp)
    return mod


def set_config(names, includeDefault=True):
    """ build and set a Config object on the Source class

    @param names sequence of module names
    @keyparam includeDefault=True flag to include default configuration module
    @return None
    """
    if includeDefault:
        names.insert(0, 'java2python.lib.defaultconfig')
    Source.config = Config(*names)


class Config:
    """ Config -> wraps multiple configuration modules


    """
    def __init__(self, *names):
        self.configs = [import_name(name) for name in names]

    def all(self, name, missing=None):
        """ value of name in each config module

        @param name module attribute as string
        @keyparam missing=None default for missing attributes
        @return list of values
        """
        return (getattr(config, name, missing) for config in self.configs)

    def last(self, name, default=None):
        """ value from final config module to define name

        @param name module attribute as string
        @keyparam default=None value returned if all modules lack name
        @return value from config module
        """
        for config in reversed(self.configs):
            if hasattr(config, name):
                return getattr(config, name)
        return default

    def combined(self, name):
        """ combined mapping of named dictionaries from all config modules

        @param dictionary attribute as string
        @return dictionary updated with each named dictionary
        """
        combined = {}
        for mapping in self.all(name, {}):
            combined.update(mapping)
        return combined


class Source:
    """ Source -> base class for source code types.

    Instances have methods to create new child instances, e.g., newClass
    to create a new class.

    This class contains some attributes only used by subclasses; their
    creation in this base type is strictly from laziness.

    """
    emptyAssign = ('%s', '<empty>')
    missingValue = ('%s', '<missing>')
    unknownExpression = ('%s', '<unknown>')
    config = Config()
    staticmethodLiteral = '@staticmethod'
    classmethodLiteral = '@classmethod'
    anonymousClassCount = 0

    def __init__(self, parent=None, name=None):
        self.parent = parent
        self.name = name
        self.bases = []
        self.annotations = []
        self.modifiers = []
        self.preamble = []
        self.epilogue = []
        self.lines = []
        self.type = None
        self.variables = list()
        self.methods = list()

        self.postIncDecInExprFixed = False
        self.postIncDecVars = []
        self.postIncDecCount= 0 

    def __str__(self):
        """ str(obj) -> source code defined in obj

        """
        out = StringIO()
        self.writeTo(out, 0)
        source = out.getvalue()
        for subs in self.config.all('outputSubs', []):
            for sub in subs:
                source = re.sub(sub[0], sub[1], source)
        return source

    def writeTo(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        offset = self.I(indent)
        for line in self.lines:
            if isinstance(line, tuple):
                line = self.formatExpression(line)
            try:
                line.writeTo(output, indent)
            except (AttributeError, ):
                output.write('%s%s\n' % (offset, line))

    def addComment(self, text, prefix='##'):
        """ add a comment to this source block

        @param text value of comment
        @keyparam prefix='##' value of comment prefix
        @return None
        """
        prefix = self.config.last('commentPrefix', prefix)
        self.addSource('%s %s' % (prefix, text))

    def addAnnotation(self, name):
        self.annotations.append('@' + name)

    def addModifier(self, name):
        """ add a modifier to this source block

        @param name value of modifier, as a string
        @return None
        """
        self.modifiers.append(name)

    def addSource(self, value):
        """ add source code to the end of this block

        @param value string, instance of Source (or subclass), or two-tuple
        @return None
        """
        self.lines.append(value)

    def addSourceBefore(self, value, stat=None):
        """ add source code to the end of this block, before the last line
        or the specified statement

        @param value string, instance of Source (or subclass), or two-tuple
        @param stat Statement, insert source before this statement
        @return None
        """
        if len(self.lines) > 0:
            if isinstance(stat, int):
                idx = stat
            else:
                idx = 0 if stat == None else self.lines.index(stat)
            self.lines.insert(idx, value)
        else:
            self.lines.append(value)

    def addVariable(self, var, force=False):
        """ add variable name to set for tracking

        Variables are only added to Class instances unless the force
        parameter True.

        @param name variable as string
        @keyparam force=False, if True, always add to set
        @return None
        """
        if force or (var.name and self.isClass):
            self.variables.append(var)

    def addMethod(self, meth):
        self.methods.append(meth)

    @property
    def allParents(self):
        """ generator to provide each ancestor of this instance

        @return yields individual ancestors of this instance one at a time
        """
        previous = self.parent
        while previous:
            yield previous
            previous = previous.parent

    @property
    def allVars(self):
        """ all variables in this instance and its ancestors

        @return yields variable names from this instance and all ancestors
        """
        for obj in [self, ] + list(self.allParents):
            for v in obj.variables:
                yield v.name
            for v in obj.methods:
                yield v.name
            for v in obj.extraVars:
                yield v

    @property
    def methodVars(self):
        """ all vars declared in the current method

        @return yeilds all vars declared in the method
        """

        for obj in [self, ] + list(self.allParents):
            for v in obj.variables:
                yield v.name
            if isinstance(obj, Method): break

    @property
    def instanceMembers(self):
        """ all instance members in this class

        @return yields all instance member names from this class
        """
        for obj in [self, ] + list(self.allParents):
            if isinstance(obj, Class):
                for v in obj.variables:
                    if not v.isStatic:
                        yield v.name
                for v in obj.extraVars:
                    yield v

    @property
    def instanceMethods(self):
        """ all instance methods in this class

        @return yields all instance method names from this class
        """
        for obj in [self, ] + list(self.allParents):
            if isinstance(obj, Class):
                for v in obj.methods:
                    if not v.isStatic:
                        yield v.name

    @property
    def staticMembers(self):
        """ all static members in this class

        @return yields static member names from this class
        """
        for obj in [self, ] + list(self.allParents):
            if isinstance(obj, Class):
                for v in obj.variables:
                    if v.isStatic:
                        yield v.name

    @property
    def staticMethods(self):
        """ all static methods in this class

        @return yields static method names from this class
        """
        for obj in [self, ] + list(self.allParents):
            if isinstance(obj, Class):
                for v in obj.methods:
                    if v.isStatic:
                        yield v.name

    @property
    def extraVars(self):
        """ extra variable names; subclasses can and should reimplement

        @return sequence of variable names
        """
        return []

    @property
    def blockMethods(self):
        """ all source objects that are methods

        @return generator expression with all methods in this block
        """
        return (m for m in self.lines if getattr(m, 'isMethod', False))

    def insertSource(self, index, value):
        """ insert object before index

        @param index location at which to insert
        @param value object or string to insert
        @return None
        """
        self.lines.insert(index, value)

    @property
    def isClass(self):
        """ True if this instance is a Class

        """
        return isinstance(self, Class)

    @property
    def isMethod(self):
        """ True if this instance is a Method

        """
        return isinstance(self, Method)

    @property
    def isStatic(self):
        """ True if this instance is static

        @return if the variable is static return True
        """
        return 'static' in self.modifiers

    @property
    def declFormat(self):
        """ string format for variable names in this block

        """
        for parent in [self, ] + list(self.allParents):
            if parent.isMethod:
                preamble = parent.preamble
                if self.classmethodLiteral in preamble:
                    return 'cls.%s'
                elif self.staticmethodLiteral in preamble:
                    return '%s'
                else:
                    return 'self.%s'
        return '%s ## ERROR'

    @property
    def className(self):
        """ Return className of the source in.

        """
        if isinstance(self, Class):
            return self.name
        elif self.parent is not None:
            return self.parent.className
        else:
            return 'ERROR'

    def fixDecl(self, *args):
        """ fixes variable names that are class members

        @varparam args names to fix
        @return fixed name or names
        """
        fixed = list(args)
        methodvars = list(self.methodVars)
        membervars = list(self.instanceMembers) + list(self.instanceMethods)
        staticvars = list(self.staticMembers) + list(self.staticMethods)
        mapping = self.config.combined('variableNameMapping')
        format = self.declFormat
        for i, arg in enumerate(args):
            if arg in methodvars:
                arg = mapping.get(arg, arg)
                fixed[i] = arg
            elif arg in staticvars:
                arg = mapping.get(arg, arg)
                fixed[i] = "%s.%s" % (self.className, arg)
            elif arg in membervars:
                arg = mapping.get(arg, arg)
                fixed[i] = format % (arg, )
            else:
                fixed[i] = mapping.get(arg, arg)
        if len(fixed) == 1:
            return fixed[0]
        else:
            return tuple(fixed)

    def newClass(self, name=None):
        """ creates a new Class object as a child of this block

        @keyparam name=None name of new method
        @return Class instance
        """
        c = Class(parent=self, name=name)
        self.addSource(c)
        return c

    def newFor(self):
        """ creates a new 'for' Statement as a child of this block

        @return two-tuple of initializer Statement and block Statement
        """
        s = Source(self)
        f = Statement(self, 'while')
        self.addSource(s)
        self.addSource(f)
        return s, f

    def newMethod(self, name=None):
        """ creates a new Method object as a child of this block

        @keyparam name=None name of new method
        @return Method instance
        """
        m = Method(parent=self, name=name)
        self.addMethod(m)
        self.addSource(m)
        return m

    def newSwitch(self):
        """ creates a new 'if' Statement as a child of this block

        @return Statement instance
        """
        while_stat = Statement(self, 'while')
        while_stat.setExpression('True')
        self.addSource(while_stat)
        return while_stat

    def newStatement(self, name):
        """ creates a new Statement as a child of this block

        @param name name of statement
        @return Statement instance
        """
        s = Statement(parent=self, name=name)
        self.addSource(s)
        return s

    def newStatementBefore(self, name, stat=None):
        """ creates a new Statement as a child of this block before the last
        or the specified statement.

        @param name name of statement
        @param stat add statement before this one
        @return Statement instance
        """
        s = Statement(parent=self, name=name)
        self.addSourceBefore(s, stat)
        return s

    def removeStatement(self, stat):
        """ remove a statement from source.

        @param stat Statement to be removed.
        @return None
        """
        idx = self.lines.index(stat)
        del self.lines[idx]

    def newVariable(self, name=None):
        """ creates a new Variable for the block
        
        @param name name of the variable
        @return Variable instance
        """
        var = Variable(self)
        self.addVariable(var, True)
        return var

    def formatExpression(self, expr):
        """ format an expression set by the tree walker

        Expressions are either strings or nested two-tuples of
        format strings and their arguments.

        @param expr string or two-tuple
        @return interpolated, fixed expression as string
        """
        fixdecl = self.fixDecl

        if isinstance(expr, basestring):
            return fixdecl(expr)

        format = self.formatExpression
        first, second = expr
        if isinstance(first, basestring) and isinstance(second, basestring):
            return fixdecl(first) % fixdecl(second)
        elif isinstance(first, basestring) and isinstance(second, tuple):
            return fixdecl(first) % format(second)
        elif isinstance(first, tuple) and isinstance(second, basestring):
            return format(first) % fixdecl(second)
        elif isinstance(first, tuple) and isinstance(second, tuple):
            return (format(first), format(second))
        else:
            raise NotImplementedError('Unhandled expression type:  %s' % expr)

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

    def setName(self, name):
        """ sets the name of this block

        @param name any string
        @return None
        """
        self.name = name

    def trimLines(self):
        """ removes empty lines from the end of this block

        @return None
        """
        lines = self.lines
        if lines:
            while not lines[-1]:
                lines.pop()

    def I(self, indent):
        """ calculated indentation string

        @param indent integer indentation level
        @return string of spaces
        """
        return (' ' * self.config.last('indent', 4)) * indent

    def fixAssignInExpr(self, needFix, expr, left):
        if not needFix: return expr
        if self.name == 'if':
            self.parent.addSourceBefore(expr, self)
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
                self.parent.addSourceBefore((var[0] + ' = %s', var[1]), self)
            for var in self.postIncDecVars:
                self.parent.addSourceBefore(('%s ' + var[2] + '= 1', var[1]), self)
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

class Module(Source):
    """ Module -> specialized block type

    Module instances write a preamble before writing their source
    objects.
    """
    def __init__(self, infile, outfile):
        Source.__init__(self, parent=None, name=None)
        self.infile = infile
        self.outfile = outfile

    def writeTo(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        self.writeExtraLines('modulePreamble', output)
        output.write('\n')
        Source.writeTo(self, output, indent)
        self.writeExtraLines('moduleEpilogue', output)
        if self.config.last('writeMainMethodScript'):
            self.writeMainBlock(output)

    def writeExtraLines(self, name, output):
        """ writes a sequence of lines given a config attribute name

        Lines may be callable.  Refer to the defaultconfig module for
        details.

        @param name configuration module attribute
        @param output writable file-like object
        @return None
        """
        for lines in self.config.all(name, []):
            for line in lines:
                try:
                    line = line(self)
                except (TypeError, ):
                    pass
                output.write('%s\n' % (line, ))

    def writeMainBlock(self, output):
        """ writes a block to call the module as a script

        @param output writable file-like object
        @return None
        """
        try:
            cls = [c for c in self.lines if getattr(c, 'isClass', None)][0]
            methods = [m for m in cls.lines if getattr(m, 'isMethod', None)]
            main = [m for m in methods if m.name == 'main'][0]
        except (Exception, ):
            pass
        else:
            mods = main.modifiers
            typ = main.type
            if ('public' in mods) and ('static' in mods) and (typ == 'void'):
                name = cls.name
                offset = self.I(1)
                output.write("if __name__ == '__main__':\n")
                output.write("%simport sys\n" % offset)
                output.write("%s%s.main(sys.argv)\n" % (offset, name))


class Class(Source):
    """ Class -> specialized block type

    """
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
            name = self.formatExpression(name)
            self.bases.append(name)

    def fixDecl(self, *args):
        """ fixes variable names that are class members

        @varparam args names to fix
        @return fixed name or names
        """
        ret = list(args)
        for i, arg in enumerate(args):
            if self.className != arg:
                ret[i] = Source.fixDecl(self, arg)
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
            self.insertSource(0, c)
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
        mapping = [(m.name, len(m.parameters)) for m in self.blockMethods]
        propmap = {}

        for meth in self.blockMethods:
            name = meth.name
            if (name, 1) in mapping and (name, 2) in mapping:
                argc = len(meth.parameters)
                methmap = propmap.setdefault(name, {1:None, 2:None})
                methmap[argc] = meth
                meth.name = ('get_%s' if argc==1 else 'set_%s') % name
        lines = self.lines
        for name, meths in propmap.items():
            lines.remove(meths[1])
            lines.remove(meths[2])
        self.trimLines()
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
                    meth.addSourceBefore("super(%s, self).__init__()" % meth.className, 0)
                    meth.stmtAfterSuper = meth.newStatementBefore("if", 1)

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
                    

    def writeTo(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        config = self.config
        if config.last('fixPropMethods'):
            self.fixPropMethods()

        if config.last('fixOverloadMethods'):
            self.fixOverloadMethods()

        if config.last('sortClassMethods'):
            def methodsorter(x, y):
                if getattr(x, 'isMethod', False) and \
                       getattr(y, 'isMethod', False):
                    return cmp(x.name, y.name)
                return 0
            self.lines.sort(methodsorter)
        name = self.name
        offset = self.I(indent+1)
        output.write('%s%s\n' % (self.I(indent), self.formatDecl()))
        if config.last('writeClassDocString'):
            output.write('%s""" generated source for %s\n\n' % (offset, name))
            output.write('%s"""\n' % (offset, ))
        Source.writeTo(self, output, indent+1)


class Method(Source):
    """ Method -> specialized block type

    """
    instanceFirstParam = ('object', 'self')
    classFirstParam = ('type', 'cls')

    def __init__(self, parent, name):
        Source.__init__(self, parent=parent, name=name)
        self.parameters = [self.instanceFirstParam, ]

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
                self.preamble.append(deco)
                if (deco == self.classmethodLiteral) and (self.parameters) \
                       and (self.parameters[0] == self.instanceFirstParam):
                    self.parameters[0] = self.classFirstParam
        Source.addModifier(self, name)

    def addParameter(self, typ, name):
        """ adds named parameter to method

        @param typ parameter type as string
        @param name parameter name as string
        @return None
        """
        name = self.alternateName(name)
        typ = Source.alternateName(self, typ, 'typeTypeMap')
        self.parameters.append((typ, name))
        self.variables.append(Variable(self, name))

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
            return Source.alternateName(self, name)

    def writeTo(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        offset = self.I(indent)
        output.write('\n')


        for anno in self.annotations:
            output.write('%s%s\n' % (offset, anno))

        if self.config.last('writeModifiersComments'):
            output.write('%s## modifiers: %s\n' % (offset, str.join(',', self.modifiers)))

        sorter = self.config.last('methodPreambleSorter')
        if sorter:
            self.preamble.sort(sorter)
        for obj in self.preamble:
            output.write('%s%s\n' % (offset, obj))
        output.write('%s\n' % (self.formatDecl(indent), ))

        writedoc = self.config.last('writeMethodDocString')
        if writedoc:
            docoffset = self.I(indent+1)
            output.write('%s""" generated source for %s\n\n' % \
                         (docoffset, self.name))
            output.write('%s"""\n' % (docoffset, ))
        if (not self.lines) and (not writedoc):
            self.addSource('pass')
        self.trimLines()
        Source.writeTo(self, output, indent+1)
        try:
            next = self.parent.lines[1+self.parent.lines.index(self)]
            addline = not next.isMethod
        except (IndexError, AttributeError, ):
            addline = True
        if addline:
            output.write('\n')


class Statement(Source):
    """ Statement -> specialized block type

    Unlike Source instances, Statement instances have expressions.  These
    expressions are evaluated before they're output.
    """
    def __init__(self, parent, name=None, expr=None):
        Source.__init__(self, parent=parent, name=name)
        self.expr = expr

    @property
    def isBadLabel(self):
        """ True if instance is a break or continue statement outside
        of a while or for loop.

        """
        if self.name in ('break', 'continue'):
            parent_names = [p.name for p in self.allParents]
            if 'while' not in parent_names and 'for' not in parent_names:
                return True

    @property
    def isNoOp(self):
        """ True if instance does nothing

        """
        return self.name in ('else', 'finally') and (not self.lines)

    @property
    def needsBlockIndicator(self):
        """ True if instance needs a colon written after its expression

        """
        return self.name in ('if', 'while', 'for', 'else', 'elif',
                             'try', 'except', 'finally')

    def setExpression(self, value):
        """ sets the value of the expression for this Statement

        @param value expression (see formatExpression in Source class).
        @return None
        """
        self.expr = value

    def writeTo(self, output, indent):
        """ writes the string representation of this block

        @param output any writable file-like object
        @param indent indentation level of this block
        @return None
        """
        name = self.name
        parents = self.allParents
        lines = self.lines

        if self.isBadLabel or self.isNoOp:
            return

        offset = self.I(indent)
        output.write('%s%s' % (offset, name))
        if self.expr is not None:
            expr = self.formatExpression(self.expr)
            output.write(' %s' % (expr, ))
        if self.needsBlockIndicator:
            output.write(':')
        output.write('\n')
        if (not lines) and name not in ('break', 'continue', 'raise'):
            self.addSource('pass')
        Source.writeTo(self, output, indent+1)

class Variable(Source):
    """Variable is a defined class member variable or auto variable of the
    method.

    """

    def __init__(self, parent, name=None, expr=None):
        Source.__init__(self, parent=parent, name=name)
        self.expr = expr

    def setExpression(self, expr):
        """ sets the value of the expression for this Variable

        @param value expression (see formatExpression in Source class).
        @return None
        """
        self.expr = expr

