#!/usr/bin/env python
# -*- coding: utf-8 -*-
from java2python.lib import import_name


def set_config_target(target, names, includeDefault=True):
    """ build and set a Config object on the target object

    @param names sequence of module names
    @keyparam includeDefault=True flag to include default configuration module
    @return None
    """
    if includeDefault:
        names.insert(0, 'java2python.lib.defaultconfig')
    target.config = Config(*names)


class Config:
    """ Config -> wraps multiple configuration modules


    """
    def __init__(self, *names):
        self.configs = [import_name(name) for name in names]

    def all(self, name, missing=None):
        """ value of name in each config module

        @param name module attribute as string
        @keyparam missing=None default for missing attributes
        @return list of values
        """
        return (getattr(config, name, missing) for config in self.configs)

    def last(self, name, default=None):
        """ value from final config module to define name

        @param name module attribute as string
        @keyparam default=None value returned if all modules lack name
        @return value from config module
        """
        for config in reversed(self.configs):
            if hasattr(config, name):
                return getattr(config, name)
        return default

    def combined(self, name):
        """ combined mapping of named dictionaries from all config modules

        @param dictionary attribute as string
        @return dictionary updated with each named dictionary
        """
        combined = {}
        for mapping in self.all(name, {}):
            combined.update(mapping)
        return combined
