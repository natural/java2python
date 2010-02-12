#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
#
# This is the default configuration file for java2python.  Unless
# explicity disabled with the '-n' or '--nodefaults' options, the j2py
# script will reference this file for runtime options.
#
# The j2py script accepts additional configuration modules with the
# '-c' or '--config' arguments.  These arguments may be repeated.
#
# There are three flavors of options: all, last, and combined.  The
# semantics are:
#
#  * all means the value is loaded from each configuration module and
#    returned as a sequence.
#
#  * last means the value is selected from the last configuration
#    module specified.  if no configuration modules are specified (and
#    if the default is not disabled), the last value will be the value
#    in this module.
#
#  * combined means that the values (dictionaries) will be merged in
#    order and returned as a single dictionary.
#
# In some cases, noted below, the value or values may be a dotted path
# to a python callable.  In these cases, the callable is imported and
# run when needed.


## leading indent characters (or character).  this is a "last" option.
leadingIndent = '    '


## prefix for comments.  this is a "last" option.
commentPrefix = '## '


modulePrologueHandlers = [
    'java2python.mods.simpleShebang',
    'java2python.mods.simpleDocString',
    'java2python.mods.simpleModuleImports',
]

moduleEpilogueHandlers = [
    'java2python.mods.scriptMainStanza',
]


moduleOutputHandlers = [
    'java2python.mods.outputSubs',
#    'java2python.mods.scriptMainStanza',
]


methodDocStringHandlers = [
    'java2python.mods.simpleDocString',
]


moduleOutputSubs = [
#    (r'(\.self\.)', '.'),
    (r'String\.valueOf\((.*?)\)', r'str(\1)'),
    (r'System\.out\.println\((.*)\)', r'print \1'),
    (r'System\.out\.print_\((.*?)\)', r'print \1,'),
    (r'(.*?)\.equals\((.*?)\)', r'\1 == \2'),
    (r'(.*?)\.equalsIgnoreCase\((.*?)\)', r'\1.lower() == \2.lower()'),
    (r'([\w.]+)\.size\(\)', r'len(\1)'),
    (r'(\w+)\.get\((.*?)\)', r'\1[\2]'),
    (r'(\s)(\S*?)(\.toString\(\))', r'\1str(\2)'),
    (r'(\s)(\S*?)(\.toLowerCase\(\))', r'\1\2.lower()'),
    (r'(\s)(\S*?)(\.length\(\))', r'\1len(\2)'),
    (r'(.*?)IndexOutOfBoundsException\((.*?)\)', r'\1IndexError(\2)'),
    (r'\.__class__\.getName\(\)', '.__class__.__name__'),
]


modulePostParseHandlers = [

    ## You only need one of these:
    'java2python.mods.simpleInterfaces',
    #'java2python.mods.abcInterfaces',
    #'java2python.mods.zopeInterfaces',
]

classDocStringHandlers = [
    'java2python.mods.simpleDocString',
]


classBaseLookup = 'java2python.mods.defaultClassBase'


## This enum constant handler inspects the enum block and determines
## the best handler to call.  If the enum constant contains a
## constructor, it defers to the enumConstantInstances, otherwise it
## uses the enumConstantStrings:
enumEpilogueHandler = 'java2python.mods.enumConstantSelector'


## This handler generates enum constants as instances of the enum
## class (as class attributes):
# enumEpilogueHandler = 'java2python.mods.enumConstantInstances'

## This handler generates enum constants as integers:
# enumEpilogueHandler = 'java2python.mods.enumConstantInts'

## This handler generates enum constants as strings:
# enumEpilogueHandler = 'java2python.mods.enumConstantStrings'



inputSubs = [
]

outputSubs = [
    (r'(\.self\.)', '.'),
    (r'String\.valueOf\((.*?)\)', r'str(\1)'),
    (r'System\.out\.println\((.*)\)', r'print \1'),
    (r'System\.out\.print_\((.*?)\)', r'print \1,'),
    (r'(.*?)\.equals\((.*?)\)', r'\1 == \2'),
    (r'(.*?)\.equalsIgnoreCase\((.*?)\)', r'\1.lower() == \2.lower()'),
    (r'([\w.]+)\.size\(\)', r'len(\1)'),
    (r'(\w+)\.get\((.*?)\)', r'\1[\2]'),
    (r'(\s)(\S*?)(\.toString\(\))', r'\1str(\2)'),
    (r'(\s)(\S*?)(\.toLowerCase\(\))', r'\1\2.lower()'),
    (r'(\s)(\S*?)(\.length\(\))', r'\1len(\2)'),
    (r'(.*?)IndexOutOfBoundsException\((.*?)\)', r'\1IndexError(\2)'),
    (r'\.__class__\.getName\(\)', '.__class__.__name__'),
]

## mapping of java type names to python type names.  user-defined
## configuration modules can replace and/or augment this mapping.
typeRenames = {
    'String'  : 'str',
    'Integer' : 'int',
    'Object'  : 'object',
    'Date'    : 'datetime.date',
    'int'     : 'int',
    'double'  : 'float',
    'Vector'  : 'list',
    'boolean' : 'bool',
    'char'    : 'str',
    '['       : 'list',
}


## mapping of java type values to python type values.  user-defined
## configuration modules can replace and/or augment this mapping.
typeValueMap = {
    'String'  : '""',
    'int'     : '0',
    'double'  : '0.0',
    'Vector'  : '[]',
    'boolean' : 'False',
    'str'     : '""',
    '['       : 'None',
}


## not implemented:
## move inner class definitions to the top of their outer class.
## allows the outer class to reference the inner class definition
#bubbleInnerClasses = True

## minimum parameter count to trigger indentation of parameter names
## in method declarations.  set to 0 to disable.
#minIndentParams = 5

## these handle shift right and bit shift right assignments.
#bsrHandler = 'java2python.mods.functionBsr'
#bsrHandlerAssign = 'java2python.mods.functionBsrAssign'

# etc.,
