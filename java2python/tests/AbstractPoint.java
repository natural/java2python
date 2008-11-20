abstract class Point {
    int x = 1, y = 1;
    void move(int dx, int dy) {
	x += dx;
	y += dy;
	alert();
    }
    abstract void alert();
}
abstract class ColoredPoint extends Point {
    int color;
}

class AbstractPoint extends Point {
    public static void main(String[] args) {
	Point p = new AbstractPoint();
    }

    void alert() { }
}



