class OuterNew {
    class Inner {
        void check() {
            System.out.println(42);
        }
    }

    public static void main(String[] args) {
        OuterNew outer = new OuterNew();
	Inner i = outer.new Inner();
        i.check();
    }

}