public class ClassInit  {
    static int x = 1;

    static {
        x = 2;
    }
    public static void main(String[] args) {
        assert ClassInit.x == 2;
        System.out.println( ClassInit.x );
    }
}
