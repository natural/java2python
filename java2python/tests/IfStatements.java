class IfStatements {
    public static void main(String[] args) {
	String sa = "before the ifs";
	if (false) {
	    sa = "ouch";
	    if (true) {
		sa = "horray";
	    }
	}
	if (true) {
	    System.out.println(1);
	    System.out.println(2);
	} else {
	    System.out.println(0);
	    System.out.println(-1);
        }
	String sb = "after the ifs";


	int x = 0;
	if (++x > 0) { System.out.println("ok"); }

	int y = 0;
	if ((y+= (y+=(++y))) == 1) { System.out.println("nested expr"); }
    }



}
