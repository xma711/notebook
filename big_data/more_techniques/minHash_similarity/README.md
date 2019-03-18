Problem to solve
----------------

Given n documents, find which documents are similar.


How
------------------

Map each document to shingles.

Get all the shingles from all documents and reduce them to a unique shingle set.

For each shingle, indicate whether a document has this single (1) or does not have this shingle (0).  
So there will be a table, with first column as the single, the 2nd column as the row id, 3rd as file 1, 4th as file 2 and so on.
Each row is the indication (1 or 0) about whether this document has the shingle.  
For example:
```
shingles	row	file1	file2	file3
s1		1	1	0	1
s2		2	0	0	1
s3		3	1	1	0
s4		4	0	0	1
....
```

Then get a permutation of the row ids (i.e. randomize the row ids) and form a new table.  
Then get the row ids based on the new table for which a file has the first 1.
This is the minhash value!!  
E.g. if the new order is (4 3 1 2) the value for file1 will be 2, that for file2 will be 2, and that for file3 will be 3

do this for some times to form a minhash table. something like:  
```
file1	file2	file3
4	4	3
2	1	2
3	3	1
2	4	4
```

Then partition the table to n bands of k rows.  
We can use different combinations of AND and OR to get the final results.  
E.g. we can get 2 bands, each has 2 rows. and then we do a AND for the rows in each band, and then OR for each band.  
AND means the rows in the band must be all the same to be considered TRUE.  
OR means as long as at least 1 band is the same for 2 files, these two files will considered as similar.  


Some analysis
-----------------------

If two file are 80% similar, and the threshold is 50%, we know the ground truth is that these two files will be similar.  
The probability that these 2 files will be considered as similar by the algorithm with r = 4 (AND), n = 3 (OR) will be:  
P(all r are same) = 0.8^r  
P(all n bands are different) = (1-0.8^r)^n  
P(the 2 files are considered similar) = P (at least one band is same) = 1 - (1-0.8^r)^n which will be a greater than 0.8.  
In fact, the more closer to 1, the better.  
In this case, if these similar files are turned out to be dissimilar, it will be a false negative case.  
The probability will be 1- P(2 files are same) = (1-0.8^r)^n.  

Similarly, if two files are only 10% similar and by the 50% threshold we know they are different.  
The chance that they will be considered similar = 1 - (1-0.1^r)^n, which is false positive.

With different combinations of AND and OR, the formula will be different.  
Just have to do it carefully.  
E.g. if we do a 4 OR first, then 4 AND, then 4 OR, and finally 4 AND, we need 4^4 rows of minhash values.  
Each 4 rows will do a AND, then each 4 bands will do a OR, then each 4  next-level band will do a AND, and each 4 final-level band will do a AND... 
