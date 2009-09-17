class Switch1 {
    public static void main(String[] args) {
	int x = 1;
	int y = 0;
	switch (x) {
	case 0:
	    y = 0;
	    break;
	case 1:
	    y = 1;
	    break;
	default:
	    y = 3;
	    break;
	}
	System.out.println(y);
    }
}
