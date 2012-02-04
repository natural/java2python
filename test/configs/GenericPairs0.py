#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.config import default


moduleOutputSubs = default.moduleOutputSubs + [
    (r'import java\.util', r''),
    (r'first\ \=\ T\(\)', 'first = None'),
    (r'second\ \=\ S\(\)', 'second = None'),
]
