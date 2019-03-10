http
---------------

http is an server-client application protocol built on top of TCP.

if i understand correctly, http is one implementation of such RESTful API.

server has some resources (like a html file), each of which can be addressed uniquely using the URL.  
there are actions defined for the resources: get, post, put and delete.  
a client (such as browser, curl command, etc) can set an action and the resource the action is intented to be act on, 
and send such a reqeust to the server.  
the server (such as apache, nginx, built-in http server in nodejs ) will handle the req accordingly and the send back the response.
 
e.g. if a browser wants to get a html page, it will send a 'get' request to this server (using domain name or ip address) and indicate which resouce it wants (usually it is the path to the file).  
the http server looks at the action and the resource, and then act accordingly.  

note that http server ( and the controller) can do anything to the request.  
it doesn't have to serve file at the 'path' indicated by the reqeust, 
but interprets this 'path' as something that the server knows what to do, like execute a particular function.  
whatever the server does, it needs to returns something to indicate whether it is successful or not, and the returning stuff to the client.

this is a simplification of the reality.  
in the case of apache (http server) + php (controller), 
the apache server knows which php file to execute based on the resource in the request,
and then the control is handled by the php files.  
the php file can do anything subsequently.
it can changes the header, it can server whatever contents it wants,
and then apache will simply forward the reply from the php files to the client.

in the case of django, it is similar.
the whatever built-in http server fowards the whole request to the underlying controller,
which looks at the resource and action and then decides what to do.  
a slight difference compared to apache + php is that apache acts a bit on the resource already, 
as apache already picks which php file to forward the request to.

ultimatley, in the case of apache and php, it is
url --> apache --> php --> (output/render something) --> apache --> (foward this something) --> browser.  
url is like an action + resource, browser is a tool to display whatever returned.
