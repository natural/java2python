enum Vowels {
    A, E, I, O, U, someTimesY;
}

enum LogLevel {
    UNSET, DEBUG(10), INFO(20), WARN(30), ERROR(40),
    CRITICAL(50) {
        int extra = 42;
        public final int extra() { return extra; }
    };
    private final int level;

    LogLevel() {
        this.level = 0;
    }
    LogLevel(int v) {
        this.level = v;
    }
    public int level() { return level; }
}


class EnumMixed {
    public static void main(String[] args) {
        System.out.println(Vowels.A);
        for(Vowels v : Vowels.values())
	    System.out.println(v);
	System.out.println(Vowels.valueOf("A"));
	System.out.println(Vowels.valueOf("E"));
	System.out.println(Vowels.valueOf("I"));
	System.out.println(Vowels.valueOf("O"));
	System.out.println(Vowels.valueOf("U"));
	System.out.println(Vowels.valueOf("someTimesY"));
	System.out.println(LogLevel.DEBUG.level());
    }
}
