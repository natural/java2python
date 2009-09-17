enum Color {
    WHITE(255, 0),
	GRAY(127, 1),
	BLACK(0, 2);
    private final int val;

    Color(int v, int x) {
	this.val = v;
    }

    public int code() {
	return val;
    }
}

class Enum2 {
    public static void main(String[] args) {
        System.out.println(Color.WHITE.code());
    }
}
