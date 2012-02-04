class Comments0 {

    static void bar(int x) {
        System.out.println(x);
    }
        public static void main(String[] args) {
            int foo = 2;
            while (foo > 0 /* what magic is this */) {
                bar(/* funk */ foo);
                foo -= 1;
            }
            bar(1);
        }
}
