@interface AnnotationExample {
    int id();
    String title() default "unset";

    public static final int a = 3;

}


@AnnotationExample(id=1)
class Anno1 {
    public static void main(String[] args) {
        System.out.println("a");
    }

    @AnnotationExample(id=2, title="test method")
    public static int foo(int a) {
	System.out.println(a);
	return a;
    }

}
