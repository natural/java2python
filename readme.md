## java2python

Simple but effective tool to translate Java source code into Python.


The java2python package can translate any syntactically valid Java source code
file.  The generated Python code is not guaranteed to run, nor is guaranteed to
be syntactically valid Python.  However, java2python works well many cases, and
in some of those, it creates perfectly usable and workable Python code.

For more information, read the [introduction][].  To install, refer to the
[installation][] page.

There are [lots of docs][], [plenty of tests][], and [many options][] for
controlling code generation.

If you're looking for old releases, check the [downloads][] link above.

Here's a very simple example:

```bash
$ cat HelloWorld.java
```
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
```python
#!/usr/bin/env python
""" generated source for module HelloWorld """

#  This is the HelloWorld class with a single method.
class HelloWorld(object):
    """ generated source for class HelloWorld """

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        print "Hello, world."

if __name__ == '__main__':
    import sys
    HelloWorld.main(sys.argv)
```


[downloads]: https://github.com/natural/java2python/downloads
[installation]: https://github.com/natural/java2python/tree/master/doc/install.md
[introduction]: https://github.com/natural/java2python/tree/master/doc/intro.md
[lots of docs]: https://github.com/natural/java2python/tree/master/doc/
[many options]: https://github.com/natural/java2python/tree/master/doc/customization.md
[plenty of tests]: https://github.com/natural/java2python/tree/master/doc/tests.md
