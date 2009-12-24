

class Pair<T, S>{
    private final T first;
    private final S second;

    public Pair(T f, S s) {
        first = f;
        second = s;
    }

    public T getFirst() {
        return first;
    }

    public S getSecond()   {
        return second;
    }

    public String toString()  {
        return "(" + first.toString() + ", " + second.toString() + ")";
    }


}



class GenericPairs {
    public static void main(String[] args) {

	Pair<String, String> first = new Pair<String, String>("hello", "world");
        System.out.println( first.toString() );
    }
}
