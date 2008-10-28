interface RainbowColors {
    void make_rgb(int x);
    int roy();
    int g();
    int biv();

    int red = 0;
    int green = 0;
    int blue = 0;

    class Clr {};
}

interface PrintColors {
}


interface LotsOfColors extends RainbowColors, PrintColors {
    int RED = 1;
    int FUCHSIA = 17, VERMILION = 43, CHARTREUSE = RED+90;
}


class InterfaceExtends {
    public static void main(String[] args) {
        System.out.println(LotsOfColors.CHARTREUSE);
        System.out.println(args);
    }
}

