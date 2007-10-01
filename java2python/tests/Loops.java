import junit.framework.*;

public class Loops extends TestCase {

    public void testFor() {
        int a, b;

        for(a = 1; a < 10;){
            a+= 3;
        }
        Assert.assertEquals(a, 10);

        for (b = 0; b < 20; b+=2) {
        }
        Assert.assertEquals(b, 20);
    }

    public void testDeadLoop() {
        int x = 0;
        for (;;) {
            x ++;
            if (x > 10) break;
        }
    }

    public void testDoWhile() {
        int x = 0;
        do {
            x += 1;
        } while (x <= 10);
        Assert.assertEquals(x, 11);
    }

}

