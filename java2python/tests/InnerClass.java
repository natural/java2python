
class InnerClass {
    static class StaticInner {
	public static String x = "notnull";
    }

    class NestedInner {
	public String x = "somenull";
    }

    public static void main(String[] args) {
	StaticInner i = new StaticInner();
        System.out.println(i.x);

	InnerClass ic = new InnerClass();

	//TODO: NestedInner n = ic.new NestedInner();
        //TODO: System.out.println(n.x);
    }

}
