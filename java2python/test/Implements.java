interface Base {
    int move(int dx, int dy);
}

interface Extra {
}


class Implements implements Base, Extra {
    public int move(int dx, int dy) {
    return 0;
    }

    public static void main(String[] args) {
        Implements i = new Implements();
        System.out.println(i.getClass().getName());

	for (Class c : i.getClass().getInterfaces()) {
	    System.out.println(c.getName());
	}
    }

}

