import junit.framework.*;

class SimpleClassInit {
    static int x = 1;

    static {
        x = 2;
    }

}

public class ClassInit extends TestCase {

    public void testClassInit() {
        Assert.assertEquals(SimpleClassInit.x, 2);
    }
}
