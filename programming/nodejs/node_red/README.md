Overview
----------------------

Reference: http://noderedguide.com/

reference for this section: http://noderedguide.com/nr-lecture-1/

node-red is a powerful tool for building internet of things (IoT) applications
with a focus on simplifying the 'writing together' of code blocks to carry out tasks.

It uses a visual programming approach that allows developers to connect predefined code blocks,
known as 'nodes', together to perform a task.  
The connected nodes, usually a combination of input nodes, processing nodes and output nodes,
when wired together, make up a 'flows'.

It has evolved to be a general purpose IoT programming tool.

Node-red is an example of a flow-based programming model - 
messages representing events flow between nodes, triggering processing that results in output.  
The flow-based programming model maps well to typical IoT applications which are characterised by 
real-world events that trigger some sort of processing 
which inturn results in real-world actions.

Node-red offers developers powerful building blocks to allow them to quickly put together flows
that accomplish a lot, 
without having to worry about the programming details.

There is one type of node: function node, 
which allows the developer to quickly write arbitrary javascript.

Node-red excels at rapid application development and at acting as the glue for connecting events to actions, or sensors to actuators.

Shortcomings:  
	- node-red is cumberosme when handling loops.  
	- when an application gets above a certain size, it becomes complex to visually program and manage through node-red.

Although node-red's roots are in the IoT, it is a tool that can be used to build a wide variety of applications.


Install ndoe-red in ubuntu 16.04
--------------------------------------

Reference: https://www.digitalocean.com/community/tutorials/how-to-connect-your-internet-of-things-with-node-red-on-ubuntu-16-04

prerequirements:  
	- install nodejs LTS release: sudo apt-get install nodejs-legacy  
	- install npm: sudo apt-get install npm

now install node-red:  
	sudo npm install -g --unsafe-perm node-red node-red-admin  
	(--unsafe-perm flag helps us avoid some errors that can pop up when npm tries to compile native modules) 

then just run node-red locally:  
node-red

from browser, we can accesss the node-red admin interface in localhost:1880.

If i want to start node-red automatically, then i can create a systemd service file to auto start the admin interface. (not needed for testing)

there is another command called 'node-red-pi', which accepts some memory-saving option to node.js.  
E.g. node-red-pi --max-old-space-size=128 -v

to enable some security, contine to follow the tutorial to setup nginx... (skip here).


Building first flow
-------------------------------

Open node-red admin interface at localhost:1880 in browser.

The main pane is the flow creation workspace in the middle.  
This is where you drag and drop nodes and connect them with wires.  
Along the top of the workspace (i.e. the main pane) is a set of tabs.  
Each tab opens a previously created workspace and shows any flows created using that workspace.

On the left is the node pane that contains all the built-in nodes that your instance of node-red supports.
Nodes are grouped into categories, such as input, output, function.

On the right-hand side is the output pane that can be toggled between the info and debug tabs.  
When info is selected, documentation for the selected node is shown there.  
When debug is selected, it will display the output of debug nodes, errors and warnings.

Above these 3 main panes is the usual toolbar, 
and on the right-hand side are 3 widgets, a deploy button, 
a user info icon and a pulldown menu for admin and control.

The deploy button is used when a flow has been constructed and causes the flow to be deployed onto the node-red system and executed.
For now just treat the deploy button as the way to get the flow running.

Messages pass between nodes, moving from input nodes through processing nodes to output nodes.  
There are 3 main types of nodes:  
1. input nodes (e.g. inject)  
2. output nodes (e.g. debug)  
3. processing nodes (e.g. function)

input nodes allow you to input data into a node-red application or "flow".  
They have at least one output endpoint represented by the small grey square only on their right side. (meaning?)  
You use input nodes to connect data from other services such as twitter, 
or to manaully input data into a flow using the inject node.

Output nodes allow you to send data outside of a node-red flow.  
They have a single input endpoint on their left side. (meaning?)  
You use output nodes to send data to other services, e.g. via twitter or email nodes,
or to use the debug node to output to the debug pane.

Processing nodes allow you to process data.  
They have an input endpoint and one or more output endpoints.  
They allow you to transform the data type (e.g. json, csv) nodes,
use the data to trigger a message (e.g. trigger) nodes 
and to write custom code that uses the data received (e.g. function node).

Inject node has a button to allow you to actuate a node.  
Debug node has a button to allow you to enable and disable a node.

Flow consist of multiple nodes wired together, 
with output tabs linked to input tabs of the next node in the flow.  
Messages flow along the nodes carrying data from node to node.

Node-red nodes consume input messages and produce output messages.  
Messages are javascript objects that contain at least a payload parameter, like:  
```
msg = {
	payload: "message payload"
};
```
nodes consume and produce messages, usually using msg.payload as the main placeholder for the data they consume and produce.  
Messages can be extended to contain other parameters. e.g.  
```
msg = {
	payload: "message payload",
	topic: "error",
	location: "somewhere in space and time"
};
```

