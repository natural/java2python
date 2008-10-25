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
	Fiddles z = new Fiddles();
    }

    int check() {return 3;}
}
