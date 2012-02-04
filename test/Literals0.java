class Literals0 {
    public static void main (String [] args) {

        int h = 0xAA;
        int o = 034;
        float f = .3f;
        double d = .4d;
        long l = 234l;
	char c = 'c';
	String s = "string theory";
	Boolean F = false;
	Boolean T = true;

	Object n = null;

	System.out.println(h);
	System.out.println(o);
	System.out.println(f);
	System.out.println(d);
	System.out.println(l);
	System.out.println(c);
	System.out.println(s);
	System.out.println(T ? 1 : 0);
	System.out.println(F ? 1 : 0);

	System.out.println(n==null ? 1 : 0);
    }
}