general info about nodes
--------------------------------

Reference: http://noderedguide.com/node-red-lecture-5-the-node-red-programming-model/

one important thing is that nodes are self contained and 
typically only interact with other nodes using messages,
you can be sure that they have no unintended side effects and 
so can be safely re-used when you create new flows.  
This 'safe' code reuse is exactly what you are doing each time you drag and drop a node onto your workspace.

Nodes can have at most one input, and 0 or more outputs.

Btw to add a new node type, click "manage palette" in the user settings, 
and in the "install" tab, search the node type name, e.g. "openweathermap",
and then click install.

Note: we can copy and paste nodes and even full flows using the standard cut-and-paste clipboard.  
Node-red flows are simply coded as json strings and can be exported from a workspace,
and imported into a workspace using the node-red pulldown menu in the top right of the node-red window.


Some built-in nodes
--------------------------

Comment node: for adding visible comments into flows.

Inject node: can be used to generate input into a flow. 
The default behaviour for the node is to inject a timestamp.  
The blue dot indicates that the node has not been deployed since it was last changed.  
The grey square is the output point for the node.
This is where you attach 'wires' that route ouptput message from the inject node to the next node in the flow.

Debug node: it is to display the message received by the debug node.  
Btw all message in node-red has 3 default properties: payload, message topic and an internal identifier.
To see all these information, click debug node and configure it to display the full message.

Openweathermap node: allow me to get weather info from openweathermap.org.  
After install these node, there is 2 nodes appeared in the "weather" category. 
Seems one of them is not working..  
Anyway, it needs an api key, which can be obtained after creating an account in openweathermap.org.

Function node: allow us to add customized logic.  
(more details about function node is in the "more about function node" section)

twitter node: allow message to be displayed in a twitter account.. (cool..)

Mqtt node: subscriber to a broker

json node: it parses the incoming message and tries to convert it to/from JSON.
So if you send a JSON string, it will convert it to a javascript object, and vice versa.

Switch node: route a message depending on the incoming message properties.

(actually, node-red is like the simulation tool Arena!)

Change node: allow you to change a message payload or add new properties.
You can use this node to affect the properties in a message, 
either by changing existing ones, deleting them or adding new properties.

Rbe node: i.e. "report by exception", node which only passes on data if it has changed.
You can set it to examine a message payload and either block until a message changes (rbe mode)
or when a message changes by a specified amount (deadband mode).  
E.g. the 1st msg's value is 6, and then the 2nd msg's value is 10. 
Then the rbe node will let the 2nd msg pass (don't know about what will happend to the 1st msg..)

Scale node: allows you to scale (linearly) an input value.
E.g. from (0-10) to (0-255).

Websockets provide a duplex TCP connection and were designed to allow web browsers and servers to maintain a 'backchannel'
that could be used to augment traditional HTTP interactions,
allowing servers to update web pages without the client making a new pull request.

Websocket node: 2 flavours - input and output, allowing you to listen for incoming data (input) or to send (output) on a websocket.  
The output version is designed to check to see if the output payload originated at a websocket in a node,
in which case it responds to the original sender.  
Otherwise it will broadcast the payload to all connected websockets.  
Both input and output websocket nodes can be configured as either server or client - 
in server mode they 'listen on' a URL,
and client mode they connect to a specified IP address.

Tcp request node: can be configured to connect to server and sent a tcp request.
The message to be sent to the server comes from the previous node.
After the tcp node, need a function node to parse the data received in the buffer.  
Note that there is another type of node called "tcp" node, which is different from tcp request node.
Btw inject node 'escapes' the string it uses, causing the return/newline to be removed.
Therefore, to pass a message to the tcp node, use a function node to control the exact message to be passed to the tcp node.


More about function node
-------------------------------

E.g.  
```
if (msg.payload.weather == "Clear") {
	msg.payloaad = "Clear skies ahead today!" // rewrite the msg payload
	return msg;
}
return null; // node-red nodes ignore null messages
```
function node can uses something called context (e.g. local context or global context) to keep some states (e.g. count or sum) in memory.

	
There are some utility functions, such as node.log(), node.warn() and node.error()
which allow us to log text to the console or debug pane (or others) -- this means node-red actually has a console (i think it is like javascript console) 

there is also node.send() function that can be used to send messages to downstream nodes 
in a callback function, rather than returning the message(s). 
This can be used to control time of sending. e.g.
```
// send message after 10s delay
setTimeout( function() {
	node.send(msg);
}, 10000);
return null;
```

in fact, the function node can use the usual javascript/node.js functions.


Subflow
-------------------

Note that there is this concept called subflow.  
Just imagine there is a flow that can be used as if it is one single node in another flow (main flow).  
The former is a subflow of the main flow.

See http://noderedguide.com/node-red-lecture-5-the-node-red-programming-model/ for more details.
