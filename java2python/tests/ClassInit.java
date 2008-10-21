import junit.framework.*;

class SimpleClassInit {
    static int x = 1;
    static int y;

    static {
        x = 2;
    }

}

public class ClassInit extends TestCase {

    public void testClassInit() {
        Assert.assertEquals(SimpleClassInit.x, 2);
    }

    public static void main(String[] args) {
        System.out.println(SimpleClassInit.x);
    }


}
