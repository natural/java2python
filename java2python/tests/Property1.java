class Property1 {
    int m_foo = 0;

    public int fooProp() {
	return m_foo;
    }

    public void fooProp(int f) {
	m_foo = f;
    }
    public static void main(String[] args) {
	Property1 p = new Property1();
        System.out.println(p.fooProp());
	p.fooProp(1);
        System.out.println(p.fooProp());
    }
}
