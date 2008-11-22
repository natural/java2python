class InnerNew {
    class InnerType {
        void check() {
            System.out.println(0);
        }
    }

    public static void main(String[] args) {
        InnerNew outer = new InnerNew();
	InnerType i = outer.new InnerType();
        i.check();
    }


}