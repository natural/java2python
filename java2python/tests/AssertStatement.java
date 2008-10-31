class AssertStatement {
    public static void main(String[] args) {
	Boolean v = true, w = false;
        assert v;
        assert (!!v);
        try {
	    assert w : "I am Fail!";
	} catch (AssertionError e) {
	    System.out.println(e.getMessage());
        } catch (Exception f) {
        } finally {
            System.out.println("Finally!");
	}
    }
}
