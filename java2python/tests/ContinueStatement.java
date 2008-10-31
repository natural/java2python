class ContinueStatement {
    public static void main(String[] args) {
	outer: for (int i=0; i<3; i++) {

            inner: for (int j=0; j<3; j++) {
		System.out.println(i);
		System.out.println(j);
		if (i==1) {continue outer; };


	    }
        }
    }
}
