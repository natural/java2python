class ForStatements {
    public static void main(String[] args) {
        int z = 0;

	int[] someInts = {0+z, 1, 2};
        for (int i: someInts)
            System.out.println(i);
        for (int j: someInts) {
            System.out.println(j);
        }
        for (int k=0,m=1; k<3; k++) {
            System.out.println(someInts[k]);
        }


            for (;;) { break ; };

        for (int x=32;;) { break; };

        int a, b;

        for(a = 1; a < 10;){
            a+= 3;
	    System.out.println(a);
        }


        for (b = 0; b < 20; b+=2) {
	    System.out.println(b);
        }

        int x = 0;
        for (;;) {
            x ++;
            if (x > 10) break;
        }


    }



}
