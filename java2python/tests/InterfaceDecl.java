interface Foo {
    public void bar(int x);
    public int baz(int y);
}


class InterfaceDecl implements Foo {
    public void bar(int x) {
	System.out.println(x);
    }

    public int baz(int y) {
	return y*2;
    }

    public static void main(String[] args) {
	InterfaceDecl d = new InterfaceDecl();
        System.out.println(d.baz(3));
    }
}
