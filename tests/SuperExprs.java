interface None { int x = -2; }
class OuterSuper implements None { int x = -1; }

class SuperExprs extends OuterSuper {
    int x = 0;

    public static void main(String[] args) {
        SuperExprs init = new SuperExprs();
        init.foo();
    }

    void foo() {
	System.out.println(SuperExprs.super.x);
    }

}
