class Class07 {
    static int a = 1;
    private static int b = 2;
    private int c;

    private void x() {
	System.out.println('x');
    }

    private void y() {
	System.out.println(a);
    }

    private void empty() {
    }

    private void z(int a) {
	System.out.println(a);
    }
    public static void main(String[] args) {
	System.out.println(a);
	System.out.println(b);

	Class07 c = new Class07();
	c.x();
	c.y();
	c.z(3);
    }
}
