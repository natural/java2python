class Continue1 {
    public static void main(String[] args) {
        int x = 0;
        while (x < 10) {
            System.out.println(x);
            if (x==6) {
                break ;
            } else {
                x+=2;
                continue ;
            }
    }
    }
}
