class Vector {}

class BasicTypes3 {
    Boolean B;
    Integer I;
    Double D;

    String S;
    Vector V;

    public static void main(String[] args) {
        BasicTypes3 bt3 = new BasicTypes3();
        System.out.println(bt3.B == null ? 1 : 0);
        System.out.println(bt3.I == null ? 1 : 0);
        System.out.println(bt3.D == null ? 1 : 0);
        System.out.println(bt3.S == null ? 1 : 0);
        System.out.println(bt3.V == null ? 1 : 0);
    }

}
