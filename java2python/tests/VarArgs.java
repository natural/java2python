class VarArgs {
    public static void show(Objects... objects) {
        for (Object o : objects)
            System.out.println(o + " ");
    }
    public static void main(String[] args) {
	VarArgs.show(1, 2, "three", .5f);
    }
}
