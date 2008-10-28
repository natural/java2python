import java.util.*;


public class Card {
    public enum Rank { DEUCE, THREE, FOUR, FIVE, SIX,
	    SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE }

    public enum Suit { CLUBS, DIAMONDS, HEARTS, SPADES }

    public enum Cover { PLAIN (1, 2), FANCY, MODERN(5), SILLY;
	private final int x;
	private final int y;

            Cover () {this.x=0; this.y=1;}
            Cover (int x) {this.x=x; this.y=0;}
            Cover (int x, int y) {this.x=x; this.y=y;}
    }

    public static void main(String[] args) {
        System.out.println(Cover.PLAIN.x);
    }

}


interface Body {
}



enum Planet implements Body {
    MERCURY (3.303e+23, 2.4397e6),
	VENUS   (4.869e+24, 6.0518e6),
	EARTH   (5.976e+24, 6.37814e6),
	MARS    (6.421e+23, 3.3972e6),
	JUPITER (1.9e+27,   7.1492e7),
	SATURN  (5.688e+26, 6.0268e7),
	URANUS  (8.686e+25, 2.5559e7),
	NEPTUNE (1.024e+26, 2.4746e7),
	PLUTO   (1.27e+22,  1.137e6);

    private final double mass;   // in kilograms
    private final double radius; // in meters
    Planet(double mass, double radius) {
        this.mass = mass;
        this.radius = radius;
    }
    public double mass()   { return mass; }
    public double radius() { return radius; }

    // universal gravitational constant  (m3 kg-1 s-2)
    public static final double G = 6.67300E-11;

    public double surfaceGravity() {
        return G * mass / (radius * radius);
    }
    public double surfaceWeight(double otherMass) {
        return otherMass * surfaceGravity();
    }
}
