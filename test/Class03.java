// tests method calling with single argument
class Class03 {
    public int m1(int x) {
        System.out.println(x);
        return x;
    }

    public static void main(String[] args) {
	Class03 c = new Class03();
        System.out.println(c.m1(3));
    }
}
