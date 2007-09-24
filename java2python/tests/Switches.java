class Switches {
    public static void main(String[] args) {
	System.out.println( switches() );
    }

    public static int switches() {
        int i;
	i = 3;

        switch (i) {
            case 1:
            case 2:
                break;
            case 3:
                i = 2;
            default:
                return -4;
        }

        switch (i) {
            case 3:
            default:
                i = 2;
	}
        return -1;
    }

}

