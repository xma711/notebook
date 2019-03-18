SVM (support vector machine)
-------------------------------

My view: SVM is a linear classifier.

Ultimately it has a linear function of the input data point x (not necessarily on its original form, as it can be mapped to a higher dimension to improve linearity),
whose output is passed in as input to a sign function (at least for 2-classes case).

The problem is that given a set of points (x) and the discrete labels (y) (e.g. 2 classes: 1 and -1),
how to find a hyperplane that can separate the points accordingly to different labels.

Svm solves this problem by finding out the hyperplane that kinda provides the best separation of the points in terms of the distance from points to the hyperplane.

E.g. imagine a set of 2d points that can be drawn on a 2d Cartesian coordinate systems,
and each point belongs to 1 of the 2 classes.
Svm allows us to find a 1d line that separates these points (1d line is a hyperplane in the 2d space).

However, you may ask, if the points by nature cannot be separated cleanly, then how can svm solve this?
E.g. one class of points stays in the centre, occupying a circular area, while other points are scattering around them. 
In this case it is impossible to find a line on the 2d plane to separate them cleanly.  
In fact in this case they are not linear by nature.

There are 2 approaches.  
First one is that we don't mind not separating them cleanly. we just want to find the best line that allow us the chop them to 2 classes even if there could be some points that lie on the wrong side.  
This is the soft svm i think.  
(hard svm is that we need to cleanly classify each point on the training set to its label correctly based on the labels.)

Another approach may be better. it is to map each point to a higher dimensional space.
E.g. if each point has 2 dimensions (x1, x2), we make it to 3 dimensions such as (x1^2, x1x2, x2^2).  
Why do we want to do that?  
Because in higher dimension they could be more linear (based on how we transform them).  
If they are linear in the high-dimension space, it is back to the original problem of finding a hyperplane to classify them.

However, there is another problem. 
If we have to map points to very-high dimension space, the computation could be too complex.  
(the size of wT certainly increases linearly. not sure if this is the main reason that we use kernel method instead.)  
Luckily, kernel method comes to our rescue.


Kernel method
-------------------------

Let phi(x) be the function that maps x into a coordinates in a high-dimension space.  
Then < phi(xi), phi(xj) > is the dot product of the two points in the high-dimension space.  
But what if we can find a simpler function K such that K(xi, xj) has exactly the same result as <phi(xi), phi(xj)>?  
If such function exists, then it is a short cut to compute the dot products in high dimension without having to explicitly visit the high dimension.

In fact, such functions do exist.  they are called kernel functions.
Some even correspond to infinite dimension. 
Imagine if we have to use brute force to map each point to infinite dimension space, it is kinda un-do-able.  
This is called a kernel trick.

