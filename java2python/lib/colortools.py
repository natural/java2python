#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial


colors = {
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
    return colors.get(color, '') + str(value) + colors.get('NORMAL', '')


black = partial(escape, 'BLACK')
blue = partial(escape, 'BLUE')
cyan = partial(escape, 'CYAN')
green = partial(escape, 'GREEN')
magenta = partial(escape, 'MAGENTA')
red = partial(escape, 'RED')
white = partial(escape, 'WHITE')
yellow = partial(escape, 'YELLOW')
