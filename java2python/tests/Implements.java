interface Base {
}

interface Extra {
}


class Implements implements Base, Extra {
    public static void main(String[] args) {
        Implements i = new Implements();
        System.out.println(i.getClass().getName());

	for (Class c : i.getClass().getInterfaces()) {
	    System.out.println(c.getName());
	}
    }

}

