#!/usr/bin/env python
# -*- coding: utf-8 -*-


## leading indent characters (or character)
leadingIndent = '    '


## prefix for comments
commentPrefix = '## '


## move inner class definitions to the top of their outer class.
## allows the outer class to reference the inner class definition
bubbleInnerClasses = True


## minimum parameter count to trigger indentation of parameter names
## in method declarations.  set to 0 to disable.
minIndentParams = 5


## these handle shift right and bit shift right assignments.
bsrHandler = 'java2python.mods.functionBsr'
bsrHandlerAssign = 'java2python.mods.functionBsrAssign'


commentHandlers = [
    # javadoc2docstring
    # javadoc2pythondoc
    'java2python.mods.simpleComments',
]


## this value controls how enums are created, if at all.  the default
## creates enums as classes with minimum support for the interface and
## behavior defined for java classes.  in the.mods.enums module, the
## other usable functions are or fullJava, pyInts, pyStrings and
## subClass.
enumConstantHandlers = [
    #'java2python.mods.enums.pyInts',
    #'java2python.mods.enums.minJava',
]


## this value controls how import statements are processed.  the
## default converts the statement into a comment.  user-supplied
## handlers could map between java and python packages.
importHandlers = [
    'java2python.mods.commentImport',
]


## these functions control how package statements are processed.
## packages-as-comments and packages-as-setuptools are supported, but
## only one should be necessary.
packageHandlers = [
    'java2python.mods.commentPackage',
    #'java2python.mods.setupToolsPackage',
    #'java2python.mods.setupToolsPackageComment',
]


## these functions finish the construction of a class block.
classHandlers = [
    ## this function sorts sorts class methods by name.
    'java2python.mods.classes.sortMethods',

    ## this handler creates an __init__ method if required and adds a
    ## super(...) call if necessary.
    'java2python.mods.classes.updateConstructor',

    ## this function scans the class for methods that look like
    ## accessors.  matching methods are renamed and declared as
    ## properties.  references are *not* renamed, so if you use this
    ## you will need to update those references (manually or with
    ## output subsititutions).
    #'java2python.mods.classes.convertProperties',

    ## with this handler, classes are scanned for duplicate method
    ## names.  matching methods are augmented with the '@overloaded'
    ## decorator.
    'java2python.mods.classes.overloadMethods',

    ## this function inserts a simple docstring at the beginning of
    ## the class definition.
    'java2python.mods.simpleDocString',

    ## this function addss a base class to annotation types
    'java2python.mods.classes.updateAnnotation',

    'java2python.mods.classes.insertModifiersAsComments',
    'java2python.mods.classes.updateBases',
]


## these functions complete the construction of method blocks.
methodHandlers = [
    ## this function uses the methodRenames map above
    'java2python.mods.methodRename',

    ## this function inserts a simple docstring at the beginning of
    ## the class definition.
    'java2python.mods.simpleDocString',

    ## this function adds a comment with the original function's
    ## return type.
    #'java2python.mods.methods.insertReturnTypeComment',

    ## this function adds a comment with the original function's
    ## modifiers.
    #'java2python.mods.methods.insertModifiersAsComments',
]


## these functions are writers; they're called to write directly to an
## output when a module is dumped.  they use the modulePreamble and
## moduleEpilogue values below.
modulePreambleWriters = [
    'java2python.mods.modules.insertPreamble',
]


moduleEpilogueWriters = [
    'java2python.mods.modules.insertEpilogue',
    ## with this function, if the source contains a "public static
    ## void main" method, a block is written to the end of the file to
    ## call the class method with sys.argv.
    'java2python.mods.modules.ifMainScript',
]


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


## method name mapping.  user-defined configuration modules can
## replace and/or augment this with their own.
methodRenames = {
    'equals' : '__eq__',
    # 'and'    : 'and_',
    # 'del'    : 'del_',
    # 'elif'   : 'elif_',
    # 'from'   : 'from_',
    # 'in'     : 'in_',
    # 'is'     : 'is_',
    # 'not'    : 'not_',
    # 'or'     : 'or_',
    # 'print'  : 'print_',
    'toString' : '__str__',
}


exceptionRenames = {
    'IndexOutOfBoundsException' : 'IndexError',
    'NoSuchFieldError'          : 'AttributeError',
    'NoSuchMethodException'     : 'AttributeError',
    }


## method type modifier mapping.  when input methods have modifiers
## with matching names, those names are replaced with their
## corresponding statements from this mapping.  this value can be
## replaced and/or augmented via user-defined configuration modules.
modifierDecoratorMap = {
    'synchronized' : '@synchronized(mlock)',
    'static'       : '@classmethod',
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


def makeIdentifierRenames():
    """ returns a dictionary that maps python keywords and builtins to
        valid identifiers (by appending '_' to each).
    """
    from keyword import kwlist as keywords
    from __builtin__ import __dict__ as builtins
    identifiers = keywords + builtins.keys()
    return dict((ident, '%s_' % ident) for ident in identifiers)


identRenames = makeIdentifierRenames()
