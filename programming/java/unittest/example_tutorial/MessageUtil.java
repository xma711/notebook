/*
 * This class prints the given message on console. 
 * this is the class be be tested.
 */

public class MessageUtil {
	private String message;

	//constructor
	//@param message to be printed
	public MessageUtil(String message) {
		this.message = message;
	}

	// prints the message
	public String printMessage() {
		// this function prints and return the same message
		System.out.println(message);
		return this.message;
	}
}
