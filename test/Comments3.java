class Comments3 {

    static void bar(int x) {
        System.out.println(x);
    }
        public static void main(String[] args) {
            int foo = 100;
            if (foo < 38) {
                // will never happen
                bar(/* funk */ 0);
            }
            bar(1);
        }
}
