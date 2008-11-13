class Expressions {
    public static void main(String[] args) {
	int x = 42;
	System.out.println(x-x);

	int y = 42, z;
	z = 41;
	System.out.println(y-z);

        x = 4;
	x = x >> 1;
	System.out.println(x);
	System.out.println(x==2 ? 1 : 0);
	System.out.println(x<2 ? 1 : 0);
	System.out.println(x<=2 ? 1 : 0);

        x = 2;
	x = x << 2;
	System.out.println(x);
	System.out.println(x==8 ? 1 : 0);
	System.out.println(x>8 ? 1 : 0);
	System.out.println(x>=8 ? 1 : 0);

	int xa = 0;
        xa += 3;
	System.out.println(xa);

        int xb = 0;
        xb -= 3;
	System.out.println(xb);

        xb *= 3;
	System.out.println(xb);

        int xc = 0;
        xc /= (y+xb+z);
	System.out.println(xc);

        int xd = 5;
	System.out.println(xd & 4);
        xd &= 4;
	System.out.println(xd);

        int xe = 1;
	System.out.println(xe | 2);
	xe |= 2;
	System.out.println(xe);

        int xf = 2;
	System.out.println(xf ^ 4);
	xf ^= 4;
	System.out.println(xf);

	int xg = 15;
	System.out.println(xg % 4);
	xg %= 4;
	System.out.println(xg);
	System.out.println(xg != 3 ? 1 : 0);

	Boolean T=true, F=false;
        System.out.println(T && F ? 1 : 0);
        System.out.println(T || F ? 1 : 0);
        System.out.println(!F ? 1 : 0);

	Integer xh = 3;
	System.out.println((xh instanceof Object) ? 1 : 0);

	System.out.println(xh+3);
	System.out.println(xh-3);
	System.out.println(xh*3);
	System.out.println(xh/3);
	System.out.println(xh%3);

	Integer xi = -3;
	System.out.println(+xh);
	System.out.println(-xh);

	xi = 2;
	System.out.println(~xi);
	System.out.println(!(xi==3) ? 1 : 0);

	/*
	System.out.println(++xi);
	System.out.println(xi++);
	*/

    }
}
