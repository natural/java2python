// tests basic class member lookup; python code changes 'x' to 'self.x'
class Class06 {
    int x = 42;

    public void spam() {
        x += 1;
        System.out.println( x );
    };

    public static void main(String[] args) {
        Class06 c = new Class06();
        c.spam();
    }
}