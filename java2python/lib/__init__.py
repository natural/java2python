#!/usr/bin/env python
# -*- coding: utf-8 -*-
# java2python.lib -> common library bits.

from functools import partial


class FS(object):
    """ Format string abbreviations. """
    l = '{left}'
    r = '{right}'
    c = ':'
    lc = l + c
    lr = l + r
    lsr = l + ' ' + r
    lsrc = lsr + c

    @classmethod
    def op(cls, op):
        """ Returns a format string for the given operation. """
        l, r = cls.l, cls.r
        if op == '>>>':
            return '(' + l + ' & (2**32+' + l + ')) >> ' + r
        if op == '>>>=':
            return l + ' = bsr(' + l + ', ' + r + ')'
        return l + ' ' + op + ' ' + r


escapes = {
    'BLACK'   : '\033[90m',
    'BLUE'    : '\033[94m',
    'CYAN'    : '\033[96m',
    'GREEN'   : '\033[92m',
    'MAGENTA' : '\033[95m',
    'NORMAL'  : '\033[0m',
    'RED'     : '\033[91m',
    'WHITE'   : '\033[97m',
    'YELLOW'  : '\033[93m',
    }


def escape(color, value):
    return escapes.get(color, '') + str(value) + escapes.get('NORMAL', '')


class colors:
    black = partial(escape, 'BLACK')
    blue = partial(escape, 'BLUE')
    cyan = partial(escape, 'CYAN')
    green = partial(escape, 'GREEN')
    magenta = partial(escape, 'MAGENTA')
    red = partial(escape, 'RED')
    white = partial(escape, 'WHITE')
    yellow = partial(escape, 'YELLOW')
