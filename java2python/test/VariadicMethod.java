class VariadicMethod {

    public static void show(Object... objects) {
        for (Object o : objects)
            System.out.println(o.toString() + " ");
    }
    public static void main(String[] args) {
	VariadicMethod.show(1, 2, "three", .5f);
    }
}
