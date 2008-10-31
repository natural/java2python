class DoAndWhileStatements {
    public static void main(String[] args) {
	int i = 0;
        do {
            System.out.println(i);
	    i++;
	} while (i < 3);

        int j = 3;
        while (j > 0) {
	    j--;
	    System.out.println(j);
	};

        int x = 0;
        do {
            x++;
	    System.out.println(x);
        } while (x <= 10);

    }
}
