Simple but effective tool to translate Java source code into Python.

Here's a quick example.  First, the Java source:


    $ cat HelloWorldApp.java
    class HelloWorldApp {
        public static void main(String[] args) {
            System.out.println('Hello, world.');
            System.out.println(args);
        }
    }

Next, we translate:

    $ j2py -i HelloWorldApp.java
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    class HelloWorldApp(object):
        ''' generated source for HelloWorldApp

        '''
        @classmethod
        def main(cls, args):
            print 'Hello, world.'
            print args

    if __name__ == '__main__':
        import sys
        HelloWorldApp.main(sys.argv)

