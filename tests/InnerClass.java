class InnerClass {
    static class StaticNestedClass {
    }

    class InnerInnerClass {
    }

    public static void main(String[] args) {
        System.out.println(InnerInnerClass.class.getName());
        System.out.println(int.class.getName());
        System.out.println(void.class.getName());
    }

}
