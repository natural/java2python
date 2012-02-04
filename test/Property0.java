class Property0 {
    int m_bar = 0;

    public int barProp() {
	return m_bar;
    }

    public void barProp(int f) {
	m_bar = f;
    }

    public void barProp(String g) {

    }

    public static void main(String[] args) {
	Property0 p = new Property0();
        System.out.println(p.barProp());
	p.barProp(1);
        System.out.println(p.barProp());
    }
}
