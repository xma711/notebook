Ruby on Rails.
--------------

Reference: book "learn Rails by example / Michael Hartl".

Ruby is a python-like programming language.  

Python has a django web framework.  
Similary, ruby has a Rails web framework.

The whole framework is quit similar to the nodejs experess web framework, 
as it has a controller, a model and a view (html file with ruby scripts).

All the http requests are forwarded to the Rails controlller,
and then based on the resource (route) in the request, it gets/add data from/to model, 
and then render the html file (views).

The output will be sent to the client.

The html file with ruby script is like the html with php case. 
We just have to be careful about the syntax.

But Ruby does have some 'strange' syntax.
Ruby has some special 'symbols'..


Symbols
-------------------

Reference: http://www.troubleshooters.com/codecorn/ruby/symbols.htm

one example:   :myname,  :'string string string'

anyway most symbols looks like a colon followed by a normal variable common in other programming langugages.

Symbols are immutable. cannot do this:  "myname = "steven".  
Question: how to initialize a symbol?   
Answer: there is no such thing as initialize a symbol.. the question wrong assumes that a symbol is a variable (it is not!).  
Or a better way to say is that when the first time we write :mysymbol, it is already initialized and itself is the value.  
What we should do is that x = :mysymbol so that the variable x has the value of ":mysymbol".

A ruby symbol is a thing that has both a number (integer) representation and a string representation.  
Integer representation:  :mysymbol.to_i ; string represention:  :mysymbol.to_s  ;   
by default in ruby, a symbol yields the string representation even without the .to_s conversion.

A symbol is more light-weight than a string class in ruby.. (that is what i understand)  

a symbol is not a raw string like what is in c.  
It is still a class and it has its methods.


Run interactive Ruby
-------------------------
Type command 'irb' in terminal..


Deployment
----------------------

To deploy a rails application, one website that can be used in Heroku.

Heroku is like github. 
Create a repo there, push rails codes to the repo,
and then magically the website for the application is up!
