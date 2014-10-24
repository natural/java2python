import java.io.IOException;

class Exception0 {
    static void test() throws IOException {
        throw new IOException("test");
    }

    public static void main(String[] args) {
        try {
            test();
        } catch (IOException e) {
            System.out.println("catch");
        } finally {
            System.out.println("done");
        }
    }
}
