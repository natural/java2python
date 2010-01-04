class Break1 {
    public static void main(String[] args) {
	int x = 0;
	while (x < 10) {
	    if (x == 3) {
		break;
	    }
	    x++;
	    System.out.println(x);
	}
    }
}
