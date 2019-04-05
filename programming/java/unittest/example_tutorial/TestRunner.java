
// need to pay attention to the package names; capital letters cannot be written as small letters

// need runClasses method from the JunitCore
import org.junit.runner.JUnitCore;
// need Result class to get the result of test cases
import org.junit.runner.Result;
// need Failure class to get failure(s)
import org.junit.runner.notification.Failure;

public class TestRunner {
	// main function!
	public static void main(String[] args) {
		// again, TestJunit is the unit-test class that tests on the messageUtil class;
		// this line actually runs all the test cases and store the results
		Result result = JUnitCore.runClasses(TestJunit.class);

		// iterate thru the each failure in the results
		for (Failure failure : result.getFailures()) {
			// simply print to console;
			// there should another way to print them to xml files
			System.out.println(failure.toString());
		}
		// print the successful cases
		System.out.println(result.wasSuccessful());
	}
}
