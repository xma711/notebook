public class PrintSomething {
	String Something = "print something";

	void print() {
		System.out.println(Something);
	}

	// a main function
	public static void main(String[] args) {
		// declare a new variable, based on the class PrintSomething
		PrintSomething p = new PrintSomething();

		// execute a method
		p.print();
	}
}
