class Base {
    public int x = 42;
    public String y = null;

    public Base() {
        x = 43;
    }

    public Base(String arg) {
        y = arg;
    }

    public Base(int arg) {
        x = arg;
    }
}

class Test1 extends Base {
    public Test1() {
    }
}


class Test2 extends Base {
    public Test2() {
	super();
    }
}


class Test3 extends Base {
    public Test3() {
	super("arg");
    }
}


class Test4 extends Base {
    public Test4(int arg) {
	super(arg);
    }
}


public class Ctor3  {
    public static void main(String[] args) {
        Test1 t1 = new Test1();
        System.out.println(43 == t1.x ? 1 : 0);

        Test2 t2 = new Test2();
        System.out.println(43 == t2.x ? 1 : 0);

        Test3 t3 = new Test3();
        System.out.println("arg" == t3.y ? 1 : 0);
        System.out.println(42 == t3.x ? 1 : 0);

        Test4 t4 = new Test4(10);
        System.out.println(10 == t4.x ? 1 :0);
    }
}
