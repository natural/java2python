import junit.framework.*;

public class FloatFix extends TestCase {
    public void runTest() {
        float b = 1.2f;
        Assert.assertEquals(b, 1.2f);
    }
}
