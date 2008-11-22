public class AnonClass {
    public static void main(String[] args) {

	int y = 0;

	test(
	     new Object() {
		 public void haveFrobinated( String e ) {
		     System.out.println(e);
		 }
	     }
	     );



    }

    public static void test(Object o) {
	System.out.println(o);
    }

}
