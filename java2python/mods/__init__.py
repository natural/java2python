#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def simpleShebang(module):
    yield '#!/usr/bin/env python'


def simpleDocString(block):
    return [
	'""" generated source for %s' % block.getName(),
	'',
	'"""'
    ]


def newLine(block):
    ## ["\n"] doesn't work and it's annoying.
    return []


def outputSubs(module, text):
    subs = module.config.all('moduleOutputSubs', [])
    for sub in subs:
	for pattern, repl in sub:
	    text = re.sub(pattern, repl, text)
    return text


def scriptMainStanza(module, text):
    name = module.getName()
    indent = module.indent()

    def filterClass(x):
	return x.blockTypeName()=='class' and x.getName()==name

    def filterMethod(x):
	return x.blockTypeName()=='method' and \
	       x.isPublic() and x.isStatic() and x.isVoid()

    for cls in [c for c in module.getChildren() if filterClass(c)]:
	if [m for m in cls.getChildren() if filterMethod(m)]:
	    return text +  '\n' + '\n'.join(
		["if __name__ == '__main__':",
		 ("%simport sys" % indent),
		 ("%s%s.main(sys.argv)" % (indent, name)),
		 ]
		)

    return text


def scriptTrailingNewLine(module, text):
    if text and text[-1] != '\n':
	return text + u'\n'
    return text



