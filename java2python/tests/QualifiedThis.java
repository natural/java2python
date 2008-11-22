public class QualifiedThis
{
    class Inner {
	public void action() {
	    QualifiedThis.this.check();
	}
    }

    Object o;

    QualifiedThis() {
	Inner o = new Inner();
	o.action();
    }

    public static void main(String[] args) {
	QualifiedThis q = new QualifiedThis();
    }

    void check() {
	System.out.println("checkpoint");
    }


}
