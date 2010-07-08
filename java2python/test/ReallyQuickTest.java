class ReallyQuickTest {
    public int x = 3;

    public setSome(int v) {
        x = v;
    }

    public static void main(String[] args) {
        ReallyQuickTest rqt = new ReallyQuickTest();
        rqt(5);
        System.out.println(rqt.x);
    }
}
