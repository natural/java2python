class Switch2 {
    public static void main(String[] args) {
	int x = 1;
	int y = 0;
	switch (x) {
	case 0:
	    y = 3;
	    break;
	default:
	    y = 4;
	    break;
	}
	System.out.println(y);
    }
}
