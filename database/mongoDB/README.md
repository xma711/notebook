mongoDB
----------

to access the http interface to mongoDB server, use port number 28017 (not 27017).  
i.e. localhost:28017

to access the mongoDB server from shell, use command "mongo".  
the shell is an interactive javascript shell that is tightly coupled with the mongoDB data structure.

to run a script from host machine, use: mongo script_name.js (in host machine's terminal, not mongo shell), or
go into mongo shell first, then use function load(script_name.js).


"database" in mongo is like database in mysql.  
a "collection" in mongo is like a table in mysql.  
a "document" in a collection in mongo is like a single row of data entry in the table in mysql.  
such one entry in mongo is like a json object { key: value .. }.

in mysql, each table must have the same format - the schema.  
but a collection doesn't have such a schema. 
each document can have their own format, i.e. each document can have different fields (keys).

one field in a document is like a column in the table in mysql.  
of course one field in one document doesn't mean the same field has to appear in another document in the same collection.


find document(s)
-----------------------

the "SELECT" keyword in mysql becomes "collectionObject.find ( options )" function when using javascript.  
the return object from the find() function is a cursor, which is a pointer to the first item found in the database. 
(however, it is not an array, because the data have not been transferred.)  
the options argument in the find() function is a javascript object (like json);  
inside the the options object there can be some keywords ($sth, like $in, $and) to handle some logic relations.  
ultimately, it is to return documents that make the requirements in the options argument TRUE..


update
----------------

one way to update an existing document is to find the document and then use the update() method to update the fields wanted.  
btw, the update() method has a upsert parameter (update and insert). if it is set to true, the input document will be inserted if it is not found in the target collection.

another way is to change the field's value locally, and then use save() method to commit it. 
seems that the 2nd method is more intuitive.


