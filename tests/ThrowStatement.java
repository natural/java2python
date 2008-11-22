class ThrowStatement {
    public static void main(String[] args) {
	try {
            throw new IndexOutOfBoundsException("Bad bounds");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
