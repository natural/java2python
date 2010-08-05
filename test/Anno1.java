@interface AnnotationExample {
    int id();
    String title() default "simple string";
}


@AnnotationExample(id=1)
class Anno1 {
    public static void main(String[] args) {
        System.out.println("a");
    }

    @AnnotationExample(id=2, title="test method")
    public static int foo(int a) {
        return 2;
    }
}
