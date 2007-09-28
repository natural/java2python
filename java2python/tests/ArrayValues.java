import junit.framework.*;

public class ArrayValues extends TestCase {

    int a[] = {1, 2, 3};

    public void testArrayValues() {
        int b[] = {4, 5, 6};
        Assert.assertEquals(a[0], 1);
        Assert.assertEquals(a[1], 2);
        Assert.assertEquals(a[2], 3);
        Assert.assertEquals(b[0], 4);
        Assert.assertEquals(b[1], 5);
        Assert.assertEquals(b[2], 6);
    }
}
