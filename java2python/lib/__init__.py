def import_name(name):
    """ import_name(name) -> import and return a module by name in dotted form

    Copied from the Python lib docs.

    @param name module or package name in dotted form
    @return module object
    """
    mod = __import__(name)
    for comp in name.split('.')[1:]:
        mod = getattr(mod, comp)
    return mod

