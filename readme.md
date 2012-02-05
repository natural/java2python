## java2python

Simple but effective tool to translate Java source code into Python.


There are [lots of docs][], [plenty of tests][], and [many options][] for
controlling code generation.

I'm in the process of finalizing the documentation and packaging a release.
That will be release 0.5 when it's done.  If you're looking for old releases,
check the [downloads][] link above.

Here's a very simple example.  First we show the file:

```bash
$ cat HelloWorld.java
```

And we get this:

```java    
// This is the HelloWorld class with a single method.
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world.");
    }
}
```

Next we run our program:


```bash
$ j2py HelloWorld.java
```

And we get this:

```python
#!/usr/bin/env python
""" generated source for module HelloWorld

"""
#  This is the HelloWorld class with a single method.
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
```


[lots of docs]: https://github.com/natural/java2python/tree/master/doc/
[plenty of tests]: https://github.com/natural/java2python/tree/master/test/
[many options]: https://github.com/natural/java2python/tree/master/doc/customization.md
[downloads]: https://github.com/natural/java2python/downloads
