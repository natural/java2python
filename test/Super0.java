class Base {
    public int foo(int x) {
        return x + 1;
    }
}

class Super0 extends Base {

    public int foo(int y) {
        int retval = super.foo(y);
        return retval + 1;
    }

    public static void main(String[] args) {

        Super0 x = new Super0();

        System.out.println(x.foo(3));


    }


}