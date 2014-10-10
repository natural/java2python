public class Class15 {

    static Test X = new Test();

    public static void main(String[] args) {
        System.out.println(X.Y);
    }

    static class Test {
        int Y = 42;
    }

}
