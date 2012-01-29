class Ctor4 {

    public int                                  m_foo;
    public int                                  m_bar;
    


    public Ctor4() {
        this(/* foo */ 0, /* bar */ 0);
    }

    public Ctor4(int p_foo) {
        this(p_foo, 0);

    }
    
    public Ctor4(int p_foo, int p_bar) {
        m_foo = p_foo;
        m_bar = p_bar;
    }
    

    public static void main(String[] args) {
        Ctor4 a = new Ctor4();
        System.out.println(a.m_foo);
        System.out.println(a.m_bar);

        Ctor4 b = new Ctor4(1);
        System.out.println(b.m_foo);
        System.out.println(b.m_bar);


        Ctor4 c = new Ctor4(2, 3);
        System.out.println(c.m_foo);
        System.out.println(c.m_bar);

    }


}
