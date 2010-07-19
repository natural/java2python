#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):
    """ Config -> wraps multiple configuration modules

    """
    def __init__(self, names):
	self.configs = [self.load(name) for name in names]

    def __iter__(self):
	return iter(self.configs)

    def every(self, key, default=None):
	return [getattr(config, key, default) for config in self]

    def last(self, key, default=None):
	for config in reversed(list(self)):
	    if hasattr(config, key):
		return getattr(config, key)
	return default

    def handler(self, key, default=None):
	handler = self.last(key, default)
	return handler

    def handlers(self, key, default=None):
	handlers = self.last(key, default)
	if handlers is default:
	    return
	for handler in handlers:
	    yield handler

    @staticmethod
    def load(name):
	""" load(name) -> import and return a module by name in dotted form.

	Copied from the Python lib docs.
	"""
	mod = __import__(name)
	for comp in name.split('.')[1:]:
	    mod = getattr(mod, comp)
	return mod
