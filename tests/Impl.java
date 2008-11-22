interface Base {
}

interface Extra {
}


class Impl implements Base, Extra {
    public static void main(String[] args) {
        System.out.println("ok");
    }

}

