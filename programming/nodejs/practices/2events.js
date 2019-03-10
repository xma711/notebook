// an example to set 2 events and let them emit each other periodically

// import
var events= require('events')

// create an eventEmitter object
// this object handles all the events
var eventEmitter = new events.EventEmitter(); // the allocation looks like c++, while the typeless looks like python

// the implementation of event 1
// to be more generic, event1 function is just one listener to the event "event1"
// we can add another listener function to the event1.
// therefore, event1 is not really the only implementation of event1;
// there could be parallel listeners that can be fired off when event1 happens.
// same for event2
var event1 = function () {
	console.log("in event 1.")
	console.log("now going to to call event 2 in 2 seconds")
	setTimeout(	function() { 
				eventEmitter.emit('event_two');
			},  // first argument is the function
			2000) // second argument is the time duration in ms
	
	
}

// the implementation of event 2
var event2 = function () {
	console.log("in event 2.")
	console.log("now going to to call event 1 in 2 seconds")
	setTimeout(function() {eventEmitter.emit('event_one');}, 
		2000)
}

// bind event1 with the event1 handler/real implementation
eventEmitter.on('event_one', event1);

// bind event2 with the event2 handler/real implementation
eventEmitter.on('event_two', event2);

// "event_one" and "event_two" are two names that have been registered in the eventEmitter object

// fire event1
eventEmitter.emit('event_one'); 
// the funny thing here is that if i type eventEmitter.emit('event1') there won't be any complaints..
// even though there is no such event as "event1" in the eventEmitter object..
// need to pay attention to this type of problem 
