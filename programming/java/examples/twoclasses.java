// first thing learnt: the filenmae can have nothing with the classes inside;
// 2nd thing: one file can have multiple classes. \
// after compile it using javac, different classes will have their own className.java file generated.

// however, if there is a public class, the filename must be the same as the class name, with .java at the end
// public class can be accessed (used?) by another class from another package;
// normal class is private by default and it can be accessed by classes within the same package
// ref about public class: http://stackoverflow.com/questions/16779245/what-is-the-difference-between-public-class-and-just-class

// following is an example

class C1 {
	public void print_hello() {
		System.out.println("hello from c1");
	}
}

class C2 {
        public void print_hello() {
                System.out.println("hello from c2");
        }
}

class C1C2 {
	public static void main(String args[]) {
		C1 obj1 = new C1();
		C2 obj2 = new C2();
		obj1.print_hello();
		obj2.print_hello();
	}
}
