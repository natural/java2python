public class AnonTest {
    public static void main(String[] args) {

	int y = 0;

	test(
	     new Frobinator() {
		 public void haveFrobinated( FrobEvent e ) {
		     otherAction();
		 }
	     }
	     );



    }

    public static void test(Object o) {
	System.out.println(o);
    }

}
