// tests inner class instance declaration and creation
class Class4 {
    static class StaticInner {
	public static String x = "notnull";
    }

    int foo = 3;

    class NestedInner {
	public String y = "somenull";
    }

    int bar = 4;

    public static void main(String[] args) {
	Class4 c4 = new Class4();

	StaticInner si = new StaticInner();
        System.out.println(si.x);

	NestedInner ni = c4.new NestedInner();
        System.out.println(ni.y);
    }
}
