var dns = require('dns');

// one issue here is that how can we know the format of the callback function?
// based on documents but sometimes it is not clear
dns.lookup('google.com', function(err, address, family) {
	console.log("ip address of google.com is: " + address);

	// again, how do i know the callback format is callback(err, hostnames)
	dns.reverse(address, function(err, hostnames) {
		if (!err){
			console.log("hostnames of the ip address are: " + hostnames);
		} else {
			console.log("Encountered error: " + err);
		}
	})
});

// to get the exact APIs, refer to https://nodejs.org/api/
// don't refer to the tutorial http://www.tutorialspoint.com/nodejs/nodejs_dns_module.htm because the descriptions for APIs are not complete

// strangely, there is no method for getServers()
//console.log("dns servers: " + dns.getServers());
