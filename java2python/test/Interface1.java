interface I0 {
    public int m(int x);
}


class Interface1 implements I0 {
    public int m(int y) {
	return y;
    }

    public static void main(String[] args) {
	Interface1 i = new Interface1();
        System.out.println(i.m(3));
    }
}
