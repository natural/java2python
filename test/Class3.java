// tests method calling with single argument
class Class3 {
    public int m1(int x) {
        System.out.println(x);
        return x;
    }

    public static void main(String[] args) {
	Class3 c = new Class3();
        System.out.println(c.m1(3));
    }
}
