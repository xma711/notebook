var events= require('events')

// create an eventEmitter object
// this object handles all the events
var eventEmitter = new events.EventEmitter(); // a nested class inside the class events?

// create the first listener function
listener1_to_event1 = function listener1() {
	console.log('listen 1 to event 1 is fired');
}

// create the 2nd listener function
listener2_to_event1 = function listener2() {
	console.log('listen 2 to event 1 is fired');
}

// add the listening functions to the same event1
eventEmitter.addListener('event1', listener1_to_event1)
eventEmitter.addListener('event1', listener2_to_event1)

console.log("after emitting event1, two listeners will be fired off");
eventEmitter.emit('event1')

// get the list of listeners and number of listeners
num_listeners_event1 = events.EventEmitter.listenerCount(eventEmitter, 'event1'); 
// what does this mean? how can i call a function directly in this way?
// it turns out events.EventEmitter.listenerCount is just another independent function in the events.js file;
// it doesn't mean that listenerCount() is a method in events.EventEmitter;
// it is only because the function can be defined by any names, include something.something.something...


console.log("The number of listeners that listen to event1 = " + num_listeners_event1)
