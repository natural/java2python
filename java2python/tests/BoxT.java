/**
 * This version introduces a generic method.
 */
public class BoxT<T> {

    private T t;

    public void add(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }

    public <U> void inspect(U u){
        System.out.println("T: " + t.getClass().getName());
        System.out.println("U: " + u.getClass().getName());
    }

    public static void main(String[] args) {
        BoxT<Integer> integerBox = new BoxT<Integer>();
        integerBox.add(new Integer(10));
        integerBox.inspect("some text");
    }
}
