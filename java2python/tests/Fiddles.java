class Fiddles {
    public static void main(String[] args) {
	int a = 0, b = 0, c = 0;

	System.out.println(a);
	System.out.println(a++);
	System.out.println(a);
	System.out.println(++a);
	System.out.println(a);

	//if ((b += a += 1) == c) { System.out.println("nested expr"); }
    }
}
