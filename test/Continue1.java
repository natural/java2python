class Continue1 {
    public static void main(String[] args) {
        int[] ints = {1, 2, 3, 4, 5, 6, 7};
        for (int x : ints) {
            if (x == 6) {
                break;
            } else if (x == 3) {
                continue;
            }
            System.out.println(x);
        }
    }
}
