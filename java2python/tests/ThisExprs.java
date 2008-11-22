interface None { int x = -2; }

class OuterThis implements None {
    int x = -1;
    int xx = 3;

    public OuterThis (int w) {
	xx = w;
    }

    public OuterThis () {
	xx = 0;
    }


}

class ThisExprs extends OuterThis {
    int x = 0;

    public ThisExprs(int w) {
	super(w);
	x = w;
    }

    public ThisExprs() {
	this(0);
    }


    public static void main(String[] args) {
        ThisExprs init = new ThisExprs();
	init.foo(null);
    }

    void foo(Object other) {
	this.x += 1;
	System.out.println(x);
	System.out.println(this == other ? 1 : 0);
    }

}
