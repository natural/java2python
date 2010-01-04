#!/usr/bin/env python
# -*- coding: utf-8 -*-


## lines written at the beginning of each generated module.  this value
## is cumulative, so when user-defined configuration modules specify
## this value, those lines are written after these.
modulePreamble = [
    'from threading import Lock',
    'from overloading import overloaded',
    'from java2python.config.examples import Annotation, Enum',
    ]





outputSubs = [
    (r'(.*?)\.getMessage\(\)', r'\1.message'),
    (r'(.*?)(\w+?)\.length(.*)', r'\1len(\2)\3'),
    (r'assertEquals', 'self.assertEquals'),
    (r'## import junit.framework', 'from unittest import *'),
    (r'(.*?)\.getClass\(\)', r'\1.__class__'),
    (r'(.*?)\.getName\(\)', r'\1.__name__'),
    (r'(.*?)\.getInterfaces\(\)', r'\1.__bases__'),

    (r'(.*?)\.fooProp\(\)', r'\1.fooProp'),
    (r'(.*?)\.fooProp\((.+)\)', r'\1.fooProp = \2'),

    (r'(.*?)lock(.*?) = object\(\)', r'\1lock\2 = Lock()'),

    ## these two fudge something that should be handled in parsing
    (r'(.*?)StaticInner\(\)', r'\1cls.StaticInner()'),
    (r'(.*?)outer\.cls', r'\1outer'),
    (r'from java\.util import \*', ''),
    ]



enumConstantHandlers = [
#    'java2python.mods.enums.pyStrings',
    'java2python.mods.enums.minJava',

]

classHandlers = [
    #'java2python.mods.classes.sortMethods',
    'java2python.mods.classes.updateConstructor',

    'java2python.mods.classes.convertProperties',
    'java2python.mods.classes.overloadMethods',
    'java2python.mods.simpleDocString',
    'java2python.mods.classes.insertModifiersAsComments',
    'java2python.mods.classes.updateBases',
    'java2python.mods.classes.updateAnnotation',

]
