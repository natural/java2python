interface Foo {
    public void bar(int x);
    public int baz(int y);
}


class Interface1 implements Foo {
    public void bar(int x) {
    }

    public int baz(int y) {
	return y;
    }

    public static void main(String[] args) {
	Interface1 d = new Interface1();
        System.out.println(d.baz(3));
    }
}
