class Ctor1 {
    public int x = 1;
    public String y = null;

    public Ctor1() {
        x = 2;
    }

    public Ctor1(int arg) {
        x = arg;
    }

    public Ctor1(String arg) {
        y = arg;
    }

    public static void main(String[] args) {
        Ctor1 t1 = new Ctor1();
        System.out.println(2 == t1.x ? 1 : 0);

        Ctor1 t2 = new Ctor1(3);
        System.out.println(3 == t2.x ? 1 : 0);

        Ctor1 t3 = new Ctor1("notnull");
        System.out.println("notnull" == t3.y ? 1 : 0);
        System.out.println(1 == t3.x ? 1 : 0);
    }
}
