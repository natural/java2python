#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial


colors = dict(
    BLACK   = "\033[90m",
    RED     = "\033[91m",
    GREEN   = "\033[92m",
    YELLOW  = "\033[93m",
    BLUE    = "\033[94m",
    MAGENTA = "\033[95m",
    CYAN    = "\033[96m",
    WHITE   = "\033[97m",
    NORMAL  = "\033[0m",
)


def color_escape(color, value):
    return colors.get(color, '') + str(value) + colors.get('NORMAL', '')


blue = partial(color_escape, 'BLUE')
cyan = partial(color_escape, 'CYAN')
green = partial(color_escape, 'GREEN')
magenta = partial(color_escape, 'MAGENTA')
red = partial(color_escape, 'RED')
white = partial(color_escape, 'WHITE')
yellow = partial(color_escape, 'YELLOW')
