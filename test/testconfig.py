#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.config import default


modulePrologueHandlers = default.modulePrologueHandlers + [
    'from overloading import overloaded',
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
