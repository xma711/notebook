Http
---------------

Http is an server-client application protocol built on top of TCP.

If i understand correctly, http is one implementation of such RESTful API.

Server has some resources (like a html file), each of which can be addressed uniquely using the URL.  
There are actions defined for the resources: get, post, put and delete.  
A client (such as browser, curl command, etc) can set an action and the resource the action is intented to be act on, 
and send such a reqeust to the server.  
The server (such as apache, nginx, built-in http server in nodejs ) will handle the req accordingly and the send back the response.
 
E.g. if a browser wants to get a html page, it will send a 'get' request to this server (using domain name or ip address) and indicate which resouce it wants (usually it is the path to the file).  
The http server looks at the action and the resource, and then act accordingly.  

Note that http server ( and the controller) can do anything to the request.  
It doesn't have to serve file at the 'path' indicated by the reqeust, 
but interprets this 'path' as something that the server knows what to do, like execute a particular function.  
Whatever the server does, it needs to returns something to indicate whether it is successful or not, and the returning stuff to the client.

This is a simplification of the reality.  
In the case of apache (http server) + php (controller), 
the apache server knows which php file to execute based on the resource in the request,
and then the control is handled by the php files.  
The php file can do anything subsequently.
It can changes the header, it can server whatever contents it wants,
and then apache will simply forward the reply from the php files to the client.

In the case of django, it is similar.
The whatever built-in http server fowards the whole request to the underlying controller,
which looks at the resource and action and then decides what to do.  
A slight difference compared to apache + php is that apache acts a bit on the resource already, 
as apache already picks which php file to forward the request to.

Ultimatley, in the case of apache and php, it is
url --> apache --> php --> (output/render something) --> apache --> (foward this something) --> browser.  
Url is like an action + resource, browser is a tool to display whatever returned.