class Synchronized1 {

    public synchronized void run() {
	System.out.println(0);
    }

    public static synchronized void class_run() {
	System.out.println(0);
    }

    public static void main(String[] args) {
        Synchronized1 obj = new Synchronized1();
        obj.run();
        obj.class_run();

    }
}
