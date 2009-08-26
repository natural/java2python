#!/usr/bin/env python
# -*- coding: utf-8 -*-


## lines written at the beginning of each generated module.  this value
## is cumulative, so when user-defined configuration modules specify
## this value, those lines are written after these.
modulePreamble = [
    'from overloading import overloaded',
    ]





outputSubs = [
    (r'(.*?)\.getMessage\(\)', r'\1.message'),
    (r'(.*)(\w+)\.length(.*)', r'\1len(\2)\3'),
    (r'assertEquals', 'self.assertEquals'),
    (r'## import junit.framework', 'from unittest import *'),
    (r'(.*?)\.getClass\(\)', r'\1.__class__'),
    (r'(.*?)\.getName\(\)', r'\1.__name__'),
    (r'(.*?)\.getInterfaces\(\)', r'\1.__bases__'),
    ]



enumConstantHandlers = [
#    'java2python.mods.enums.pyStrings',
    'java2python.mods.enums.minJava',

]
