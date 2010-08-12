@interface AnnoEx {
    String title() default "simple string";
    int value() default 0;
}





@AnnoEx(value=3, title="asdf")
class Anno1 {

    @AnnoEx
    public static void zero() {}

    @AnnoEx(1)
    public static void one() {}

    @AnnoEx(value=2, title="bar")
    public static void two() {}

    public static void main(String[] args) {
        System.out.println("a");
    }


}
