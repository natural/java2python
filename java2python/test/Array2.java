public class Array2  {
    static Integer a[] = {1, 2, 3};

    void foo(int i) {
        System.out.println( a[i] );
    }

    public static void main(String[] args) {
	Array2 ar = new Array2();
	ar.foo(0);
    }
}
