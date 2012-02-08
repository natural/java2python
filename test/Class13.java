public class Class13 {

    static int x = 0;
    static int y = Class13.x;

    Class klass = Class13.class;

    public static void main(String[] args) {
        System.out.println(Class13.x == Class13.y ? 1 : 0);
    }

}