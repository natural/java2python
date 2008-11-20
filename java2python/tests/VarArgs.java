class VarArgs {

    public static void show(Object... objects) {
        for (Object o : objects)
            System.out.println(o.toString() + " ");
    }
    public static void main(String[] args) {
	VarArgs.show(1, 2, "three", .5f);
    }
}
