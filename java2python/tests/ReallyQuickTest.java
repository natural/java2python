class ReallyQuickTest {
    public static void main(String[] args) {
	int x;
	String y = new String("asdf");
	System.out.println(y instanceof java.lang.String ? 1 : 0);
	System.out.println(3 >= 3 ? 1 : 0);
	System.out.println(3 > 3 ? 1 : 0);

	System.out.println(3 <= 3 ? 1 : 0);
	System.out.println(3 < 3 ? 1 : 0);

	System.out.println(true && true ? 1 : 0);
	System.out.println(false || true ? 1 : 0);
	System.out.println(3 | 4);
	System.out.println(6 ^ 1);
	System.out.println(6 & 4);
	System.out.println(3 == 4 ? 5 : 6);

	System.out.println( 3 << 4 );
	System.out.println( 32 >> 4 );
	// 1073741820
	System.out.println( -14 >>> 2);

	x = 3;
	++x;
	System.out.println(x);

	--x;
	System.out.println(x);
	System.out.println(x+1);
	System.out.println(x-22);

	System.out.println( 8 / 4 );
	System.out.println( 12 * 4 );
	System.out.println( 12 % 5 );

	x = 1;
	x >>>= 4;
	System.out.println( x );


	x = 10;
	x += 1;
	System.out.println( x );

	x -= 23;
	System.out.println( x );

	x *= 44;
	System.out.println( x );

	x = 16;
	x /= 2;
	System.out.println( x );

	x = 3;
	x &= 2;
	System.out.println( x );

	x = 6;
	x |= 1;
	System.out.println( x );

	x = 3;
	x ^= 2;
	System.out.println( x );

	x = 5;
	x %= 2;
	System.out.println( x );

	x = 3;
	x <<= 4;
	System.out.println( x );

	x = 32;
	x >>= 4;
	System.out.println( x );

	x = 3;
	System.out.println( ~x );

	boolean b = false;
	System.out.println( !b ? 1 : 0 );

	System.out.println( (x) );

    }
}
