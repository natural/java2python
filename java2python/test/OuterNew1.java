class OuterNew1 {
    class Inner {
        void check() {
            System.out.println(42);
        }
    }

    public static void main(String[] args) {
        OuterNew1 outer = new OuterNew1();
	Inner i = outer.new Inner();
        i.check();
    }

}