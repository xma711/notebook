Json
-------------

JSON stands for 'JavaScript Object Notation'.

Reference: http://www.w3schools.com/json/

example:  
```
{"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]}
```

like xml, json is language independent.


In python
-----------------

Reference: https://docs.python.org/2/library/json.html

the 'json' package can be used to convert dictionary to json, and vice versa.

Example for convert dict to json:   
import json  
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])  
(note that an integer key will become string in json. 
Maybe all the keys will be string in json.)

Example for convert json to dict:  
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')


work with javascript (and html)
-------------------------

Reference: http://www.w3schools.com/json/json_intro.asp

check examples/ex1.html.
