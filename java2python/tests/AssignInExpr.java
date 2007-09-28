import junit.framework.*;

public class AssignInExpr extends TestCase {

    public void testExpr() {
        int a = 1, b = 2, c = 3;

        a = b += c;
        Assert.assertEquals(b, 5);
        Assert.assertEquals(a, 5);

        a = b += c += a;
        Assert.assertEquals(c, 8);
        Assert.assertEquals(b, 13);
        Assert.assertEquals(a, 13);

        a = (b = 1) * (c = 10);
        Assert.assertEquals(a, 10);
        Assert.assertEquals(b, 1);
        Assert.assertEquals(a, 10);

    }

    public void testIf() {
        int a = 4, b = 6, c = 10;

        if ((a +=b) == c) {
            c = 20;
        }
        Assert.assertEquals(a, 10);
        Assert.assertEquals(b, 6);
        Assert.assertEquals(c, 20);
    }

    public void testWhile() {
        int i = 0;

        while (++i < 10) {
            Assert.assertTrue(i < 10);
        }
        Assert.assertEquals(i, 10);

    }

    public void testDo() {
        int i = 0;
        do {
            Assert.assertTrue(i < 10);
        } while (++i < 10);
        Assert.assertEquals(i, 10);
    }

    public void testPostIncDec() {
        int i = 0, j = 0, k = 0;
        i = j++;
        Assert.assertEquals(i, 0);
        Assert.assertEquals(j, 1);

        if (++i == j++) {
            k = 3;
        }
        Assert.assertEquals(i, 1);
        Assert.assertEquals(j, 2);
        Assert.assertEquals(k, 3);
    }

    public void testAndOr() {
        int i = 0, j = 0;

        if (i++ == 1 && j++ == 1) {
            Assert.fail("and test fail");
        } else {
            Assert.assertEquals(i, 1);
            Assert.assertEquals(j, 0);
        }

        if (--i != 0 || j-- == 0) {
            Assert.assertEquals(i, 0);
            Assert.assertEquals(j, -1);
        } else {
            Assert.fail("or test fail");
        }

    }

}
