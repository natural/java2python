import junit.framework.*;

public class Keywords extends TestCase {
    public static String None = "this is None";
    public static String and = "this is and";

    public void runTest() {
	String and = "this is and";
	Assert.assertEquals(and, "this is and");
	Assert.assertEquals(Keywords.and, "this is and");

	String del = "this is del";
	Assert.assertEquals(del, "this is del");

	String elif = "this is elif";
	Assert.assertEquals(elif, "this is elif");

	String from = "this is from";
	Assert.assertEquals(from, "this is from");

	String in = "this is in";
	Assert.assertEquals(in, "this is in");

	String is = "this is is";
	Assert.assertEquals(is, "this is is");

	String not = "this is not";
	Assert.assertEquals(not, "this is not");

	String or = "this is or";
	Assert.assertEquals(or, "this is or");

	String print = "this is print";
	Assert.assertEquals(print, "this is print");

	String str = "this is str";
	Assert.assertEquals(str, "this is str");

	String None = "this is None";
	Assert.assertEquals(None, "this is None");
	Assert.assertEquals(Keywords.None, "this is None");

    }

    public static void main(String[] args) {
	Keywords k = new Keywords();
	k.runTest();
        System.out.println("Complete.");
    }


}
