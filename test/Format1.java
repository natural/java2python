public class Format1 {
  public static void main(String[] args) {
    long n = 461012;
	String f1 = String.format("%d%n", n);      //  -->  "461012"
	String f2 = String.format("%08d%n", n);    //  -->  "00461012"
	String f3 = String.format("%+8d%n", n);    //  -->  " +461012"
	String f4 = String.format("%,8d%n", n);    // -->  " 461,012"
	String f5 = String.format("%+,8d%n", n); //  -->  "+461,012"

	System.out.println(f1 + f2 + f3 + f4 + f5);

	double pi = 3.14159265;
	String pf1 = String.format("%f%n", pi);       // -->  "3.141593"
	String pf2 = String.format("%.3f%n", pi);     // -->  "3.142"
	String pf3 = String.format("%10.3f%n", pi);   // -->  "     3.142"

	System.out.println(pf1 + pf2 + pf3);
  }
}
