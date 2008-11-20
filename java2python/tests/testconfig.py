#!/usr/bin/env python
# -*- coding: utf-8 -*-


## lines written at the beginning of each generated module.  this value
## is cumulative, so when user-defined configuration modules specify
## this value, those lines are written after these.
modulePreamble = [
    '#### from overloading import overloaded',
    ]

## lines written at the end of each generated module.  this value is
## cumulative, so user-defined configuration modules may specify
## additional values.
moduleEpilogue = [
    ]


identRenames = {
    'Assert':'self',
    }


outputSubs = [
    (r'(.*?)\.getMessage\(\)', r'\1.message'),
    (r'(.*)(\w+)\.length(.*)', r'\1len(\2)\3'),
    ]


commentHandlers = []
