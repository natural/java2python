import junit.framework.*;

class SuperClass {
    public int x = 0;
    public String y = null;

    public SuperClass() {
        x = 1;
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

public class SuperCtorTest extends TestCase {
    
    public void testSuperCtor() {
        SuperCtorTest1 t1 = new SuperCtorTest1();
        Assert.assertEquals(1, t1.x);

        SuperCtorTest2 t2 = new SuperCtorTest2();
        Assert.assertEquals(1, t2.x);

        SuperCtorTest3 t3 = new SuperCtorTest3();
        Assert.assertEquals("arg", t3.y);
        Assert.assertEquals(0, t3.x);

        SuperCtorTest4 t4 = new SuperCtorTest4(10);
        Assert.assertEquals(10, t4.x);
    }

}
