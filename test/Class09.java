class Class09 {
    class Inner {
        void check() {
            System.out.println(42);
        }
    }

    public static void main(String[] args) {
        Class09 outer = new Class09();
	Inner i = outer.new Inner();
        i.check();
    }

}