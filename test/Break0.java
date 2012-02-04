class Break0 {
    public static void main(String[] args) {
	int x = 0;
	foo:
  	while (x < 10) {
	    if (x == 3) {
		break foo;
	    }
	    x++;
	    System.out.println(x);
	}
    }
}
