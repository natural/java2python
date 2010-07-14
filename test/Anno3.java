class Outer {
}

@interface TestAnno {
    int id();
    String title() default "unset";

    public static final int a = 3;

    class Inner {
	private static int a = 4;
	public int bar(String a) {
	    System.out.println(a);
	    return 0;
	}
    }
}

@interface Marker {}

@Marker
@TestAnno(id=1)
class Anno3 {
    public static void main(String[] args) {
        System.out.println("a");
    }

    @TestAnno(id=2, title="test method")
    @Marker public static int foo(int a) {
	System.out.println(a);
	return a;
    }

    @Marker
    public void bar() {
    }
}
