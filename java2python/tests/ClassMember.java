import junit.framework.*;

class Simple {
    public int a = 1;
    public int [] b = new int[10];
}

public class ClassMember extends TestCase {
    
    public void testNonStaticMember() {
        Simple x = new Simple();
        Simple y = new Simple();
        x.b[0] = 1;
        Assert.assertEquals(y.b[0], 0);
    }
}
