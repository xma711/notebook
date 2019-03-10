// this file uses event to create an async function for use

var events = require('events')
var eventEmitter = new events.EventEmitter();

var event_name = "event1"

// the primary function that accepts a string argument and a callback function.
// the call back will happen only when the event1 is emitted.
var primary_function = function (string, callback) {
	console.log('primary function is called')
	var listener = function () {
		console.log("listener event fires off.")
		callback(string);
	}
	// btw it seems easier to treat traditional variables (int, string), classes and functions all as variables in nodejs.
	// declare a variable as something and then use them directly

	// add the listener to the event for one time only
	// only when the event happens the listen will happen once
	console.log("add a listen to event1; when event1 happens, the callback will be called once only.")
	eventEmitter.once(event_name, listener)
	//eventEmitter.on(event_name, listener) // when the event buffer has no event, it will exit

}

// call the primary function
primary_function("hello world!", function(str) {console.log(str);} );


// the callback function that will emit the event
var emit_event1 = function() {
	console.log("event1 is emitted.")
	eventEmitter.emit(event_name);
}

// set a timer to emit the event
console.log("set a timer to emit event1 in 3 seconds.")
setTimeout(emit_event1, 3000)

// set another timer
console.log("set another timer event in 5 seconds.")
setTimeout(emit_event1, 5000) // this won't cause another fire-off of the listener in the primary function
