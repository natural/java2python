#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python import maybeattr


def insertModifiers(block):
    nondecos = [m for m in block.modifiers if not m.startswith('@')]
    block.prefix.insert(0, '# modifiers: %s' % (str.join(', ', nondecos)))
