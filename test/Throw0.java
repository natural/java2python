class Throw0 {
    public static void main(String[] args) {
        try {
            throw new Exception("some exception message");
        } catch (Exception e) {
	    System.out.println( "caught" );
        }
    }
}
