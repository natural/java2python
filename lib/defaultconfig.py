#!/usr/bin/env python
# -*- coding: utf-8 -*-

indent = 4


outputSubs = [
    (r'(\.self\.)', '.'),
    (r'String\.valueOf\((.*?)\)', r'str(\1)'),
    (r'System\.out\.println\((.*?)\)', r'print \1'),
    (r'(.*?)\.equals\((.*?)\)', r'\1 == \2'),
    (r'(.*?)\.equalsIgnoreCase\((.*?)\)', r'\1.lower() == \2.lower()'),
    (r'([\w.]+)\.size\(\)', r'len(\1)'),
    (r'(\w+)\.get\((.*?)\)', r'\1[\2]'),
    ]


typeTypeMap = {
    'String':'str',
    'int':'int',
    'double':'float',
    'Vector':'list',
    'boolean':'bool',
}


typeValueMap = {
    'String':'""',
    'int':'0',
    'double':'0.0',
    'Vector':'[]',
    'boolean':'False',
    'str':'""',
}


renameMethodMap = {
    'equals':'__eq__'
}


renameAnyMap = {
    'this':'self',
    'null':'None',
    'false':'False',
    'true':'True',
}


modifierDecoratorMap = {
    'synchronized':'## original method synchronized'
}


modulePreable = [
    '#!/usr/bin/env python',
    '# -*- coding: utf-8 -*-',
    '',
    ]


bubbleInnerClasses = True
scanPropMethods = True
scanOverloadMethods = True
sortClassMethods = False
writeModifiersComments = False
writeClassDocString = True

commentPrefix = '##'
