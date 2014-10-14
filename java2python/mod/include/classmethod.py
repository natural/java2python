class classmethod_(classmethod):
    """ Classmethod that provides attribute delegation.

    """
    def __getattr__(self, name):
        return getattr(self.__func__, name)
