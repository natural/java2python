class Self0 {
	private int v1 = 100;
	public int v2 = 2;

	public int test0(){
		return v2 + v1;
	}

	public boolean test1(){
		return (v1 == v2 || v2 < v1 );
	}

	public static void main(String[] args) {
		Self0 s = new Self0();
		System.out.println(s.test0());
		if(s.test1())
			System.out.println("True");
		else
			System.out.println("False");
                System.out.print("test");
                System.out.print("ing");
                System.out.println();
	}
	
}
