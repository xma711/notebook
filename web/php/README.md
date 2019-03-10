basics
------------

reference: http://www.w3schools.com/php/php_syntax.asp

A PHP script can be placed anywhere in the document.

A PHP script starts with <?php and ends with ?>:

Php syntax is a lot like bash script.  
just remember that the output will be the html file content.

to run a php script in command line: php -f php_file  
the output will be the html file, which has many html-style markups.  
to see the output content in a better way, one method is to save the outputs to a file
and open it in a browser.

another way is to use apache2.  
like the php file with apache2 and browse the file from browser localhost/path_to_file, 
and apache will run the file and return the contents to the browser.


relation with apache
----------------------------

apache is the http server. 
in fact, initially apache is called httpd.

the http server serves clients files on the server machines.  
these files can be plain html files (and its associated css javascript files),
or can be html files with php inside.  

if the html file have php inside, apache knows that it should run the php codes first,
and then whatever outputs from the file will be sent over to the client.


how to run php
---------------------

firstly, php is server side, not client side.

it relies on apache2.

steps: http://www.allaboutlinux.eu/how-to-run-php-on-ubuntu/

anyway, they are:  
install apache2
got to /var/www/html/ and change index.html to index.php for the easiest case.

then i can access it from localhost:80


integrate with mysql
-------------------------

very straightforward. 
just form the sql command in a string, and then send it using the php sql api.

ultimately, the most important technique is to know the sql commands.

after send a command to SELECT stuff, the stuff will be returned can be captured by a variable.  
then there are other apis to loop through each row in the variable. 


GET and POST
--------------------------

for the get and post requests, php codes can access the details from the _GET and _POST global variables (each is an array).

for 'post', it is usually a 'form' in the html file.  
there are some input fields in the html file for user to inputs.
after the user clicks submit, the corresponding php file will be able to access the inputs from the _POST variable. 


other notes
----------------------

just remember php is a programming language.  
the php codes can run as multiple small groups inside a html file.  
all these groups inside the same file are actually in the same script so they can access to the same variables etc.  
ultimately, it makes the html files dynamic in the server side.  
different final html file will be served based on different requests.

