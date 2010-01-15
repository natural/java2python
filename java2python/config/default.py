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
]


moduleEpliogueHandlers = [
]

moduleOutputHandlers = [
    'java2python.mods.outputSubs',
    'java2python.mods.scriptMainStanza',
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


classDocStringHandlers = [
    'java2python.mods.simpleDocString',
]


classBaseLookup = 'java2python.mods.defaultClassBase'

## handlers for generating text inserted at the top of each module.
## this is a "last" option.  note that the preamble for a module
## should include the docstring generator.  (other docstrings are
## indented).
modulePreamble = [
#    'java2python.mods.simpleShebang',
#    'java2python.mods.simpleDocString',
]

## lines of static text inserted at the end of each module.  this is a
## "last" option.
moduleEpilogue = [
    ## TODO:  add "trailing-newline" handler.
]


methodPreamble = [
#    'java2python.mods.newLine',
    ]

classDocString = [
#    'java2python.mods.simpleDocString',
    ]


methodDocString = [
#    'java2python.mods.simpleDocString',
    ]


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
