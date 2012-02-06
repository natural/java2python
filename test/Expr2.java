class Expr2 {
    public static void main(String[] args) {
	int a = 1;
        int b = 2;
        int c = 3;
        int radius = 4;
        int y = (radius*radius*a*(a + radius)*radius*b*b) / (c*c+a*a+b*b);
        System.out.println(y);

    }
}
