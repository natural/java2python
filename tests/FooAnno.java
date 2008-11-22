import static java.lang.Math.PI;



public class FooAnno {
    @Test public static void m1() { }
    public static void m2() { }
    @Test public static void m3() {
        throw new RuntimeException("Boom");
    }
    public static void m4() { }
    @Test public static void m5() { }
    public static void m6() { }
    @Test public static void m7() {
        throw new RuntimeException("Crash");
    }
    public static void m8() { }



    @RequestForEnhancement(
        id = 2868724,
        synopsis = "Enable time-travel",
        engineer = "Mr. Peabody",
        date = "4/1/3007"
    )
    public static void travelThroughTime(Date destination) { }




}



public @interface Preliminary { }


@Preliminary public class TimeTravel { }


