/* This is the unit-testing class to test the MessageUtil class */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestJunit {
	String message = "Hello World";
	MessageUtil messageUtil = new MessageUtil (message);

	// why need to place @Test in front? it is an annotation.
	@Test
	public void testPrintMessage() {
		assertEquals(message, messageUtil.printMessage());
	}
}
