/*

Cribbed from sun docs:

http://java.sun.com/j2se/1.5.0/docs/guide/language/enums.html

*/
public enum Operation {
      PLUS   { double eval(double x, double y) { return x + y; } },
      MINUS  { double eval(double x, double y) { return x - y; } },
      TIMES  { double eval(double x, double y) { return x * y; } },
      DIVIDE { double eval(double x, double y) { return x / y; } };

      // Do arithmetic op represented by this constant
      abstract double eval(double x, double y);
}

