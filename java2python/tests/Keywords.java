import junit.framework.*;

public class Keywords extends TestCase {
    public static void main(String[] args) {
        String and = "this is and";
        Assert.assertEquals(and, "this is and");        

        String del = "this is del";
        Assert.assertEquals(del, "this is del");

        String elif = "this is elif";
        Assert.assertEquals(elif, "this is elif");

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
    }
}
