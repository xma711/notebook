MongoDB
----------

To access the http interface to mongoDB server, use port number 28017 (not 27017).  
I.e. localhost:28017

to access the mongoDB server from shell, use command "mongo".  
The shell is an interactive javascript shell that is tightly coupled with the mongoDB data structure.

To run a script from host machine, use: mongo script_name.js (in host machine's terminal, not mongo shell), or
go into mongo shell first, then use function load(script_name.js).


"database" in mongo is like database in mysql.  
A "collection" in mongo is like a table in mysql.  
A "document" in a collection in mongo is like a single row of data entry in the table in mysql.  
Such one entry in mongo is like a json object { key: value .. }.

In mysql, each table must have the same format - the schema.  
But a collection doesn't have such a schema. 
Each document can have their own format, i.e. each document can have different fields (keys).

One field in a document is like a column in the table in mysql.  
Of course one field in one document doesn't mean the same field has to appear in another document in the same collection.


Find document(s)
-----------------------

The "SELECT" keyword in mysql becomes "collectionObject.find ( options )" function when using javascript.  
The return object from the find() function is a cursor, which is a pointer to the first item found in the database. 
(however, it is not an array, because the data have not been transferred.)  
The options argument in the find() function is a javascript object (like json);  
inside the the options object there can be some keywords ($something, like $in, $and) to handle some logic relations.  
Ultimately, it is to return documents that make the requirements in the options argument TRUE..


Update
----------------

One way to update an existing document is to find the document and then use the update() method to update the fields wanted.  
Btw, the update() method has a upsert parameter (update and insert). if it is set to true, the input document will be inserted if it is not found in the target collection.

Another way is to change the field's value locally, and then use save() method to commit it. 
Seems that the 2nd method is more intuitive.


