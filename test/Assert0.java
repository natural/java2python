class Assert0 {
    public static void main(String[] args) {
	int x = 1;
	assert x>0;
	assert x==1: "not";

	int y = 3;
        try {
	    assert x==0;

	} catch (AssertionError e) {
	    System.out.println(y);
	} catch (IndexOutOfBoundsException e) {
	    System.out.println(y);
        }
    }
}

//	    assert x == 0: y;
