class Ctor2 {
    public int x = 1;
    public String y = null;

    public Ctor2() {
        x = 2;
    }

    public Ctor2(int arg) {
        x = arg;
    }

    public Ctor2(String arg) {
        y = arg;
    }

    public static void main(String[] args) {
        Ctor2 t1 = new Ctor2();
        System.out.println(t1.x);

        Ctor2 t2 = new Ctor2(3);
        System.out.println(t2.x);

        Ctor2 t3 = new Ctor2("notnull");
        System.out.println(t3.x);
        System.out.println(t3.y);
    }
}
