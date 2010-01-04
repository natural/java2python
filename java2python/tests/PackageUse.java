import Package1.*;

class PackageUse {
    public static void main(String[] args) {
	Package1.Class1 c = new Package1.Class1();
        System.out.println( c.m() );
    }
}
