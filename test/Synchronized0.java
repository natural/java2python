class Synchronized0 {
    private long c1 = 0;
    private long c2 = 0;
    private Object lock1 = new Object();
    private Object lock2 = new Object();


    public void inc1() {
        synchronized(lock1) {
            c1++;
        }
    }

    public void inc2() {
        synchronized(lock1) {
            c2++;
        }
    }

    public static void main(String[] args) {
        Synchronized0 obj = new Synchronized0();
        obj.inc1();
        obj.inc2();
	System.out.println( obj.c1 );
	System.out.println( obj.c2 );
    }
}
