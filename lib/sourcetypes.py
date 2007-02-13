#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" java2python.lib.sourcetypes -> classes for building python source code.

When used by java2python.lib.walker, the Module class below is updated
as the java AST is walked.  Refer to the java2python script for usage.


TODO:
    replace 'if False:pass' statements with equivelents.
    add substitution for 'foo == None'
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
    
    def __init__(self, parent=None, name=None):
        self.parent = parent
        self.name = name
        self.bases = []
        self.modifiers = set()
        self.preable = []
        self.lines = []        
        self.type = None
        self.variables = set()
        
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
    
    def addComment(self, text, prefix='##'):
        """ add a comment to this source block

        @param text value of comment
        @keyparam prefix='##' value of comment prefix
        @return None
        """
        prefix = self.config.last('commentPrefix', prefix)
        self.addSource('%s %s' % (prefix, text))

    def addModifier(self, name):
        """ add a modifer to this source block

        @param name value of modifier, as a string
        @return None
        """
        self.modifiers.add(name)

    def addSource(self, value):
        """ add source code to the end of this block

        @param value string, instance of Source (or subclass), or two-tuple
        @return None
        """
        self.lines.append(value)

    def addVariable(self, name, force=False):
        """ add variable name to set for tracking

        Variables are only added to Class instances unless the force
        parameter True.
        
        @param name variable as string
        @keyparam force=False, if True, always add to set
        @return None
        """
        if force or (name and self.isClass):
            self.variables.add(name)

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
        """ provides all variables in this instance and its ancestors

        @return yields variable names from this instance and all ancestors
        """
        for parent in self.allParents:
            for v in parent.variables:
                yield v

    @property
    def blockMethods(self):
        return (m for m in self.lines if getattr(m, 'isMethod', False))

    def insertSource(self, index, value):
        self.lines.insert(index, value)
        
    @property
    def isClass(self):
        return self.__class__ is Class

    @property
    def isMethod(self):
        return self.__class__ is Method

    def fixDecl(self, *args):
        fixed = list(args)
        for i, arg in enumerate(args):
            if arg in self.allVars:
                fixed[i] = "self.%s" % (arg, )
        if len(fixed) == 1:
            return fixed[0]
        else:
            return tuple(fixed)

    def newClass(self):
        c = Class(parent=self, name=None)
        self.addSource(c)
        return c

    def newFor(self):
        s = Source(self)
        f = Statement(self, 'while')
        self.addSource(s)
        self.addSource(f)
        return s, f
    
    def newMethod(self, name=None):
        m = Method(parent=self, name=name)
        self.addSource(m)
        return m

    def newSwitch(self):
        s = Statement(self, 'if')
        s.expr = 'False'
        self.addSource(s)
        return s
    
    def newStatement(self, name):
        s = Statement(parent=self, name=name)
        self.addSource(s)
        return s

    def formatExpression(self, s):
        if isinstance(s, basestring):
            return self.fixDecl(s)
        if isinstance(s[0], basestring) and isinstance(s[1], basestring):
            return self.fixDecl(s[0]) % self.fixDecl(s[1])
        if isinstance(s[0], basestring) and isinstance(s[1], tuple):
            return self.fixDecl(s[0]) % self.formatExpression(s[1])
        if isinstance(s[0], tuple) and isinstance(s[1], basestring):
            return self.formatExpression(s[0]) % self.formatExpression(s[1])
        if isinstance(s[0], tuple) and isinstance(s[1], tuple):
            return (self.formatExpression(s[0]), self.formatExpression(s[1]))

    def alternateName(self, value):
        mapping = self.config.combined('renameAnyMap')
        try:
            return mapping[value]
        except (KeyError, ):
            return value

    def setName(self, name):
        self.name = name
        
    def writeTo(self, output, indent):
        offset = self.I * indent
        for line in self.lines:
            if isinstance(line, tuple):
                line = self.formatExpression(line)
            try:
                line.writeTo(output, indent)
            except (AttributeError, ):
                output.write('%s%s\n' % (offset, line))
    @property
    def I(self):
        return ' ' * self.config.last('indent', 4)


class Module(Source):
    def __init__(self, infile, outfile):
        Source.__init__(self, parent=None, name=None)
        self.infile = infile
        self.outfile = outfile

    def writeTo(self, output, indent):
        for preables in self.config.all('modulePreable', []):
            for line in preables:
                try:
                    line = line(self)
                except (TypeError, ):
                    pass
                output.write('%s\n' % (line, ))
        output.write('\n')
        Source.writeTo(self, output, indent)


