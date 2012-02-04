public class Array1  {
    static Integer a[] = {1, 2, 3};

    void foo(int i) {
        System.out.println( a[i] );
    }

    public static void main(String[] args) {
	Array1 ar = new Array1();
	ar.foo(0);
    }
}
