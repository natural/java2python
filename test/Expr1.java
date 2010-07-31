class Expr1 {
    public static void main(String[] args) {
	int x = 0;
        System.out.println(x);

	// assign
	x = 42;
        System.out.println(x);

	// plus assign
	x += 33;
        System.out.println(x);

        // minus assign
	x -= 21;
        System.out.println(x);

	// star assign
	x *= 17;
        System.out.println(x);

	// div assign
	x /= 4;
        System.out.println(x);

	// and assign
	x &= 3;
        System.out.println(x);


	//  and assign
	x = 444;
	x &= 0x0bc;
        System.out.println(x);

	// or assign
	x = 444;
	x |= 0x01;
        System.out.println(x);

	// mod assign
	x = 13;
	x %= 5;
        System.out.println(x);


	// bit shift right assign
	// shift right assign
	// shift left assign

	// question
	x = 3;
	System.out.println(x==3 ? 1 : 0);
	System.out.println(x!=3 ? 1 : 0);


	String y = new String();
        System.out.println(y instanceof String ? "object" : "notobject");
	System.out.println(x <= 0 ? 1 : 0);
	System.out.println(x >= 0 ? 1 : 0);


	// logical or
	System.out.println(1 < 3 || 3 > 1 ? 1 : 0);

	// logical and
	System.out.println(1 < 3 && 3 > 1 ? 1 : 0);



	// or
	System.out.println(4 | 2);

	// xor
	System.out.println(4 ^ 3);

	// and
	System.out.println(3 & 2);


	// equal
	System.out.println(3 == 3 ? 1 : 0);
	System.out.println(3 == 4 ? 1 : 0);

	// not equal
	System.out.println(3 != 3 ? 1 : 0);
	System.out.println(3 != 4 ? 1 : 0);



	System.out.println(44 >> 3);
	System.out.println(44 > 3 ? 1 : 0);
	System.out.println(44 << 3);
	System.out.println(44 < 3 ? 1 : 0);


	x = 33;
	System.out.println(x+1);
	System.out.println(x-1);
	System.out.println(x*x*x);
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


	x = 7;
	System.out.println(x >>> 1);

    }
}
