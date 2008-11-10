import junit.framework.*;

public class FloatFix extends TestCase {
    public static void main(String[] args) {
        float f = 1.2f;
        Boolean b = (f == 1.2f);
        System.out.println( b.toString().toLowerCase() );
    }

}
