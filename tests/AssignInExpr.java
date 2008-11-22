public class AssignInExpr  {
    public static void main(String[] args) {
        int a = 1, b = 2, c = 3;

        a = b += c;
        System.out.println(b == 5 ? 1 : 0);
        System.out.println(a == 5 ? 1 : 0);

        a = b += c += a;
        System.out.println(c == 8 ? 1 : 0);
        System.out.println(b == 13 ? 1 : 0);
        System.out.println(a == 13 ? 1 : 0);

        a = (b = 1) * (c == 10 ? 1 : 0);
        System.out.println(a == 10 ? 1 : 0);
        System.out.println(b == 1 ? 1 : 0);
        System.out.println(a == 10 ? 1 : 0);

    }

    public void testIf() {
        int a = 4, b = 6, c = 10;

        if ((a +=b) == c) {
            c = 20;
        }
        System.out.println(a == 10 ? 1 : 0);
        System.out.println(b == 6 ? 1 : 0);
        System.out.println(c == 20 ? 1 : 0);
    }

    public void testWhile() {
        int i = 0;

        while (++i < 10) {
            System.out.println(i < 10 ? 1 : 0);
        }
        System.out.println(i == 10 ? 1 : 0);

    }

    public void testDo() {
        int i = 0;
        do {
            System.out.println(i < 10 ? 1 : 0);
        } while (++i < 10);
        System.out.println(i == 10 ? 1 : 0);
    }

    public void testPostIncDec() {
        int i = 0, j = 0, k = 0;
        i = j++;
        System.out.println(i == 0 ? 1 : 0);
        System.out.println(j == 1 ? 1 : 0);

        if (++i == j++) {
            k = 3;
        }
        System.out.println(i == 1 ? 1 : 0);
        System.out.println(j == 2 ? 1 : 0);
        System.out.println(k == 3 ? 1 : 0);
    }

    public void testAndOr() {
        int i = 0, j = 0;

        if (i++ == 1 && j++ == 1) {

        } else {
            System.out.println(i == 1 ? 1 : 0);
            System.out.println(j == 0 ? 1 : 0);
        }

        if (--i != 0 || j-- == 0) {
            System.out.println(i == 0 ? 1 : 0);
            System.out.println(j == -1 ? 1 : 0);
        } else {

        }

    }

}
