public class ArrayValues  {
    static Integer a[] = {1, 2, 3};

    void foo(int hex) {
        System.out.println( a[0] );
    }

    public static void main(String[] args) {
        Integer b[] = {4, 5, 6};
        System.out.println(a[0].toString());
        System.out.println(a[1].toString());
        System.out.println(a[2].toString());
        System.out.println(b[0].toString());
        System.out.println(b[1].toString());
        System.out.println(b[2].toString());

	Integer[] c;
	c = new Integer[10];
    }
}
