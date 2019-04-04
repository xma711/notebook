Understanding
---------------------

Give a set of data points in n-dimensional space 
(ok, let's don't make it so complicated, just say 3 dimensional spaces),
and we want to find out the n new axis that better represent the shape of the data.
These new axis are the principle components of the data set.
(however, these principle components are NOT eigenvectors of data set, 
rather, they are eigenvectors of the covariance matrix. check details later.)

For example, if the shape of the data looks a like a rugby (in certain orientation), 
maybe the data is better not represented by
the usual x, y and z axis, but better represented by the new set of x, y and z axis , 
which are the vector along the longest part of the rugby,
and 2 other directions that are 90 degrees to the first vector.

In the new axis system, each data point has to be transformed, 
by vector producting each point with each axis.
So each point becomes the distance of mapping into the 3 principle components.

One possible such usage is that after getting the 3 principle components, 
we will notice the last one's variance is very small.
This means the data are quite flat in certain direction. 
So maybe we can represent this set 3d data by the 2 most significant components 
(which is not as simple as getting rid of one of the original axis x, y or z).
After transforming the data to the new coordinates, 
we can simply remove the 3rd value in each transformed data point to make it 2d in the "eigenspace".  
Interesting, after transforming them into the original xyz space, it is still 3d.
The intuition is that each principle component is a combination of the original xyz.

One good reference: https://georgemdallas.wordpress.com/2013/10/30/principal-component-analysis-4-dummies-eigenvectors-eigenvalues-and-dimension-reduction/


how to get principle component -> they are the eigenvectors of the covariance matrix of xi!
----------------------------

Given a set of data xi, each xi is a vector with m variables 
(variables are like temperature, humidity in env data, or pixel 1, pixel 2 ... in an image).
There are n data points.

Imagine we have the the first principle component q. 
Mapping of each xi to q is yi = xiT * q. this can be positive or negative.
Then the squared version is y^2 = (xiT * q)^2. 
Sum this term up and take average, it is V = 1/n(SUM(yi^2)) = qT (1/n SUM(xi * xiT)) q.  
Interestingly the covariance C of the data set pops out from this equation, which is C = 1/n SUM(xi * xiT),
and it is a n x n matrix.

Note that the principle component is the principle component of the data set xi, 
not the principle component of the covariance matrix!
The covariance matrix is just an intermediate thing we need.
However, these principle components are the eigenvectors of the covariance matrix,
not the eigenvectors of the data set xi.

There, given a data set xi, the eigenvectors of its covariance matrix C are 
the principle components of xi.

To obtain q, we need to maximize V subject to ||q|| = 1.
(when q is a unit vector, the vector product between xi and q is the real distance of xi on q.)  

After using Lagrange method, we will have Cq = lambda q (which is called ab eigenvector equation), 
where lambda is the eigenvalue of C (not of data set).  
It is a bit confusing that xi disappears.
But it doesn't matter. just remember eigenvectors of C are the principle components of dataset xi.

Anyway after finding out the first principle component, we can try to find the 2nd one, 
which has a constraint of being orthogonal to the first component.

It turns out that Cq2 = lambda2 q2 ,
which is similar to the first eigenvector equation, but now replaced by q2 and lambda 2.

Ultimately, with all eigenvectors and eigenvalues, we will have QT C = A QT,
where Q is m x m matrix with each column = an eigenvector,
and A is the diagonal matrix of lambda, with other elements = 0 except diagonal elements.


PCA algorithm
---------------------

PCA means to find out the principle components of data set xi.

Algorithm 1:  
	1. get mean vector mu of xi (in step 2 we will subtract mu from each xi.)  
	2. computer the covariance matrix C = 1/n SUM( (xi - mu) * (xi - mu)T )  
	3. find out the eigenvectors and eigenvalues of C. or simply say perform eigendecomposition of C, C = Q A QT.

When the value of m (num of dimensions) is too big, while n (number of data points) is smaller,
it is not wise to perform step 2 and step 3,
because step 2 will result in a super big matrix m x m.  

Then what can we do? we follow algorithm 2:  
	1. same as previous  
	2. get matrix A = ((x1 - mu) (x2 - mu) ..), each column is a data point subtracted by mu. in fact, this is the data set in transpose.  
	3. computer a matrix ATA, which is NOT the covariance of data set.  
	4. obtain eigenvectors and eigenvalues of ATA (ATA qj = lambdaj qj). the eigenvectors obtained are NOT the principle components of xi, simply because ATA is not the covariance matrix of xi.  
	5. because A AT A qj = A lambdaj qj and A AT = nC, then nC(Aqj) = lambdaj (A qj), and finally C (A qj) = lambdaj/n (A qj). so eigenvectors of C are A qj and eigenvalues are lambdaj/n.  
	6. since we got the eigenvectors of the covariance matrix of xi, we got the principle components of x.

