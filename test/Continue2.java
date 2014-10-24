class Continue2 {
    public static void main(String[] args) {
        int x = 0;
        do {
            System.out.println(x);
            if (x == 6) {
                break;
            } else {
                x += 2;
                continue;
            }
        } while (x < 10);
    }
}
