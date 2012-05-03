public class Format {
  public static void main(String[] args) {
    int i = 22;
    String s = "text";
    String r = String.format("> (%d) %s", i, s);

    System.out.println(r);
  }
}
