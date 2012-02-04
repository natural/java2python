class If0 {
    public static void main(String[] args) {
	int x = 0;

	if (x == 0) {
	    System.out.println(0);
	}

	if (x == 0) {
	    System.out.println(1);
	} else {
	    System.out.println("fail");
        }

	if (x == 0) {
	    System.out.println(2);
	} else if (x == 1) {
	    System.out.println("catastrophe");
        } else if (x == 2) {
		System.out.println("error");
        } else {
	    System.out.println("disaster");
        }

    }
}
