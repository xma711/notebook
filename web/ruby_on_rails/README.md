Ruby on Rails.
--------------

reference: book "learn Rails by example / Michael Hartl".

ruby is a python-like programming language.  

python has a django web framework.  
similary, ruby has a Rails web framework.

the whole framework is quit similar to the nodejs experess web framework, 
as it has a controller, a model and a view (html file with ruby scripts).

all the http requests are forwarded to the Rails controlller,
and then based on the resource (route) in the request, it gets/add data from/to model, 
and then render the html file (views).

the output will be sent to the client.

the html file with ruby script is like the html with php case. 
we just have to be careful about the syntax.

but Ruby does have some 'strange' syntax.
ruby has some special 'symbols'..


symbols
-------------------

reference: http://www.troubleshooters.com/codecorn/ruby/symbols.htm

one example:   :myname,  :'string string string'

anyway most symbols looks like a colon followed by a normal variable common in other programming langugages.

symbols are immutable. cannot do this:  "myname = "steven".  
question: how to initialize a symbol?   
answer: there is no such thing as initialize a symbol.. the question wrong assumes that a symbol is a variable (it is not!).  
or a better way to say is that when the first time we write :mysymbol, it is already initialized and itself is the value.  
what we should do is that x = :mysymbol so that the variable x has the value of ":mysymbol".

a ruby symbol is a thing that has both a number (integer) representation and a string representation.  
integer representation:  :mysymbol.to_i ; string represention:  :mysymbol.to_s  ;   
by default in ruby, a symbol yields the string representation even without the .to_s conversion.

a symbol is more light-weight than a string class in ruby.. (that is what i understand)  

a symbol is not a raw string like what is in c.  
it is still a class and it has its methods.


run interactive Ruby
-------------------------
type command 'irb' in terminal..


deployment
----------------------

to deploy a rails application, one website that can be used in Heroku.

Heroku is like github. 
create a repo there, push rails codes to the repo,
and then magically the website for the application is up!
