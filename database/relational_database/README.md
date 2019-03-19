Join
---------------------

Reference: https://en.wikipedia.org/wiki/Join_(SQL)

join is to match rows from two or more tables and then combine the rows
to a new row, and all new rows to a new table.
(in another words, it is to combine columns...) 

There are outer join and inner join.

Outer join is like a vector cross product.  
(don't care about too much on this cross join. left join and right join are more important.)  
(to learn outer join, better follow this tutorial: www.diffen.com/difference/Inner_Join_vs_Outer_Join)  

rows (a, b, c)^T in table 1 and rows (1,2,3)^T in table 2 will become
(a 1, b 1, c 1, a 2, b 2, c 2, c 1, c 2, c 3)^T in the new table.  
(note that each element in the () like a is a row instead of a column).  
Then user can do a filter to obtain the rows desired.
This may not be as bad as it looks because it won't eliminate any rows accidentally.  
The disadvantage is that it requires a great amount of memory.

Inner join is to use a single command to join tables with matching rows.

When using inner join, be careful when there can be NULL values in the comparing metric (column).
NULL will not be matched to anything, even NULL itself;
so all rows with NULL in the comparing metric will be eliminated,
which may not be desired (depending on the purpose).

E.g. of outer join: SELECT * FROM employee CROSS JOIN department;  
e.g. of inner join: SELECT * FROM employee INNER JOIN department ON employee.DepartmentID = department.DepartmentID;

btw, there is no OUTER JOIN in MySQL.


Normalization
---------------------

When designing a database (inside are multiple tables), we need to normalize them.  
Normalization is a process to find the replicated information in a table and then try to separate them to another table.

We can start from a huge flat table (like spreadsheet) that contains everything we want to have for this database.  
Then we can follow 3 rules to do the normalization.

The first rule is called "first normal form (1NF)".
A relation is in 1NF if and only if the domain (?) of each attribute (column) contains only atomic (indivisable) values,
the the value of each attribute contains only a single value from that domain.  
1NF enforces:  
	- it is to eliminate repeating groups in individual tables;  
	- create a separate table for each set of related data;  
	- and identify each set of related data with a primary key.

One example is here: https://en.wikipedia.org/wiki/First_normal_form  
(not easy to understand what is the boundary for second normal form and third normal form.)

A table is 2NF if it is in 1NF and every non-primary attriabute is dependent on the whole of every candidate key.

A table is 3NF if and only if the table is 2NF (thus 1NF too) and 
every non-primary attribute of table is an attribute that doesn not belong to any candidate key of R..

From stackoverflow: http://stackoverflow.com/questions/723998/what-are-1nf-2nf-and-3nf-in-database-design,  
1NF: each cell in a table must contain only one piece of information, and there can be no duplicate rows.
2NF and 3NF are all about being dependent on the primary key.. 
The primary key can be made up of multiple columns.  
The data depends on the key (1NF), the whole key (2NF) and nothing but the key (3NF)..