Therefore algorithm 1 is a general one, which works on any data set.
But it will become very slow if each data point has too many variables (such as an image).

To solve this problem, we calculate the eigenvectors for A AT instead (which is a nxn matrix).
And then transform the eigenvectors of A AT to eigenvectors of C.

Anyway, if m is small, we choose algo 1; if n is small, we choose algo 2.

And yet, there is an algo 3:  
	1 to 2. same as algo 2 step 1 to 2.  
	3. apply the singular value decomposition (SVD) on A: A = U E VT (all we have to know is that there is a method to get U E and V).  
	4. transform U E V to eigenvectors and eigenvalues of C: qj of C = uj in U, and eigenvalues lambdaj of C = sj^2/n for sj in E.


Btw eigenvectors of a random square matrix doesn't have to be orthogonal.  
They are orthogonal because it is a covariance matrix, which has the property that cov = cov.T 


More on the principle components
-------------------------

When we get the principle components of a data set (eigenvectors of the cov matrix), we are still viewing them in the original vector space.  
Otherwise they should be 001 010 100 instead..  

From our project, we know that after getting the eigenvectors, 
each point in the data set (Xi) can be well represented by a linear combination of the eigenvectors.  
If there are more data points (n) than the number of dimensions (m), 
we will have m eigenvectors (Q space).  
In such case, each xi can be represented precisely by a project in the Q space,
i.e. a linear combinations of qi.  

If n is not larger than m, there will be only n-1 eigenvectors.  
In this case, each Xi may not be represented exactly by a linear combination of qi,
but we can still have a projection of Xi in the Q space.  
This can easily proven using an empirical example..  
Give a 3x1 x1 and a 3x3 eigenvectors [q1 q2 q3] (generate this from a symmetric fake cov matrix), 
then i can try to project x1 into the Q2 = [q1 q2] space and get it back,
i.e. y1 = Q2.T * x1; x1_back = Q2 * y1; 
the result x1_back will not be the same as x1.

But anyway, if another object R with similar property as Xi (e.g. R and Xi are both face images),
then R can be represented by a linear combination of Xi;
and because Xi can be represented by a linear combination of qi, 
then R can be represented by a linear combination of qi.   
In short, R = SUM{wi xi} = SUM{ wi (Q yi) } = Q SUM{wi yi} = Qy


Robust PCA
--------------------

To make PCA robust, there are some traditional methods, like trimming, winsorizing ...

One method seems to stand out, which is simply called "Robust PCA".

The problem statement is that  
given a data matrix D, find A and E that solve the problem  
min_A_E rank(A) + lambda ||E||0, s.t. A + E = D.

This means that A has to be low-rank while E has to be sparse.

E.g. D is a set of same pictures with different reflections.  
Using this method we can recover the background picture in A and the reflection of each picture in each row in E.  
In such case, the rank of A is 1. (if not set this extra constraint, the algo will minimize A's rank..)

The problem is difficult to solve because rank(A) and ||E||0 (l0 norm, or the number of non-zero elements in E) are not continuous functions and thus not convex.

One way to change the problem is that we use the nuclear norm of A (sum of singular values after performing SVD on A) to represent the rank of A, 
and the l1-norm (sum of absolute values in E) to represent the l0-norm of E.  
So it is like  
min_A_E ||A||* + lambda ||E||1, s.t. A+E=D.

Now they are convex. they can be solved exactly!

Ultimately, we solve it using Augmented Lagrange multipliers (ALM).  
If the problem can be expressed in a particular equation to be minimized (we call it L(x)), then it can be solved by ALM,
with well-defined steps in an iterative manner (refer to slide 21 of Robust PCA).

Luckily, we are able to express the robust PCA method in this way, using both Lagrange multiplier and a penalty term.  
In each iteration, we need to find A and E once.  
Gladly, how to find A and E are general mathematical problems that have been solved.

We simply have to minimize L(x) wrt E and then minimize it wrt A separately.  
Ultimately we will be able to find E and A in each iteration.

Then just follow ALM to find better E and A after convergence.


However, if E is not sparse, such as reflections on a picture are too large,
we can use fixed-rank robust pca, in which we can fix the rank of A (e.g. 1 if we know so).  
A slightly modified ALM will be performed to find A and E.

On the other hand, for matrix completion (e.g. most rows in D are face images, but some rows in D are full face images with occlusions), 
we can change the algo a bit to deal with this.  
The change is that just keep Eij to be 0, where (i,j) is the element that is NOT missing.  
It is like keeping E sparse while trying to find A, which may not have a low rank (each face can be considered different).
