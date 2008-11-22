class Simple {
    public int a = 1;
    public int [] b = new int[10];
    public static int c = 0;

    public void add() {
        c++;
        a++;
    }

    public void setA(int a) {
        this.a = a;
    }
}

public class ClassMember  {
    public void testNonStaticMember() {
        Simple x = new Simple();
        Simple y = new Simple();
        x.b[0] = 1;
        Assert.assertEquals(y.b[0], 0);
    }

    public void testStaticMember() {
        Simple x = new Simple();
        x.add();
        x.add();
        Assert.assertEquals(Simple.c, 2);
        Assert.assertEquals(x.c, 2);
    }

    public void testParamName() {
        Simple x = new Simple();
        x.setA(10);
        Assert.assertEquals(x.a, 10);
    }
}