But how does svm use kernel function exactly?  
We need to rely on this theorem called Representer Theorem.  
(need to improve this part:)   
instead of optimizing the original cost/error function formed by brute force after promoting x to a high-dimension space ( f(<w, phi(x1)>, ..., <w, phi(xm)> + regularizer ),
the theorem allows us to optimize a function made up of kernel function: 
f( sum_of(aj * K(xj, x1)), sum_of(aj * K(xj, x2)), ... ,  sum_of(aj * K(xj, xm)) ) + regularizer.  
In this case we are finding m unknown aj instead of the original w (m is the number of data points).  
Imagine that if x is mapped to 100000-dimension space, we have to find 100000 wi.  
If m is only 10000, then now we can stick to 10000 aj so it is easier to find aj in this case. 


Kernel method is more than just for svm
-------------------------------------------

Kernel method itself is quite independent from svm.  
It is that svm can use kernel method to simplify its optimization process,
but it doesn't mean svm is the only technique that can use svm.

In fact, other techniques like logistic regression, ridge regression are able to use kernel methods too.


Svm in sklearn package
------------------------

If we use svm directly, it is something like:  
sclf = svm.SVC(gamma = 0.0252, C=10, cache_size = 500, probability = True)

what do C and gamma mean?

C is the penalty parameter in the svm formula (usually in the formula it uses gamma symbol..).  
There C will be needed for whatever kernel function used.  
In fact, C should be there even if there is no kernel function involved.

Gamma is for this particular kernel function: RBF.  
But wait, where is RBF?
By default the svm.SVC() function uses RBF as the kernel function.
Therefore, unless we explicitly changes the kernel function, RBF is used.  
Gamma is a parameter inside this RBF function.  
In other words, if we use another kernel function, then gamma is not needed.

Hard SVM
------------------------

Reference: https://en.wikipedia.org/wiki/Support_vector_machine

If the training data is linearly separable, we can select 2 parallel hyperplanes that separate the 2 classes of data,
so that the distance between them is as large as possible.  
The maximum-margin hyperplane (mm hyperplane) is the one that lies halfway between them.

The equations for the 2 planes can be:  
wx - b = 1 and  
wx - b = -1  
(where the maximum-margin hyperplane is wx - b = 0)  
(and note that w is not unit vector) 

why is it 1 and -1?  
Firstly, the 2 hyperplanes have the same distance to the maximum-margin hyperplane, so it must be k and -k.  
Secondly, we can set it to any k and -k, but we can always transform the 2 equations have 1 and -1 on the RHS by dividing k on both sides of the equations.

The true distance between a hyperplane and the mm hyperplane is not 1, because w and b can be anything.

In fact, the distance between a hyperplane and the mm hyperplane is 1/||w||, 
and that between the 2 hyperplanes (i.e. margin) is 2/||w||.  
Therefore, to maximize the margin, we have to minimize ||w||.

At the same time, we need to link w to the training data points.  
As we already know that in this case the data points are separable, 
then if the w is correctly found, it should achieve:  
w xi - b >= 1 if yi = 1, and   
w xi - b <= -1 if yi = -1

This can be written in a concise way: yi (w xi - b) >= 1.

Therefore, the optimization problem becomes:  
Minimize ||w|| s.t. yi (w xi - b) >= 1


can't remember if there is a close-loop solution for this (likely have),
but it can be solved by stochastic gradient descent.


Soft SVM
-------------------


If the data points are separable, one way to solve this is to use soft svm.

The cost of soft svm has 2 components.

One is that it still wants to minimize the ||w|| (cost 1), which is to maximize the margin.

Wait.. margin of what? it is not separable in this case..

I think it is the distance between 2 hyperplanes beyond which there are supposedly no classification errors (but there are classification errors between the hyperplanes).

If this margin is widen, in this case more points will lie on the wrong size.

So we also want to minimize this case. 
The cost of lying on the wrong side (cost 2) is summarized in one equation:  
1/n SUM( MAX(0, 1 - yi(w xi - b)) ),  
where MAX(0, 1 - yi(w xi - b)) is called the hinge loss function, which is convex (unlike the 0-1 loss function).

Cost 1 and cost 2 are trade-offs.
When reducing cost 2, cost 1 will be increased and vise versa.

Therefore, the optimization function is:  
1/n SUM( MAX(0, 1 - yi(w xi - b)) ) + lambda ||w||  
(i.e. cost 2 + lambda * cost 1)

lambda is something we need to set in the first place.

This optimization problem can be solved by the stochastic gradient descent also.

Btw, another way to see this optimization problem is that we want to minimize cost 2 while having a regularizer in the form of cost 1.  
There must be a link between this margin explanation and the regularizer.


Soft svm and the kernel method
----------------------------------

The natural question to ask is what is the relationship between soft svm (or hard svm) and the kernel method.

The short answer is the kernel method is still based on soft svm but on a higher-dimensional space.

The soft svm optimization function can be transformed to a so-called Primal problem and the Dual problem (they are all equivalent).

The Dual problem is made of dot products of the xi (i.e. dot products of (transformed) data points).  
Kernel method uses the trick that for dot products of high-dimensional data points transformed from the original data points using some methods, 
the results can be obtained in a short cut based on original data points without having to visit the high-dimensional space.
