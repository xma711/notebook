javascript
-------------------

reference: book "SAMS teach yourself javascript in 24 hours".  
link: https://smkhaninfotech.files.wordpress.com/2013/10/sams-teach-yourself-javascript-in-24-hours-4th-2007.pdf

html file is used to be a static file.  
there are headers, paragraphs, tables, lists in the html file.
but then that was it. a static file.

javascript is something to make the html file dynamic.  
it can access to each single element (e.g. header, an item in a list) 
and then do something to it.

javascript can change the text in an element, make it disappears and then re-appears,
listens to an event that may happen to an element (like click a button) and then do something to it.

the whole concept is pretty simple.

the reason that javascript can access each element is that the whole html file is transformed to a DOM (Document Object Model) inside the browser.  
it is a hierachical tree representation of a html file.  
with this, javascript is able to get a 'pointer' to each element with a proper name.

each element in the html should set an 'id' if it wants to be accessed individually by javascript.  
the getElementById() is the most common way to access the element.  
other ways to access elements include getElementByClass(), 
which is able to access a list of elements under the same .class name. 
(class is usually used for css to make some makeup for the element group).

to add javascript to a html file, simply uses the <script>...</scrpit> tags.  
we can also write all javascript codes in a file (the recommended way) and include it in the html file under the same tags.


jquery
----------------

jquery is a javascript library that makes many things easier.

e.g. we can do fanciful animation on an element with the jquery lib.  
without it, we need to write a lot of raw javascript codes to achieve the same effects.

the most difficult part here is that jquery uses a somewhat different syntax compared to the raw javascript.  
but the idea is exactly the same: access the element and do something.


ajax
----------------

sometimes we just want to get some small portions of data from the server.  
it will be quite resource-consuming if we do a usual http req-rsp process.  
ajax allows the client to sends a request to the server to get some data,
and then use the data to update the current html file in browser (or more precisely, the DOM).  

note that ajax is mostly one way: client askes for server for something.  
this is unlike the socket.io in nodejs, which allows the server to send info to client too.

with ajax, the html file is more responsive.  
the ajax request can be on the way, but the local view is not frozen and the user can still do something else.


run javascript on command line
---------------------------------

http://stackoverflow.com/questions/2941411/executing-javascript-without-a-browser

Install the libv8-dev package, 
which will provide you Google's V8 engine. 
It has, as one of its examples, 
the file /usr/share/doc/libv8-dev/examples/shell.cc.gz 
which you can uncompress and compile very simply 
(e.g., g++ -Os shell.cc -o shell -lv8).

However, this only allows me to run pure javascript codes.
(in fact, nodejs should run pure javascript codes too.)

to run html with javascript, seems that the best way is to use a browser..


Object
----------------

one way to declare a javascript object is the usual 'class' way..  
declare a constructor first, and then use prototype to add methods to this class.

another way is something like this:
```
var obj = {
	name: "my objects";
	value: 7,
	getValue: function() {return this.value; }
}
```
it is easy to see that this is just a "json" like object. 
but the interesting thing is that the value of the key "getValue" is a function that is able to access other keys..  
this makes it a method in this object while other key value pairs become like class variables..
