class Vars1 {
    static int a = 1;
    private static int b = 2;
    private int c;

    private void x() {
	System.out.println('x');
    }

    private void y() {
	System.out.println(a);
    }


    private void z(int a) {
	System.out.println(a);
    }
    public static void main(String[] args) {
	System.out.println(a);
	System.out.println(b);

	Vars1 v = new Vars1();
	v.x();
	v.y();
	v.z(3);
    }
}
