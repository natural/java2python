from java2python.parser import JavaLexer as LexerModule

def tokens():
    for k in dir(LexerModule):
	v = getattr(LexerModule, k)
	if isinstance(v, (int, )):
	    yield (v, k)

tokens = dict(tokens())


def dumpTree(fd, tree, level=0):
    token = tree.getToken()
    if token is None:
	return
    tokenType = tokens.get(token.type, '?')
    print >> fd, '{0}{1}'.format('    ' * level, tokenType)
    for child in tree.getChildren():
	dumpTree(fd, child, level+1)
