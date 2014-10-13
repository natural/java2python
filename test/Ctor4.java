class Base {
    public int x = 0;

    public Base() {
        x =+ 1;
        System.out.println(x);
    }
}

class Test1 extends Base {
    public int y = 0;

    public Test1() {
        this(42);
    }

    protected Test1(int arg) {
        y = arg;
    }
}


public class Ctor4  {
    public static void main(String[] args) {
        Test1 t1 = new Test1();
        System.out.println(t1.y);
    }
}
