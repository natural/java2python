class FunctionMethod {
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
        FunctionMethod fm = new FunctionMethod();
        System.out.println(fm.one());
        fm.two(123);
    }
}
