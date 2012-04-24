interface Something {
    public int foo();
}


interface SomethingElse {
    public int foo();
}


class Both implements Something {
    public int foo() {
        return 100;
    }
}

class What extends Both {
    public int foo() {
        return 200;
    }
}


class Cast0 {
    public static void main(String[] args) {
        int x = 33;
        Integer ix = (Integer) x;
        System.out.println(x);
        System.out.println(ix);

        What w = new What();

        System.out.println( w.foo() );

        Both b = (Both) w;

        System.out.println( b.foo() );

    }
}