// tests class variable initialization and reference
class Class02 {
    public int w;
    public int x = 1;
    public int y, z = 2;
    public int a = 3, b;

    public static void main(String[] args) {
        Class02 c = new Class02();
        System.out.println(c.w);
        System.out.println(c.x);
	System.out.println(c.y);
	System.out.println(c.z);
	System.out.println(c.a);
	System.out.println(c.b);
        c.b++;
        System.out.println(c.b);
    }
}
