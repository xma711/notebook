Express in node.js
--------------------

It is a mvc web framework!  
In fact it is much easier to understand than django..

Mvc is model view control.

Control is a single nodejs file, like app.js, which handles all the http requests.  
Nodejs comes with a built-in http server, which forwards all the requests to this control script.  
Then the control script can do whatever it wants.

Model is some kind of representation of data in the database.  
The controller usually has to retrieve data from or add data to the model.

View is actually the html!  
But it is not static, it is a html with places where nodejs codes can be run.  
This is similar to php.  
The codes that can run  inside html file are called "jade".

After controller gets the necessary data from the model, it will render the html file with the data.  
The ultimate html file output will be created from the dynamic one, 
and the the output will be replied to the client.

To make express able to generate an app, install "express-generator",
and then i can use "express" as a command in terminal.  
To generate an app, using: express --view=jade myapp  
after generation, there is a file named package.json listing all the required packages. just use "npm install" (no need other arguments) to install them.

To start the web app: DEBUG=myapp:* npm start (obviously this one includes the debug option).

Structure:  
	- app.js: the Control in the MVC concept; it looks at the request path in the coming url and decide which route file (.js) to handle  
	- routes/ : all the .js files insdie can be used by app.js to handle requests. each file will look at the url again and usually render the corresponding html with jade stuff from the views/ folder  
	- views/ : all the html files with jade stuff . they will be asked to execute and output a final version of html for the corresponding requests.

To link to a javascript file, firstly place the javascript in the public/javascripts/ folder (or subfolder), 
then in the html jade file, write a line to link to the file: script(src="javascripts/test1/test1.js")  

to add a new page, create a new route in app.js, example: app.use('/test', test);  
where the 2nd argument 'test' refers to the test.js in routes/  (because we also added this line to app.js: var test = require('./routes/test');)  
(this actually mean that this test.js can be anywhere as long as app.js can understand.)  

In the routes.test, we need to add  
```
router.get('/', function(req, res, next) {  
  res.render('test', { title: 'creating test page' });  
});
```
question: why is it '/'? not '/test'?   
Answer: each route file see from its own view of the "root directory"; whatever the url is, one app.js direct the request to this file, the path in the url will be come the root for this route file.

Regarding POST, it is not so hard.  
In the html file, create a form with fields with known names. example:  
	input(type="text", name="text_input")  
in the route file (routes/test.js), we can define a post method to the '/' route and handle the req accordingly.  
To get the inputs from client, use: req.body.text_input (where 'text_input' is the name of the field we defined in the form in the html file)


html + jade file
------------------------

Refer to examples to know more.  
E.g. to add an id to an element, one example:   
	p(id="div1") This is a test page  
to add a link to another page, example:  
	a(href="/test") To test page.

Anyway after knowing the core ideas, if anything i don't know, i can just google.


Ejs
-------------------

The alternative to jade is ejs.  
Ejs has the advantage of using almost the raw html contents, which make them easier to understand;  
and easier to translate a designer's html file to a dynamic one with ejs.


Socket.io
-------------

Socket.io allows the html file in the client side and the server to have bidirectionaly communications without having to carry out the whole http req-rsp process.  
It is built on top of websockets (if websockets are available in the browser; if not, they are able to use other underlying technology).  

The whole socket.io thing is like the remove procedure calls (RPC).  
The client or the server can emit an event the other side listens to, 
and the other side will then be doing something.

The whole thing is just like the normal event-listening thing in nodejs, except they are happening remotely.  

Socket.io can be used to pass information around.  
One application is to update part of the html file in the client side without the client having to refresh the webpage.

In that application, i think the process is that:  
client html has listened to an event about the experiment.  
When the server has new information about one experiment, it emits/fires the event with new data.  
The client will get the data and update the local html inside the browser and update the view immediately.

Another application is the chat room. 
One person sends a msg and the rest receives the msg.  
This is done by socket.io, where client emits an event with the new msg,
and then the server receives the msg and the emits another event that all clients listen to.  
Then all clients will receive the msg and then update the local view in the browser.


