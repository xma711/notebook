- login to mysql:  
	mysql -h HOSTNAME -u user -p  
	e.g. mysql -h localhost -u xma -p

- if password is forgotten, one can log in as root as change the password:  
	SET PASSWORD FOR 'user-name-here'@'hostname-name-here' = PASSWORD('new-password-here');  
	e.g. SET PASSWORD FOR 'xma'@'localhost' = PASSWORD('123456');
 
- check permission for a user: show GRANTS for 'xma'@'localhost';

- list the databases:  
	SHOW databases;

- use the database:  
	USE DATABASE_NAME;

- delete a database:  
	DROP database DATABASE_NAME;

- create a database:  
	CREATE database DATABASE_NAME;

- SHOW tables list in a database:
	SHOW tables;

- see fields in a table:
	
	DESCRIBE TABLE;

- create a table:
	
	e.g. create table simple ( name varchar(30) NOT NULL DEFAULT ' ' );  
which creates a table named simple with one column "name" with string type.
	
	e.g. 
```
	CREATE TABLE IF NOT EXISTS products (
         productID    INT UNSIGNED  NOT NULL AUTO_INCREMENT,
         productCode  CHAR(3)       NOT NULL DEFAULT ' ',
         name         VARCHAR(30)   NOT NULL DEFAULT ' ',
         quantity     INT UNSIGNED  NOT NULL DEFAULT 0,
         price        DECIMAL(7,2)  NOT NULL DEFAULT 99999.99,
         PRIMARY KEY  (productID)
       );
```
- INSERT an entry into a table:
	
	e.g. INSERT into simple values ('hello');
	
	e.g. INSERT into products values (1001, 'PEN', 'Pen Red', 5000, 1.23);
	
	e.g. INSERT INTO products (productCode, name, quantity, price) VALUES ('PEC', 'Pencil 2B', 10000, 0.48);

- SELECT entries from a table:
	
	SELECT * FROM TABLE; (SHOW all entries)
	
	SELECT column1Name, column2Name, ... FROM tableName;
	
	SELECT column1Name, column2Name,... FROM tableName WHERE criteria;
	
	e.g. SELECT * FROM products WHERE productID = 1001;
	
	e.g. SELECT name, price FROM products;
	
	e.g. SELECT name, price FROM products WHERE price < 1.0;
	
	e.g. SELECT * FROM products WHERE productCode = 'PEN';

- using wild card in string matching LIKE and NOT LIKE:

	'abc%' matches strings beginning with 'abc';
	
	'%xyz' matches strings ending with 'xyz';
	
	'%aaa%' matches strings containing 'aaa';
	
	'___' matches strings containing exactly three characters; and
	
	'a_b%' matches strings beginning with 'a', followed by any single character, followed by 'b', followed by zero or more characters.

E.g. SELECT name, price FROM products WHERE name LIKE 'PENCIL%';

- order the results:
	
	e.g. SELECT * FROM products ORDER BY price DESC;
	
	e.g. SELECT * FROM products ORDER BY price ASC; (default is ascending)
	
	e.g Order by price in descending order, followed by quantity in ascending (default) order:
		
		SELECT * FROM products WHERE name LIKE 'Pen %' ORDER BY price DESC, quantity;

- CAUTION: 

	Do not compare FLOATs (real numbers) for equality ('=' or '<>'), as they are not precise. On the other hand, DECIMAL are precise.

- reference: 
	http://www.ntu.edu.sg/home/ehchua/programming/sql/MySQL_Beginner.html
