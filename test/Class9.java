class Class9 {
    class Inner {
        void check() {
            System.out.println(42);
        }
    }

    public static void main(String[] args) {
        Class9 outer = new Class9();
	Inner i = outer.new Inner();
        i.check();
    }

}