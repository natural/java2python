#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial


colors = dict(
    BLACK   = "\033[90m",
    RED     = "\033[91m",
    GREEN   = "\033[92m",
    YELLOW  = "\033[93m",
    BLUE    = "\033[94m",
    MAGNETA = "\033[95m",
    CYAN    = "\033[96m",
    WHITE   = "\033[97m",
    NORMAL  = "\033[0m",
)


def color_escape(color, value):
    return colors.get(color, '') + str(value) + colors.get('NORMAL', '')


red = partial(color_escape, 'RED')
yellow = partial(color_escape, 'YELLOW')
green = partial(color_escape, 'GREEN')
cyan = partial(color_escape, 'CYAN')
white = partial(color_escape, 'WHITE')
