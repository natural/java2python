// tests switches with class attributes

class Switch5 {
    public static final int RT_VOLUME = 48;

    public static String getField( int val) {
        switch( val) {
            case RT_VOLUME:  return "rt volume";
            default:         return "unknown";

        }
    }

    public static void main(String[] args) {
	Switch5 c = new Switch5();
	System.out.println( c.getField(48) );
	System.out.println( c.getField(49) );
    }


}