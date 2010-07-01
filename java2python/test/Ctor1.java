class Ctor1 {

    public Ctor1() {
        System.out.println("Ctor1()");
    }

    public Ctor1(int arg) {
        System.out.println("Ctor1(int)");
    }

    public Ctor1(String arg) {
        System.out.println("Ctor1(String)");
    }

    public static void main(String[] args) {
        Ctor1 t1 = new Ctor1();
        Ctor1 t2 = new Ctor1(3);
        Ctor1 t3 = new Ctor1("notnull");
    }
}

