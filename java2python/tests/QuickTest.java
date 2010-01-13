final class QuickTest extends Object {

    class X {
	int y = 1;
    }

    int i;
    int j = 2;
    static int k;
    static int m = 3;

    public QuickTest(int z) {
	int x = !z;
	System.out.println("quick test ctor");
    }


    public String foo(int... bar) {
//	comment about foo
// wa
	return "placeholder";
    }

    public String bar(int c) {
//	comment about bar
	return "another non-empty string ";
    }


    public static void main(String[] args) {
        System.out.println("Hello, world.");
	QuickTest q = new QuickTest(99);
	q.foo(4, (5), 6, 7, 8);
	q.bar(10);
    }
}
