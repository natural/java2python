class Vector {}

class BasicTypes4 {
    boolean b;
    int i;
    double d;

    Boolean B;
    Integer I;
    Double D;

    String S;
    Vector V;

    public static void main(String[] args) {
        BasicTypes4 bt4 = new BasicTypes4();
        System.out.println(bt4.b == null ? 1 : 0);
        System.out.println(bt4.i == null ? 1 : 0);
        System.out.println(bt4.d == null ? 1 : 0);
        System.out.println(bt4.B == null ? 1 : 0);
        System.out.println(bt4.I == null ? 1 : 0);
        System.out.println(bt4.D == null ? 1 : 0);
        System.out.println(bt4.S == null ? 1 : 0);
        System.out.println(bt4.V == null ? 1 : 0);
    }

}
