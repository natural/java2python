#!/usr/bin/env python
# -*- coding: utf-8 -*-

## number of spaces to indent each block
indent = 4

## prefix for comments
commentPrefix = '##'

## move inner class definitions to the top of their outer class.
## allows the outer class to reference the inner class definition
## later in its definition.
bubbleInnerClasses = True

## if True, classes are scanned for methods that look like accessors.
## Matching methods are renamed and declared as properties.
fixPropMethods = True

## if True, classes are scanned for duplicate method names.  Matching
## methods are augmented with the '@overloaded' decorator.
fixOverloadMethods = True

## if True, class methods are sorted by name before output.
sortClassMethods = False

## if True, method modifiers are written as comments prior to method
## declarations.
writeModifiersComments = False

## if True, a default docstring is generated for class statements.
writeClassDocString = True

## if True, a default docstring is generated for method statements.
writeMethodDocString = False

## if True, and if input source contains a "public static void main"
## method, a block is written to the end of the file to call the class
## method with sys.argv.
writeMainMethodScript = True

## if True, classes without base classes will instead inherit from
## object.
classesInheritObject = True

## minimum parameter count to trigger indentation of parameter names
## in method declarations.  set to 0 to disable.
minIndentParams = 5

## Note about modulePreamble and moduleEpilogue:
##
## Items in both of these lists may be strings or callables.  If
## they're callables, they should take a single argument.  The Module
## object will be passed as this single argument in the case of
## callables.

## lines written at the beginning of each generated module.  this value
## is cumulative, so when user-defined configuration modules specify
## this value, those lines are written after these.
modulePreamble = [
    '#!/usr/bin/env python',
    '# -*- coding: utf-8 -*-',
    '',
    ]

## lines written at the end of each generated module.  this value is
## cumulative, so user-defined configuration modules may specify
## additional values.
moduleEpilogue = [
    ]

## regular expression substitutions performed on source after
## generation but before final output.  this value is cumulative, so
## user-defined configuration modules can add augment these with their
## own.  each value in this list is a two-tuple of (pattern, repl).
## see the 're' module docs, specifically the re.sub function.
outputSubs = [
    (r'(\.self\.)', '.'),
    (r'String\.valueOf\((.*?)\)', r'str(\1)'),
    (r'System\.out\.println\((.*?)\)', r'print \1'),
    (r'(.*?)\.equals\((.*?)\)', r'\1 == \2'),
    (r'(.*?)\.equalsIgnoreCase\((.*?)\)', r'\1.lower() == \2.lower()'),
    (r'([\w.]+)\.size\(\)', r'len(\1)'),
    (r'(\w+)\.get\((.*?)\)', r'\1[\2]'),
    (r'(\s)(\S*?)(\.toString\(\))', r'\1str(\2)'),
    (r'(\s)(\S*?)(\.length\(\))', r'\1len(\2)'),
    ]

## mapping of java type names to python type names.  user-defined
## configuration modules can replace and/or augment this mapping.
typeTypeMap = {
    'String':'str',
    'int':'int',
    'double':'float',
    'Vector':'list',
    'boolean':'bool',
    'char':'str',
}

## mapping of java type values to python type values.  user-defined
## configuration modules can replace and/or augment this mapping.
typeValueMap = {
    'String':'""',
    'int':'0',
    'double':'0.0',
    'Vector':'[]',
    'boolean':'False',
    'str':'""',
    '[':'None',
}

## method name mapping.  user-defined configuration modules can
## replace and/or augment this with their own.
renameMethodMap = {
    'equals':'__eq__',
    'and':'and_',
    'del':'del_',
    'elif':'elif_',
    'in':'in_',
    'is':'is_',
    'not':'not_',
    'or':'or_',
    'print':'print_',
}

## generic name mapping.  user-defined configuration modules can
## replace and/or augment this with their own.
renameAnyMap = {
    'this':'self',
    'null':'None',
    'false':'False',
    'true':'True',
    'and':'and_',
    'del':'del_',
    'elif':'elif_',
    'in':'in_',
    'is':'is_',
    'not':'not_',
    'or':'or_',
    'print':'print_',
    'str':'strval',
}

## method type modifier mapping.  when input methods have modifiers
## with matching names, those names are replaced with their
## corresponding statements from this mapping.  this value can be
## replaced and/or augmented via user-defined configuration modules.
modifierDecoratorMap = {
    'synchronized':'@synchronized(mlock)',
    'static':'@classmethod',
}


baseClassMembers = {
    'Thread':['MAX_PRIORITY', 'MIN_PRIORITY', 'NORM_PRIORITY',
              'activeCount', 'checkAccess', 'countStackFrames',
              'currentThread', 'destroy', 'dumpStack',
              'enumerate', 'getContextClassLoader', 'getName',
              'getPriority', 'getThreadGroup', 'holdsLock',
              'interrupt', 'interrupted', 'isAlive',
              'isDaemon', 'isInterrupted', 'join',
              'resume', 'run', 'setContextClassLoader',
              'setDaemon', 'setName', 'setPriority',
              'sleep', 'start', 'stop', 'suspend', 'toString', 'yield',
              ],
}


variableNameMapping = {
    'str':'strval',
    'and':'and_',
    'del':'del_',
    'elif':'elif_',
    'in':'in_',
    'is':'is_',
    'not':'not_',
    'or':'or_',
    'print':'print_',
    }


exceptionTypeMapping = {
    'NoSuchFieldError':'AttributeError',
    'NoSuchMethodException':'AttributeError',
    }


## define this name in your configuration modules to sort decorators
## before they're output.  example follows.
methodPreambleSorter = None

## use a block like this to sort decorators by name.
## def methodPreambleSorter(a, b):
##     return cmp(a, b)
