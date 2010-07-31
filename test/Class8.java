class Class8 {
    public int one() {
	return 1;
    }

    public void two(int a) {
	if (a>0) {
	    return;
	}
	System.out.println(3);
    }

    public static void main(String[] args) {
        Class8 fm = new Class8();
        System.out.println(fm.one());
        fm.two(123);
    }
}
