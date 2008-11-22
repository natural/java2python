class InnerClass {
    public int overriddenMethod() {
	int y = 42;
	System.out.println(y);
	return y;
    }
}


public class CompilerAnnotations extends InnerClass {
    @Deprecated
    static void depMethod() {
	int x =  1;
	System.out.println(x);
    }

    @Override
    public int overriddenMethod() {
	int y = 2;
	System.out.println(y);
	return y;
    }

    @SuppressWarnings("deprecation")
    static void usesDepMethod() {
        depMethod();
        int z = 3;
	System.out.println(z);
    }

    public static void main(String[] args) {
	CompilerAnnotations one = new CompilerAnnotations();
	depMethod();
	one.overriddenMethod();
	usesDepMethod();
    }
}