class Class(Source):
    def addBaseClass(self, clause):
        if clause and (clause not in self.bases):
            ## in case java ever grows MI... (giggle)
            self.bases.append(clause) 

    def formatDecl(self):
        bases = self.bases or ['object', ]
        bases = str.join(', ', bases)
        return 'class %s(%s):' % (self.name, bases)

    def newClass(self):
        c = Class(parent=self, name=None)
        ## move inner classes to the top; allows for referencing
        ## later in this class definition.
        if self.config.last('bubbleInnerClasses'):
            self.insertSource(0, c)
        else:
            self.addSource(c)
        return c

    def scanPropMethods(self):
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

        if lines:
            while not lines[-1]:
                lines.pop()

        format = '%s = property(%s, %s)'                
        for name, meths in propmap.items():
            lines.append(meths[1])
            lines.append(meths[2])            
            lines.append(format % (name, meths[1].name, meths[2].name))
            
    def scanOverloadMethods(self):
        overloads = {}

        for method in self.blockMethods:
            name = method.name
            overloads[name] = 1 + overloads.setdefault(name, 0)

        for name in [n for n, c in overloads.items() if c>1]:
            renames = [m for m in self.blockMethods if m.name == name]
            first, remainder = renames[0], renames[1:]
            first.preable.append('@overloaded')
            firstname = first.name

            for index, method in enumerate(remainder):
                params = str.join(', ', [p[0] for p in method.parameters])
                method.preable.append('@%s.register(%s)' % (firstname, params))
                method.name = '%s_%s' % (method.name, index)

    def writeTo(self, output, indent):
        config = self.config
        if config.last('scanPropMethods'):
            self.scanPropMethods()
        if config.last('scanOverloadMethods'):
            self.scanOverloadMethods()
        if config.last('sortClassMethods'):
            def methodsorter(x, y):
                if getattr(x, 'isMethod', False) and \
                       getattr(y, 'isMethod', False):
                    return cmp(x.name, y.name)
                return 0
            self.lines.sort(methodsorter)
            
        name = self.name
        offset = self.I * (indent+1)
        output.write('%s%s\n' % (self.I * indent, self.formatDecl()))
        if config.last('writeClassDocString'):
            output.write('%s""" generated source for %s\n\n' % (offset, name))
            output.write('%s"""\n' % (offset, ))
        Source.writeTo(self, output, indent+1)
        output.write('\n')


class Method(Source):
    def __init__(self, parent, name):
        Source.__init__(self, parent=parent, name=name)
        self.parameters = [('object', 'self'), ]

    def addModifier(self, mod):
        try:
            mod = self.config.combined("modifierDecoratorMap")[mod]
        except (KeyError, ):
            Source.addModifier(self, mod)
        else:
            if mod not in self.preable:
                self.preable.append(mod)

    def addParameter(self, typ, name):
        name = self.alternateName(name)
        self.parameters.append((typ, name))

    def formatDecl(self, indent):
        name = self.alternateName(self.name)
        parameters = self.parameters
        if len(parameters) > 5:
            first, others = parameters[0], parameters[1:]            
            prefix = '%sdef %s(%s, ' % (self.I * indent, name, first[1], )
            offset = '\n' + (' ' * len(prefix))
            decl = '%s%s):' % (prefix, str.join(', '+offset, [o[1] for o in others]))
        else:
            params = str.join(', ', [p[1] for p in parameters])
            decl = '%sdef %s(%s):' % (self.I * indent, name, params)
        return decl

    def alternateName(self, value):
        mapping = self.config.combined('renameMethodMap')
        try:
            return mapping[value]
        except (KeyError, ):
            return value

    def writeTo(self, output, indent):
        offset = self.I * indent
        output.write('\n')
        if self.config.last('writeModifiersComments'):
            output.write('%s## modifiers: %s\n' % (offset, str.join(',', self.modifiers)))
        for obj in self.preable:
            output.write('%s%s\n' % (offset, obj))
        output.write('%s\n' % (self.formatDecl(indent), ))
        if not self.lines:
            self.addSource('pass')
        Source.writeTo(self, output, indent+1)


class Statement(Source):
    def __init__(self, parent, name=None, expr=None):
        Source.__init__(self, parent=parent, name=name)
        self.expr = expr

    @property
    def isBadLabel(self):
        if self.name in ('break', 'continue'):
            parent_names = [p.name for p in self.allParents]
            if 'while' not in parent_names and 'for' not in parent_names:
                return True
    @property
    def isNoOp(self):
        return self.name in ('else', 'finally') and (not self.lines)

    @property
    def isBlock(self):
        return self.name in ('if', 'while', 'for', 'else', 'elif', 'try', 'except', 'finally')

    def writeTo(self, output, indent):
        name = self.name
        parents = self.allParents
        lines = self.lines
        
        if self.isBadLabel or self.isNoOp:
            return

        offset = self.I * indent
        output.write('%s%s' % (offset, name))
        if self.expr is not None:
            expr = self.formatExpression(self.expr)
            output.write(' %s' % (expr, ))
        if self.isBlock:
            output.write(':')
        output.write('\n')
        if (not lines) and name not in ('break', 'continue', ):
            self.addSource('pass')
        Source.writeTo(self, output, indent+1)

    def setExpression(self, value):
        self.expr = value
