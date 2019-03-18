Why matrix
--------------------------

When solving a pair of 2-unknown linear equations, it is easy by using substitution and subtraction.

What about 3-unknown equations? what about 1 million linear equations?  
Using the same method will be extremely tedious and slow.

So, another way is to organize the coefficients into a table, or a matrix, so it looks like:  
M * x = y, where each row of M is the coefficients of one equation involving x1, x2 ... (i.e. the x vector).
Of course y is the constants of each equation.  
One example:  
--    --   --  --   --  --
| 1, 2 | * | x1 | = | 10 |
| 3, 4 |   | x2 |   | 20 |
--    --   --  --   --  --
```
then what?

As we look at this matrix M, we can start to think of extracting some properties of M to help us solve the equations.

This is a modularized thinking --> understand matrix in its own right and 
hopefully some knowledge of it will help us solve equations.

In fact it does.  
One example is the determinant.
We know that the n equations for n unknowns must be independent (different story if there are more equations than unknowns).
An easy way to check: the determinant.
As long as the determinant not equal to 0, then we know that there is a solution.

Ok great. what else?

Look at the matrix equation again M * x = y. 
Can we cancel the M away from the left-hand side by cancelling the stuff from the right-hand side, 
all at one go, just like what we usually do in the one single equation?   

It turns out that we can.
We can form a inverse matrix of M: M^(-1),
and then multiply it with each side of the matrix equation: M^(-1) * M * x = M^(-1) * y, which
reduces to x = M^(-1) * y.

Now the problem becomes how to find a M^(-1), which is specific to matrix domain.  
There are many ways, and the easiest way is to use a computer.
Suddenly in one single step we can solve a million equations at one go!


Understand AT * A
--------------------

Assume that A is a matrix of data points.
Each row is a data point with multiple variables.
For example, var 1 is temperature, and var 2 is humidity, and so on.  
As a result, each column of A is the whole data set for one variable.

Now we want to do a AT * A.
How to understand this?

The key point is to ask the following questions:
1. what is meaning of a row in the left-hand side matrix, i.e. AT?  
2. what is the meaning of a column of the right-hand side matrix, i.e. A?  
3. what is the order of meanings of rows from up to down in AT? e.g. temperature, humidity?  
4. what is the order of meanings of columns from left to right in A? 
The reason we ask this is that a matrix multiplication is that the rows of a matrix multiplies the columns of a 2nd matrix.

For A, we alr knew. a column in A is a variable's full data list.  
Then AT is the transposed matrix of A, and a row in AT is also a variable's full data list.

This means that each variable's full data list will multiply (or a vector dot product) with any variable's full data list (including itself)
and form a new row.

This means that question 1 and question 2 can be condensed to the same question:
what is the meaning of a row in AT? (and note that it is the same as the meaning of a column in A)

if there is only one variable, e.g. temperature, A is n x 1 matrix, AT is 1 x n matrix,
the result will be 1 x 1 matrix with a single number, that is temperature's variance without being divided by n.

If there is 2 variables (e.g. temperature and humidity), A is n x 2 matrix, AT is 2 x n matrix, the resultant matrix will be 2 x 2.

Okay now can try to answer question 3 and 4.  
The order of meanings of rows in AT is: temperature and humidity. 
This determines orders of meanings of rows in the resultant matrix.
From AT's row order, we know that the each element in the first row of the resultant matrix must have something to do with temperature;
and each element in 2nd row must have something to do with humidity.

And the answer to q4 is exactly the same as the answers for q3.
This determines that for each row in the resultant matrix, 
the order of meanings of each element (in fact, can say each column) has something to do with the order of meanings of columns in A.

Thus, the first row will be all temperature x one variable. 
And the order is determined by the order of columns of A.
The first element in row 1 is the variance of temperature without being divided by n,
the 2nd number in row 1 is the covariance of temperature and humidity.

For 2nd row of the resultant matrix, it must have something to do with humidity.
Then we have care about order of the elements in this row, which is again determined by the order of columns in A: temperature and then humidity.  
This means that the first element in 2nd row is not humidity x humidity.
Rather, it is humidity x temperature first; and then humidity x humidity.

In fact, all the elements at the diagonal of the resultant matrix are variances (without being divided by n) of each variables.  
And the resultant matrix is symmetric in the sense that the element at (1,2) has the same number as the element at (2,1).  
Let's call this matrix C.
So what we meant is that C = CT.

Also, when the first row of AT x first column of A, it is a vector dot product.
Which means that the first temperature data x the first temperature data + 2nd temp data * 2nd temp data + ... 
There is never a case such that the first temperature data * 2nd temperature data, which is no longer the variance (without being divided by n) of the temperature variable.  
Similarly when the first row of AT x 2nd column of A, ie, temperature vector x humidity vector.
So only temperature and humidity from the same data point will multiply with each other and then sum up.

Let xi be the vector of the ith data point (reminder: a vector is a column matrix, n x 1), 
how to represent AT*A in terms of xi?

XiT is a 1 x n matrix. 
Xi * xiT is a n x n matrix. 
Each element inside the resultant matrix is a variable's observation from the ith data point x a variable's observation from the same data point.   
To understand this result, we also have to ask a similar question: what is a row in xi and what is a column in xiT.  
A row in xi is a single value of a variable; and a column in xiT is exactly the same.
Of course we also have to care about the order.  
Xi * xiT is actually AT * A is the full data set is just one single point xi. 
(imagine x1 is the only data set collected. AT = x1, A = x1T).  
Therefore we can sum up all the xi * xiT to form AT*A.
Thus, AT * A = SUM (xi * xiT).
