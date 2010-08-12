interface Base {
    int move(int dx, int dy);
}

interface Extra {
}


class Class10 implements Base, Extra {
    public int move(int dx, int dy) {
    return 0;
    }

    public void other(Class10 v) {
    }

    public void other() {
    }

    public static void main(String[] args) {
        Class10 i = new Class10();
        System.out.println(i.getClass().getName());

	for (Class c : i.getClass().getInterfaces()) {
	    System.out.println(c.getName());
	}
    }

}

