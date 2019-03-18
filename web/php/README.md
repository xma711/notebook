Basics
------------

Reference: http://www.w3schools.com/php/php_syntax.asp

A PHP script can be placed anywhere in the document.

A PHP script starts with <?php and ends with ?>:

Php syntax is a lot like bash script.  
Just remember that the output will be the html file content.

To run a php script in command line: php -f php_file  
the output will be the html file, which has many html-style markups.  
To see the output content in a better way, one method is to save the outputs to a file
and open it in a browser.

Another way is to use apache2.  
Like the php file with apache2 and browse the file from browser localhost/path_to_file, 
and apache will run the file and return the contents to the browser.


Relation with apache
----------------------------

Apache is the http server. 
In fact, initially apache is called httpd.

The http server serves clients files on the server machines.  
These files can be plain html files (and its associated css javascript files),
or can be html files with php inside.  

If the html file have php inside, apache knows that it should run the php codes first,
and then whatever outputs from the file will be sent over to the client.


How to run php
---------------------

Firstly, php is server side, not client side.

It relies on apache2.

Steps: http://www.allaboutlinux.eu/how-to-run-php-on-ubuntu/

anyway, they are:  
install apache2
got to /var/www/html/ and change index.html to index.php for the easiest case.

Then i can access it from localhost:80


integrate with mysql
-------------------------

Very straightforward. 
Just form the sql command in a string, and then send it using the php sql api.

Ultimately, the most important technique is to know the sql commands.

After send a command to SELECT stuff, the stuff will be returned can be captured by a variable.  
Then there are other apis to loop through each row in the variable. 


GET and POST
--------------------------

For the get and post requests, php codes can access the details from the _GET and _POST global variables (each is an array).

For 'post', it is usually a 'form' in the html file.  
There are some input fields in the html file for user to inputs.
After the user clicks submit, the corresponding php file will be able to access the inputs from the _POST variable. 


Other notes
----------------------

Just remember php is a programming language.  
The php codes can run as multiple small groups inside a html file.  
All these groups inside the same file are actually in the same script so they can access to the same variables etc.  
Ultimately, it makes the html files dynamic in the server side.  
Different final html file will be served based on different requests.

