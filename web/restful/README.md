RESTful
------------------

what is restful?

REST stands for REpresentational State Transfer..

read this one: http://www.looah.com/source/view/2284 "How I explained REST to my wife."

anyway, it seems that restful is about applying verbs (get, post, put, delete) on nouns (url, a representation of resource).

another ref: http://stackoverflow.com/questions/671118/what-exactly-is-restful-programming

the actual representation of a resource wanted depends on the client's request: 
use Accept headers to control whether you want XML, HTTP, or even a java object representation (a bit confusing to add HTTP here).

the links between objects are embedded directly in the representation.

another ref: https://www.servage.net/blog/2013/04/08/rest-principles-explained/  
REST itself is not a standard but it prescribes the use of standards such as HTTP, URL and XML/HTML/JPEG..

REST architecture consist of clients and servers.
clients initiate requests to servers who process these requests and return responses based on the requests.  
these requests and responses are built around the transfer of representations of these resources.  
