class VariadicMethod0 {

    public static void show(Object... objects) {
        for (Object o : objects)
            System.out.println(o.toString() + " ");
    }
    public static void main(String[] args) {
	VariadicMethod0.show(0+0, 1, 2, "three", .5f);
    }
}
