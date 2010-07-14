interface Eggs {
    public void bar(int x);
}


interface Ham extends Eggs {
    public void baz(int y);
}


class Interface2 implements Ham {
    public void bar(int x) {
        System.out.println(x);
    }

    public void baz(int y) {
        System.out.println(y);
    }

    public static void main(String[] args) {
	Interface2 d = new Interface2();
        d.bar(0);
        d.baz(1);
    }
}
