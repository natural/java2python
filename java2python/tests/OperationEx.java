


public class OperationEx {
        public static void main(String args[]) {
            double x = Double.parseDouble("1.2");
            double y = Double.parseDouble("3.4");
            for (Operation op : Operation.values())
                System.out.printf("%f %s %f = %f%n", x, op, y, op.eval(x, y));
        }
}
