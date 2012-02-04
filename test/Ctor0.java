class Ctor0 {

    public int                                  m_foo;
    public int                                  m_bar;
    


    public Ctor0() {
        this(/* foo */ 0, /* bar */ 0);
    }

    public Ctor0(int p_foo) {
        this(p_foo, 0);

    }
    
    public Ctor0(int p_foo, int p_bar) {
        m_foo = p_foo;
        m_bar = p_bar;
    }
    

    public static void main(String[] args) {
        Ctor0 a = new Ctor0();
        System.out.println(a.m_foo);
        System.out.println(a.m_bar);

        Ctor0 b = new Ctor0(1);
        System.out.println(b.m_foo);
        System.out.println(b.m_bar);


        Ctor0 c = new Ctor0(2, 3);
        System.out.println(c.m_foo);
        System.out.println(c.m_bar);

    }


}
