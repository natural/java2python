class Expr {
    public static void main(String[] args) {
	int x = 0;
        System.out.println(x);

	x = 42;
        System.out.println(x);

	x += 33;
        System.out.println(x);

	x -= 21;
        System.out.println(x);

	x *= 17;
        System.out.println(x);

	x /= 4;
        System.out.println(x);

	x &= 3;
        System.out.println(x);

	x = 444;
	x &= 0x0bc;
        System.out.println(x);

	x = 444;
	x |= 0x01;
        System.out.println(x);

	x = 13;
	x %= 5;
        System.out.println(x);

	// TODO:  BIT_SHIFT_RIGHT_ASSIGN thru AND

	x = 3;
	System.out.println(x==3 ? 1 : 0);
	System.out.println(x!=3 ? 1 : 0);

	String y = new String();
        System.out.println(y instanceof String ? "object" : "notobject");

	System.out.println(x <= 0 ? 1 : 0);
	System.out.println(x >= 0 ? 1 : 0);

	// TODO:  BIT_SHIFT_RIGHT

	System.out.println(44 >> 3);
	System.out.println(44 > 3 ? 1 : 0);
	System.out.println(44 << 3);
	System.out.println(44 < 3 ? 1 : 0);

	x = 33;
	System.out.println(x+1);
	System.out.println(x-1);
	System.out.println(x*2);
	System.out.println(x/2);
	System.out.println(x%2);

	x = -33;
	System.out.println(-x);
	System.out.println(+x);

	// NB: these tests side-step the issue of using pre/post inc in
	// expressions
	x = 55;
	++x;
	System.out.println(x);
	--x;
	System.out.println(x);
	x++;
	System.out.println(x);
	x--;
	System.out.println(x);

	x = 55;
	System.out.println(~x);
	System.out.println(!false ? 1 : 0);

	System.out.println( (Integer) x );

    }
}
