class Expr0 {
    public static void main(String[] args) {
	int x = 0;
	if (x++ == 0) {
	    System.out.println(x);
	}
        System.out.println(x);


	int y = 0;
	if (++y == 1) {
	    System.out.println(y);
	}
        System.out.println(y);


	int z = 0;
	if (--z == -1) {
	    System.out.println(z);
	}
        System.out.println(z);


	int w = 0;
	if (w-- == 0) {
	    System.out.println(w);
	}
        System.out.println(w);


	for (int i = 0; i<3; ++i) {
	    System.out.println(i);
	}

    }
}
