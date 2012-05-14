public class Format0 {
  public static void main(String[] args) {
    int i = 22;
    String s = "text";
    String r = String.format("> (%1$d) %n %2$s", i, s);

    System.out.println(r);
  }
}
