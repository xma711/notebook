why matrix
--------------------------

when solving a pair of 2-unknown linear equations, it is easy by using substitution and subtraction.

what about 3-unknown equations? what about 1 million linear equations?  
using the same method will be extremely tedious and slow.

so, another way is to organize the coefficients into a table, or a matrix, so it looks like:  
M * x = y, where each row of M is the coefficients of one equation involving x1, x2 ... (i.e. the x vector).
of course y is the constants of each equation.  
one example:  
--    --   --  --   --  --
| 1, 2 | * | x1 | = | 10 |
| 3, 4 |   | x2 |   | 20 |
--    --   --  --   --  --
```
then what?

as we look at this matrix M, we can start to think of extracting some properties of M to help us solve the equations.

this is a modularized thinking --> understand matrix in its own right and 
hopefully some knowledge of it will help us solve equations.

in fact it does.  
one example is the determinant.
we know that the n equations for n unknowns must be independent (different story if there are more equations than unknowns).
an easy way to check: the determinant.
as long as the determinant not equal to 0, then we know that there is a solution.

ok great. what else?

look at the matrix equation again M * x = y. 
can we cancel the M away from the left-hand side by cancelling the stuff from the right-hand side, 
all at one go, just like what we usually do in the one single equation?   

it turns out that we can.
we can form a inverse matrix of M: M^(-1),
and then multiply it with each side of the matrix equation: M^(-1) * M * x = M^(-1) * y, which
reduces to x = M^(-1) * y.

now the problem becomes how to find a M^(-1), which is specific to matrix domain.  
there are many ways, and the easiest way is to use a computer.
suddenly in one single step we can solve a million equations at one go!


understand AT * A
--------------------

assume that A is a matrix of data points.
each row is a data point with multiple variables.
for example, var 1 is temperature, and var 2 is humidity, and so on.  
As a result, each column of A is the whole data set for one variable.

now we want to do a AT * A.
how to understand this?

the key point is to ask the following questions:
1. what is meaning of a row in the left-hand side matrix, i.e. AT?  
2. what is the meaning of a column of the right-hand side matrix, i.e. A?  
3. what is the order of meanings of rows from up to down in AT? e.g. temperature, humidity?  
4. what is the order of meanings of columns from left to right in A? 
the reason we ask this is that a matrix multiplication is that the rows of a matrix multiplies the columns of a 2nd matrix.

for A, we alr knew. a column in A is a variable's full data list.  
then AT is the transposed matrix of A, and a row in AT is also a variable's full data list.

this means that each variable's full data list will multiply (or a vector dot product) with any variable's full data list (including itself)
and form a new row.

This means that question 1 and question 2 can be condensed to the same question:
what is the meaning of a row in AT? (and note that it is the same as the meaning of a column in A)

if there is only one variable, e.g. temperature, A is n x 1 matrix, AT is 1 x n matrix,
the result will be 1 x 1 matrix with a single number, that is temperature's variance without being divided by n.

if there is 2 variables (e.g. temperature and humidity), A is n x 2 matrix, AT is 2 x n matrix, the resultant matrix will be 2 x 2.

Okay now can try to answer question 3 and 4.  
the order of meanings of rows in AT is: temperature and humidity. 
this determines orders of meanings of rows in the resultant matrix.
from AT's row order, we know that the each element in the first row of the resultant matrix must have something to do with temperature;
and each element in 2nd row must have something to do with humidity.

and the answer to q4 is exactly the same as the answers for q3.
this determines that for each row in the resultant matrix, 
the order of meanings of each element (in fact, can say each column) has something to do with the order of meanings of columns in A.

Thus, the first row will be all temperature x one variable. 
and the order is determined by the order of columns of A.
the first element in row 1 is the variance of temperature without being divided by n,
the 2nd number in row 1 is the covariance of temperature and humidity.

for 2nd row of the resultant matrix, it must have something to do with humidity.
then we have care about order of the elements in this row, which is again determined by the order of columns in A: temperature and then humidity.  
this means that the first element in 2nd row is not humidity x humidity.
rather, it is humidity x temperature first; and then humidity x humidity.

in fact, all the elements at the diagonal of the resultant matrix are variances (without being divided by n) of each variables.  
and the resultant matrix is symmetric in the sense that the element at (1,2) has the same number as the element at (2,1).  
let's call this matrix C.
so what we meant is that C = CT.

also, when the first row of AT x first column of A, it is a vector dot product.
which means that the first temperature data x the first temperature data + 2nd temp data * 2nd temp data + ... 
there is never a case such that the first temperature data * 2nd temperature data, which is no longer the variance (without being divided by n) of the temperature variable.  
similarly when the first row of AT x 2nd column of A, ie, temperature vector x humidity vector.
so only temperature and humidity from the same data point will multiply with each other and then sum up.

Let xi be the vector of the ith data point (reminder: a vector is a column matrix, n x 1), 
how to represent AT*A in terms of xi?

xiT is a 1 x n matrix. 
xi * xiT is a n x n matrix. 
each element inside the resultant matrix is a variable's observation from the ith data point x a variable's observation from the same data point.   
to understand this result, we also have to ask a similar question: what is a row in xi and what is a column in xiT.  
a row in xi is a single value of a variable; and a column in xiT is exactly the same.
of course we also have to care about the order.  
xi * xiT is actually AT * A is the full data set is just one single point xi. 
(imagine x1 is the only data set collected. AT = x1, A = x1T).  
therefore we can sum up all the xi * xiT to form AT*A.
Thus, AT * A = SUM (xi * xiT).
