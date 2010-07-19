#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This is the default configuration file for java2python.  Unless
# explicity disabled with the '-n' or '--nodefaults' options, the j2py
# script will reference this file for runtime configuration.
#
import java2python.mod


## leading indent character or characters.
indentPrefix = '    '


## prefix for comments.
commentPrefix = '## '


## generator-functions that yield lines for a module prologue.
modulePrologueHandlers = [
    java2python.mod.simpleShebang,
    java2python.mod.simpleDocString,
    java2python.mod.configImports,
    java2python.mod.commentedImports,
    java2python.mod.commentedPackageName,
]


## generator-functions that yield lines for a module epilogue.
moduleEpilogueHandlers = [
    java2python.mod.scriptMainStanza,
]


## generator-functions that yield (possibly modified) source strings
## for a module.
moduleOutputHandlers = [
    java2python.mod.outputSubs,
]


## generator-functions that yield doc strings for classes.
classDocStringHandlers = [
    java2python.mod.simpleDocString,
]


## generator-functions that yield doc strings for enums.
enumDocStringHandlers = [
    java2python.mod.simpleDocString,
]


## generator-functions that yield doc strings for methods.
methodDocStringHandlers = [
    java2python.mod.simpleDocString,
]


## generator-functions that yield extra method decorators.
methodExtraDecoratorHandlers = [
    java2python.mod.maybeClassMethod,
    java2python.mod.overloadedClassMethods,
]


## generator-functions that yield base types for classes.
classBaseHandlers = [
    java2python.mod.mapClassType,
]


## generator-functions that yield base types for enums.
enumBaseHandlers = [
    java2python.mod.mapClassType
]


## generator-functions that yield base types for interfaces.
interfaceBaseHandlers = [
    java2python.mod.mapClassType
]


##
# Note that the following two enum value handlers are only called for
# basic enumerations, not enumerations that take arguments in a
# constructor.  When those kinds of enum values are detected, the
# package will create the enum values as instance of the enum class,
# and these handlers will not be invoked.

# This handler creates enum values on enum classes after they've been
# defined.  The handler matches Java semantics fairly closely by using
# strings.
enumValueHandler = java2python.mod.enumConstStrings

# Alternatively, you can use this handler to construct enum values as
# integers.
#enumValueHandler = 'java2python.mod.enumConstInts'



## not implemented:

## move inner class definitions to the top of their outer class.
## allows the outer class to reference the inner class definition
#bubbleInnerClasses = True

## minimum parameter count to trigger indentation of parameter names
## in method declarations.  set to 0 to disable.
#minIndentParams = 5

## these handle shift right and bit shift right assignments.
#bsrHandler = 'java2python.mod.functionBsr'
#bsrHandlerAssign = 'java2python.mod.functionBsrAssign'


##
# Below are values used by the handlers.  They're here for
# convenience.


## module output subs.
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
    #(r'(\.self\.)', '.'),
    #(r'String\.valueOf\((.*?)\)', r'str(\1)'),
    #(r'(\s)(\S*?)(\.toString\(\))', r'\1str(\2)'),
]


typeSubs = {
    'Boolean'          : 'bool',
    'Object'           : 'object',
    'String'           : 'str',
    'char'             : 'str',
    'double'           : 'float',
    'java.lang.String' : 'str',
    'IndexOutOfBoundsException' : 'IndexError',
}


from java2python.lang.selector import *
from java2python.mod import transforms


transforms = [
    (Type('NULL'), transforms.null2None),
    (Type('FALSE'), transforms.false2False),
    (Type('TRUE'), transforms.true2True),
    (Type('IDENT'), transforms.keywordSafeIdent),
    (Type('FLOATING_POINT_LITERAL'), transforms.syntaxSafeFloatLiteral),
    (Type('TYPE') > Type('QUALIFIED_TYPE_IDENT') > Type('IDENT'), transforms.typeSub)
]
