class EmptyClass {}



class Fiddles {
    int x = 1;
    int y = x;


    void A (int k, int z) {
        B(k, z, z);
        C( this.check() +1 );

    }


    void B(int x, int y, int z) {}
    void C(int x) {}

    public static void baz (String v, String [] x) {
	Fiddles z = new Fiddles(3, 4);
    }

    int check() {return (3);}


    public Fiddles(int one, int two) {
        x = one;
        y = two;
        int hex = 0xAA;
        int oct = 034;
        float f = .3f;
        double d = .4d;
        long l = 234l;
	x += 1;
    }
}
