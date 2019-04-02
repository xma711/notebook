Book
-------------

Sams Teach Yourself SQL in 24 Hours. 5th Edition.


Chapter 2 basic data types
--------------------------------

For string data type, there can be fixed-length string, or varying-length string (e.g. VARCHAR(n) )

VARBINARY can be used to store digital data like image file.

BLOB (data type) is a binary large data, which can be used to store binary media file such as images or MP3s.

TEXT data type is a large character string data type -> like a large VARCHAR filed.

DECIMAL(p,s) is a numeric type. p is the total length allocated. s is the number of digits to the right of the decimal point. 
E.g. for DECIMAL(4,2), the max value allowed is 99.99.

DECIMAL has a better accuracy than float. mysql uses 4 bytes for float and 8 bytes for double.
(https://stackoverflow.com/questions/2160810/mysql-whats-the-difference-between-float-and-double)

Date and Time Types: DATE, TIME, DATATIME, TIMESTAMP

literal string?

NULL value is a missing value or a column in a row of data that has not been assigned a value.

MySQL has a BOOLEAN type. but others may not.

A user-defined type can be created too, using "CREATE TYPE"..

In a field defined as char field, i can still enter numeric values because it can be implicitly converted.


Chapter 3 managing database objects
--------------------------------------

A schema is a collection of database objects (e.g. tables) normally associated with one particular database username.  
The username is called the schema owner.  
E.g. admin creates a user named USER1 with password. Then USER1 creates a table. the schema name for that table is USER1.

Internally, the table name is USER1.table_name. 
When USER1 access his table, he just has to specify "table_name".

Much time and effort should be put into planning table structures before the actual execution of the CREATE TABLE statement.

ALTER can be used to modify a table. just google when needed.

In MySQL, there is a SERIAL type for creating an auto-incrementing column. for other RDBMS, need to google the right name.

Altering or dropping tables can be dangerous. it is better to copy an existing table and do modification in the copied table.  
Command: CREATE TABLE products\_copy\_tbl as SELECT * FROM products\_tbl.

Be specific when dropping a table - specify the owner name of the table!  
(however, i cannot refer body\_info\_copy table as xma.body\_info\_copy. but sgh.body\_info\_copy is okay. this kinda conflicts with the definition of 'schema'...)

You can put a UNIQUE constraint for a column when creating the table, so if you accidentally enter the same number for two different rows, the server will complain.

A foreign key is a column in a child table that references a primary key in the parent table.  
E.g. parent table: EMPLOYEE\_TBL; and child table: EMPLOYEE\_PAY\_TBL. 
When creating the child table with "CONSTRAINT EMP\_ID\_FK FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE\_TBL (EMP\_ID)", 
the foreign key ensures that for every EMP\_ID in the EMPLOYEE\_PAY\_TBL, there is a corresponding EMP\_ID in the EMPLOYEE_TBL table.














