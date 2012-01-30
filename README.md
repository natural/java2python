Simple but effective tool to translate Java source code into Python.

Here's a quick example.  First, the Java source:


    $ cat HelloWorld.java
    // This is the HelloWorld class with it's single method.
    class HelloWorld {
        public static void main(String[] args) {
            System.out.println("Hello, world.");
        }
    }

Next, we translate:

    $ j2py HelloWorld.java
    #!/usr/bin/env python
    """ generated source for module HelloWorld

    """
    #  This is the HelloWorld class with it's single method.
    class HelloWorld(object):
        """ generated source for class HelloWorld

        """
        @classmethod
        def main(cls, args):
            """ generated source for method main

            """
            print "Hello, world."


    if __name__ == '__main__':
        import sys
        HelloWorld.main(sys.argv)
