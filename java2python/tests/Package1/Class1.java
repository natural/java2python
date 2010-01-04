package Package1;

public class Class1 {
    public int m() {
	return 42;
    }

    public static void main(String[] args) {
	Package1.Class1 c = new Package1.Class1();
        System.out.println( c.m() );
    }

}

