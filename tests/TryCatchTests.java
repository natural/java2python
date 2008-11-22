class TryCatchTests {
	// this works
	public void tryCatchSimple() {
		try {
			System.out.println("try block");
		} catch (Exception e) {
			System.out.println("catch Exception block");
		}
	}
	
	// this collapse both catch blocks into a single except
	public void tryCatchCompound() {
		try {
			System.out.println("try block");
		} catch (RuntimeException re) {
			System.out.println("catch RuntimeException block");
		} catch (Exception e) {
			System.out.println("catch Exception block");
		}
	}

	// throwing generates broken python
	public void tryCatchThrowSimple() {
		try {
			System.out.println("try block");
		} catch (Exception e) {
			System.out.println("catch Exception block");
			throw e;
		}
	}
	
	// same problem with multiple catches
	public void tryCatchThrowCompound() {
		try {
			System.out.println("try block");
		} catch (RuntimeException re) {
			System.out.println("catch RuntimeException block");
			throw re;
		} catch (Exception e) {
			System.out.println("catch Exception block");
			throw e;
		}
	}
}