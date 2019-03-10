public class PrintSth {
	String sth = "print something";

	void print() {
		System.out.println(sth);
	}

	// a main function
	public static void main(String[] args) {
		// declare a new variable, based on the class PrintSth
		PrintSth p = new PrintSth();

		// execute a method
		p.print();
	}
}
