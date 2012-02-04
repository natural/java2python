enum Color {
    WHITE(10, 11+3),
	GRAY(20, 22),
	BLACK(30, 33);
    private final int val;

    Color(int v, int x) {
	this.val = v;
    }

    public int code() {
	return val;
    }
}

class Enum0 {
    public static void main(String[] args) {
        System.out.println(Color.WHITE.code());
    }
}
