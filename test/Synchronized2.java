class Synchronized2 {

    public synchronized void test1() {
        System.out.println(1);
    }

    public synchronized void test1(String s) {
        System.out.println(s);
    }

    public static synchronized void test1(int i) {
        System.out.println(i);
    }

    public static synchronized void test2() {
        System.out.println(2);
    }

    public static synchronized void test2(String s) {
        System.out.println(s);
    }

    public synchronized void test2(int i) {
        System.out.println(i);
    }

    public static void main(String[] args) {
        Synchronized2 obj = new Synchronized2();
        obj.test1();
        obj.test1("test1");
        obj.test1(1);
        obj.test2();
        obj.test2("test2");
        obj.test2(2);
    }
}
