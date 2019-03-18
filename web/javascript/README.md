Javascript
-------------------

Reference: book "SAMS teach yourself javascript in 24 hours".  
Link: https://smkhaninfotech.files.wordpress.com/2013/10/sams-teach-yourself-javascript-in-24-hours-4th-2007.pdf

html file is used to be a static file.  
There are headers, paragraphs, tables, lists in the html file.
But then that was it. a static file.

Javascript is something to make the html file dynamic.  
It can access to each single element (e.g. header, an item in a list) 
and then do something to it.

Javascript can change the text in an element, make it disappears and then re-appears,
listens to an event that may happen to an element (like click a button) and then do something to it.

The whole concept is pretty simple.

The reason that javascript can access each element is that the whole html file is transformed to a DOM (Document Object Model) inside the browser.  
It is a hierachical tree representation of a html file.  
With this, javascript is able to get a 'pointer' to each element with a proper name.

Each element in the html should set an 'id' if it wants to be accessed individually by javascript.  
The getElementById() is the most common way to access the element.  
Other ways to access elements include getElementByClass(), 
which is able to access a list of elements under the same .class name. 
(class is usually used for css to make some makeup for the element group).

To add javascript to a html file, simply uses the <script>...</scrpit> tags.  
We can also write all javascript codes in a file (the recommended way) and include it in the html file under the same tags.


Jquery
----------------

Jquery is a javascript library that makes many things easier.

E.g. we can do fanciful animation on an element with the jquery lib.  
Without it, we need to write a lot of raw javascript codes to achieve the same effects.

The most difficult part here is that jquery uses a somewhat different syntax compared to the raw javascript.  
But the idea is exactly the same: access the element and do something.


Ajax
----------------

Sometimes we just want to get some small portions of data from the server.  
It will be quite resource-consuming if we do a usual http req-rsp process.  
Ajax allows the client to sends a request to the server to get some data,
and then use the data to update the current html file in browser (or more precisely, the DOM).  

Note that ajax is mostly one way: client askes for server for something.  
This is unlike the socket.io in nodejs, which allows the server to send info to client too.

With ajax, the html file is more responsive.  
The ajax request can be on the way, but the local view is not frozen and the user can still do something else.


Run javascript on command line
---------------------------------

Http://stackoverflow.com/questions/2941411/executing-javascript-without-a-browser

Install the libv8-dev package, 
which will provide you Google's V8 engine. 
It has, as one of its examples, 
the file /usr/share/doc/libv8-dev/examples/shell.cc.gz 
which you can uncompress and compile very simply 
(e.g., g++ -Os shell.cc -o shell -lv8).

However, this only allows me to run pure javascript codes.
(in fact, nodejs should run pure javascript codes too.)

To run html with javascript, seems that the best way is to use a browser..


Object
----------------

One way to declare a javascript object is the usual 'class' way..  
Declare a constructor first, and then use prototype to add methods to this class.

Another way is something like this:
```
var obj = {
	name: "my objects";
	value: 7,
	getValue: function() {return this.value; }
}
```
it is easy to see that this is just a "json" like object. 
But the interesting thing is that the value of the key "getValue" is a function that is able to access other keys..  
This makes it a method in this object while other key value pairs become like class variables..
