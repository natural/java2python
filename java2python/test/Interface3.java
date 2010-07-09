interface B0 {
    public void m(int x);
}

interface B1 {
    public void m(int x);
}


interface C0 extends B0, B1 {
    public void n(int y);
}


class Interface3 implements C0 {
    public void m(int x) {
        System.out.println(x);
    }

    public void n(int y) {
        System.out.println(y);
    }

    public static void main(String[] args) {
	Interface3 i = new Interface3();
        i.m(0);
        i.n(1);
    }
}
