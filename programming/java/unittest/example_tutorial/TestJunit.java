/* This is the unit-testing class to test the MessageUtil class */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestJunit {
	// no need to put private???
	String message = "Hello World";
	MessageUtil messageUtil = new MessageUtil (message);

	// why need to place @Test in front?
	@Test
	public void testPrintMessage() {
		assertEquals(message, messageUtil.printMessage());
	}
}
