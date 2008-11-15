public class Switches  {

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

    /*
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
            case 5:
            default:
                i = 2;
        }
        return i;
    }
    */
}
