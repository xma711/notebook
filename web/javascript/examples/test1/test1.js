para1 = document.getElementById("para1");

button1 = document.getElementById("button1");

// after click the button, the text will change
button1.onclick = function() {
	para1.innerHTML="text is changed!";
}


// to make a count down timer
countdown = document.getElementById("count_down");
var countdown_func = function (seconds) {
	var remaining = seconds;
	setTimeout(function() {
			countdown.innerHTML = remaining;
			remaining = remaining - 1;
			// if there is still time remaining, call the function again
			if (remaining > 0) {
				countdown_func(remaining);
			}
		}, 1000
	)
}

timewanted =  5000; //ms
countdown_func(timewanted/1000);

list1 = document.getElementById("list1");

// set the list to hidden first
list1.style.visibility = "hidden";
// after a few seconds, make it appear
setTimeout(function() {list1.style.visibility = "visible";}, timewanted+1000)
