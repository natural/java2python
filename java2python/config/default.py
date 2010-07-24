#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is the default configuration file for java2python.  Unless
# explicity disabled with the '-n' or '--nodefaults' options, the j2py
# script will import this module for runtime configuration.

from java2python.mod import basic, transform
from java2python.lang.selector import *


# Leading indent character or characters.  Read PEP 8 before you
# override this.
indentPrefix = ' '*4


# Prefix character or characters for comments.  Again, you should read
# PEP 8 before you override this.
commentPrefix = '# '


# When true, class definitions will be bubbled to the top of their
# container (outer class or module).
reorderClassDefs = True


# These generator-functions yield lines for a module prologue.
modulePrologueHandlers = [
    basic.simpleShebang,
    basic.simpleDocString,
    basic.configImports,
    basic.commentedImports,
    basic.commentedPackageName,
]


# These generator-functions yield lines for a module epilogue.
moduleEpilogueHandlers = [
    basic.scriptMainStanza,
]


# These generator-functions yield (possibly modified) source strings
# for a module.  The 'outputSubs' handler references the list of
# regular expression substitutions near the end of this module.
moduleOutputHandlers = [
    basic.outputSubs,
]


# These generator-functions yield doc strings for classes.
classDocStringHandlers = [
    basic.simpleDocString,
]


# These generator-functions yield doc strings for enums.
enumDocStringHandlers = [
    basic.simpleDocString,
]


# These generator-functions yield doc strings for methods.
methodDocStringHandlers = [
    basic.simpleDocString,
]


# These generator-functions yield extra method decorators.
methodExtraDecoratorHandlers = [
    basic.maybeClassMethod,
    basic.overloadedClassMethods,
]


# These generator-functions yield base types for classes.
classBaseHandlers = [
    basic.mapClassType,
]


# These generator-functions yield base types for enums.
enumBaseHandlers = [
    basic.mapClassType
]


# generator-functions that yield base types for interfaces.
interfaceBaseHandlers = [
    basic.mapClassType
]


# This handler creates enum values on enum classes after they've been
# defined.  The handler matches Java semantics fairly closely by using
# strings.  Refer to the documentation for details.
enumValueHandler = basic.enumConstStrings

# Alternatively, you can use this handler to construct enum values as
# integers.
#enumValueHandler = basic.enumConstInts



expressionVariableNamingHandler = basic.globalNameCounter


# The AST transformation function uses these declarations to modify an
# AST before compiling it to python source.  Having these declarations
# in a config file gives clients an opportunity to change the
# transformation behavior.

astTransforms = [
    (Type('NULL'),  transform.null2None),
    (Type('FALSE'), transform.false2False),
    (Type('TRUE'),  transform.true2True),
    (Type('IDENT'), transform.keywordSafeIdent),

    (Type('FLOATING_POINT_LITERAL'),
     transform.syntaxSafeFloatLiteral),

    (Type('TYPE') > Type('QUALIFIED_TYPE_IDENT') > Type('IDENT'),
     transform.typeSub)
]


# not implemented:

# minimum parameter count to trigger indentation of parameter names
# in method declarations.  set to 0 to disable.
#minIndentParams = 5

# these handle shift right and bit shift right assignments.
#bsrHandler = 'basic.functionBsr'
#bsrHandlerAssign = 'basic.functionBsrAssign'


# Values below are used by the handlers.  They're here for
# convenience.


# module output subs.
moduleOutputSubs = [
    (r'System\.out\.println\((.*)\)', r'print \1'),
    (r'System\.out\.print_\((.*?)\)', r'print \1,'),
    (r'(.*?)\.equals\((.*?)\)', r'\1 == \2'),
    (r'(.*?)\.equalsIgnoreCase\((.*?)\)', r'\1.lower() == \2.lower()'),
    (r'([\w.]+)\.size\(\)', r'len(\1)'),
    (r'(\w+)\.get\((.*?)\)', r'\1[\2]'),
    (r'(\s)(\S*?)(\.toString\(\))', r'\1\2.__str__()'),
    (r'(\s)(\S*?)(\.toLowerCase\(\))', r'\1\2.lower()'),
    (r'(\s)(\S*?)(\.length\(\))', r'\1len(\2)'),
    (r'(.*?)IndexOutOfBoundsException\((.*?)\)', r'\1IndexError(\2)'),
    (r'\.__class__\.getName\(\)', '.__class__.__name__'),
    (r'\.getClass\(\)', '.__class__'),
    (r'\.getName\(\)', '.__name__'),
    (r'\.getInterfaces\(\)', '.__bases__'),
    #(r'String\.valueOf\((.*?)\)', r'str(\1)'),
    #(r'(\s)(\S*?)(\.toString\(\))', r'\1str(\2)'),
]


typeSubs = {
    'Boolean' : 'bool',
    'IndexOutOfBoundsException' : 'IndexError',
    'Integer' : 'int',
    'Object' : 'object',
    'String' : 'str',
    'char' : 'str',
    'double' : 'float',
    'java.lang.String' : 'str',
}
