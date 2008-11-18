class SynchronizedStatement {
    public static void main(String[] args) {
	Integer a = 1;
	synchronized (a) {
        System.out.println("In sync.");
	}
    }

    public synchronized int check() {
	return 3;
    }

}
