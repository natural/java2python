import junit.framework.*;

public class Switches extends TestCase {

    public void testSwitches() {
        Assert.assertEquals(switch1(1), 1);
        Assert.assertEquals(switch1(2), 2);
        Assert.assertEquals(switch1(3), 10);
        Assert.assertEquals(switch1(10), 4);

        Assert.assertEquals(switch2(3), 2);
        Assert.assertEquals(switch2(3), 2);

        Assert.assertEquals(switch3(3), 4);

        Assert.assertEquals(switch4(1), 1);
        Assert.assertEquals(switch4(3), 2);
    }

    public int switch1(int i) {
        switch (i) {
            case 1:
            case 2:
                break;
            case 3:
                i = 10;
                break;
            default:
                i = 4;
        }
        return i;
    }

    public int switch2(int i) {
        switch (i) {
            case 3:
            default:
                i = 2;
        }
        return i;
    }

    public int switch3(int i) {
        switch (i) {
            case 1:
            case 2:
                break;
            case 3:
                i = 10;
            default:
                i = 4;
        }
        return i;
    }

    public int switch4(int i) {
        switch (i) {
            case 1:
                if (i == 1) break;
            default:
                i = 2;
        }
        return i;
    }

}
