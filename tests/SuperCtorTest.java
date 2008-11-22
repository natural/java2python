class SuperClass {
    public int x = 42;
    public String y = null;

    public SuperClass() {
        x = 43;
    }

    public SuperClass(String arg) {
        y = arg;
    }

    public SuperClass(int arg) {
        x = arg;
    }
}

class SuperCtorTest1 extends SuperClass {
	public SuperCtorTest1() {
    }
}


class SuperCtorTest2 extends SuperClass {
	public SuperCtorTest2() {
		super();
	}
}


class SuperCtorTest3 extends SuperClass {
	public SuperCtorTest3() {
		super("arg");
	}
}

class SuperCtorTest4 extends SuperClass {
	public SuperCtorTest4(int arg) {
		super(arg);
	}
}

public class SuperCtorTest  {
    public static void main(String[] args) {
        SuperCtorTest1 t1 = new SuperCtorTest1();
        System.out.println(43 == t1.x ? 1 : 0);

        SuperCtorTest2 t2 = new SuperCtorTest2();
        System.out.println(43 == t2.x ? 1 : 0);

        SuperCtorTest3 t3 = new SuperCtorTest3();
        System.out.println("arg" == t3.y ? 1 : 0);
        System.out.println(42 == t3.x ? 1 : 0);
        System.out.println(t3.x);

        SuperCtorTest4 t4 = new SuperCtorTest4(10);
        System.out.println(10 == t4.x ? 1 :0);
    }
}
