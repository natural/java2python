class Loops {
    public static void main(String[] args) {
	for(int a = 1; a < 10;){
	    a+= 3;
	    System.out.println(a);
	}

	for (int b = 0; b < 20; b+=2) {
	}

	doWhile();
    }

    public static int doWhile() {
	int x = 0;
	do {
	    System.out.println(x);
	    x += 1;
	} while (x <= 10);
        return x;
    }
}

