// import mqtt
var mqtt = require('mqtt');

// create a client
var client = mqtt.connect('localhost');

// set up the internal callback function
client.on('connect', function() {
		client.subscribe('topic1');
	}
);

client.on('message', function() {
		console.log(message.toString());
	}
	
);

// finally, keep the thread alive
setInterval(function(){}, Math.POSITIVE_INFINITY);
