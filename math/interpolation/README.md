Interpolation
---------------------------

Given a set of points, we want to find a model that passes thru all these points.

Unlike approximation which requires the model to stay as close as possible to the points,
interpolation requires the model to pass thru all the points.

E.g. given a set of (xi, yi), using approximation, we may try to find a linear model y = ax + b to fit these points.  
There are more points than the number of unknowns (a, b), so we just find the best fit.  
The model obtained obviously cannot pass thru all the points if at first the points are not on the same line.

For interpolation, it is different. 
In the same example, we have to find a curve that passes thru all the points.

The easiest (not the best) method is to use a polynomial function, 
such as y = a1 x^3 + a2 x^2 + a1 x + a0  if there are exactly 4 points.  
Then we can sovle the unknowns exactly. 
It is not hard to see the obtained model will pass thru all the points.

What is the disadvantage of this method? 
	--> (need to find out more)

another easy method is called Lagrange interpolation.  
Given a set of (xi, yi), we need to form a model y = y1 L1(x) + y2 L2(x) + y3 L3(x) ..
Such that L1(x1) = 1 and for other xi L1(xi) = 0, and similar for L2, L3, Li...  
It is easy to see that if such conditions meet, then y will always equal to yi when x = xi.  
One way to form L1 is L1(x) = { (x-x2)(x-x3)(x-x4)... } / { (x1-x2)(x1-x3)(x1-x4)... } 
so that L1(x) | x=x1 = 1 and L1(x) | x = other xi = 0..  
Similar for L2, L3 ... each of which is a different function but is similar.  
In short, Li(x) = { (x-x2)(x-x3)...( x-x_{i-1} )( x-x_{i+1} )... } / { (xi-x2)(xi-x3)(xi-x4)... } 


above methods are global; applying one function to all points..  
There are other methods that use piecewise interpolation.  
E.g. for every neighbouring 2 points, i fit a line or curve to it. 
Then the whole model is connected by these small lines or curves.  
For some easy methods, the curve may not be smooth enough because the dy/dx at xi may not equal from one small curve to another.

One method to allow the overall curve is smooth is called cubic spline (also a piecewise interpolation). 


Cubic spline
---------------------------

One explanation from wikipedia (https://en.wikiversity.org/wiki/Cubic_Spline_Interpolation) seems easier to understand.  
For each [x{i-1}, xi], we want to find a Ci(x) such that 
Ci = ai + bi x + ci x^2 + di x^3, which is a cubic function.  
It can be seen that it is like a piecewise polynomial fitting.  
Why do we want to do this?  
We know dCi/dx = bi + 2ci x + 3di x^2  
and d^2Ci/dx^2 = 2ci + 6di x;  
then we can make dCi/dx = dCi+1/dx (condition 1) and d^2Ci/dx^2 = d^2Ci+1/dx^2 (condition 2), which can make the curve very smooth.  
We also have Ci( x{i-1} ) = y{i-1} (condition 3) and Ci( x{i} ) = y{i} (condition 4).  
Let n+1 be the total number of data points, there will be n Ci, 
and as a result there will be n-1 + n-1 + n + n = 4n-2 equations.  
But we have 4n unknowns. 
So as long as we have 2 more equations we can solve the unknowns precisely.  
One example to have two more equations are C1'(x0) = known value and Cn'(xn) = known value.

The method in wikipedia seems to combine xi and yi together, as we can see from condition 3 and 4.  
Also, the method makes the 2nd derivative of Ci|x=xi equal to the 2nd derivative of Ci+1|x=xi,
(the method in lecture notes also has this property... nvm..)

The explanation from lecture notes is harder to understand, but they should carry the same meaning.  
The method in lecture notes seems to separate xi and yi, each has its own cubic spline.

For x, we take 2 neighbouring nodes xi and x{i+1}, or pi and p{i+1} following lecture notes.  
Then we introduce one new variable called u, such that 0 <= u <= 1, and we create a model
x = phi(u) = a0 + a1 u + a2 u^2 + a3 u^3 for the line connecting pi and p{i+1}.  
Now it has nothing to do with y. it is between u and x.  
Following the method in wikipedia, we will be able to find out all the ai for each section of curve.  
Now the question is, given a x, how do i translate it to a u for the curve between the 2 points in which x is located?  
Maybe it is just u = (x - xi) / (x{i+1} - xi)..

Ok, let me describe the method in lecture.  
Phi'(u) = a1 + 2a2 u + 3a3 u^2  
phi''(u) = 2a2 + 6a3 u  (this is a line).  
Let's let phi''(0) = Di, and phi'' = D{i+1} (we don't know Di and D{i+1}; later we will try to find them).  
Implicitly we already used condition 2, because in the next section (x{i+1} and x{i+2}) its phi{i+1}''(0) = D{i+1} = phi''(1) in the current section ( x{i} and x{i+1}).    
Then we will try to express a0 a1 a2 a3 in terms of Di, D{i+1}, xi and x{i+1} => (from 4 unknowns to 2 unknowns, but used up conditions 2 3 and 4).  
How? firstly, phi''(u) = (1-u)Di + u D{i+1} (equation 1) ==> we can get a2 and a3 in terms of Di and D{i+1};  
now integrate equation 1, we will have phi(u) = A + Bu + 1/2Di u^2 + 1/6( D{i+1} - Di ) u^3.  
With condition 1 and 2, i.e. phi(0) = xi, phi(1) = x{i+1}, we can get A and B, 
and more importantly we can express a0 and a1 in terms of xi, x{i+1}, Di and D{i+1}.

We have only the last condition left.. the condition 1, which is the 1st derivatives at the boundary are the same ..  
So phi'(1) in current section = phi{i+1}'(0) in next section ==> all can be expressed in terms of xi, x{i+1}, x{i+2}, Di, D{i+1} and D{i+2}.  
Then shift the unknowns Di, D{i+1} and D{i+2} to LHS and knowns xi, x{i+1}, x{i+2} to RHS, we will have n-2 equations.  
Simply group them in a matrix AD = Z, where D = [D1 D2 ... Dn].T, and each row of A = the coefficients of each n-2 equation.  
Each row of Z is one number that is the result of the RHS of the n-2 equations.  
Of course we still need 2 more equations. 
Like the method in wikipedia, we need to have 2 more boundary conditions which lead to 2 more equations.  
Simply add these 2 equations to the matrix equation.  
The A matrix will be exactly a square matrix.   
Now we can obtain D by simply matrix operation: D = A^(-1) Z.

After having D, each of the n-2 equations are known.
Then we can solve for any input of x!  

For the y portion, do exactly the same thing.

Question: any difference in the results between this method and the method described in wikipedia?  
    -> it seems that the method in lecture notes allows any dimension in a data point, because the model for each dimension is calcuated separately.

Another question: after doing all these, we got 2 big sets of equations, one between x and u, the other between y and u,
how to combine them together to have just x and y ?  
    -> one solution i can think of is that we have a y = mu(u) function and a x = phi(u) function, then we convert phi(u) to u(x), then sub u(x) to y =mu(u) to make it become y(x).

Btw i think another way to solve the problem using similar way in the lecture notes is 
to represent a0 and a1 in term of a2, a3, xi and x{i+1} .. 
And then we solve a2 and a3 using similar way.


Piecewise Lagrange Interpolation
-------------------------------------

We can choose a few points to construct one lagrange function.  
The simplest case is to pick two points: pi and p{i+1}.

Like cubic spline, we need to introduce one more variable u.  
The relation between x and u is like that between y and x in the global lagrange method.  
For xi and x{i+1}, we have a model x = x(u) = L0(u) xi + L1(u) x{i+1} such that 
when u = 0, x = xi, and when u = 1, x = x{i+1} (same for y).  
We already know the solution for L0 and L1 
(note that the variable is u! and u has 2 values: 0 and 1; it is like u0 = 0, u1 = 1), 
i.e. L1(u) = (u-1)/(0-1) = 1-u and L2(u) = (u-0)/(1-0) = u  
so x = (1-u) xi + u x{i+1}  
similarly, y = (1-u) yi + u y{i+1}.  
These 2 equations simply mean that x and y are the linear interpolation between the neighbouring 2 points.  

To make things more interesting, let's pick 3 points as a section.  
For one section we will have x = L0(u) xi + L1(u) x{i+1} and L2(u) x{i+2}.  
The solution for Li are:  
L0(u) = (u-0.5)(u-1)/( (0-0.5)(0-1) ) = 2u^2 - 3u + 1;  
L1(u) = (u-0)(u-1)/( (0.5-0)(0.5-1) ) = -4u^2 + 4u;  
L2(u) = (u-0)(u-0.5)/( (1-0)(1-0.5) ) = 2u^2 - u.  
So x = (2u^2 - 3u + 1) xi + (-4u^2 + 4u) x{i+1} + (2u^2 - u) x{i+2}   
same for y ..  
For other section, just change xi x{i+1} x{i+2} accordingly.

It can be seen that 2 neighbouring sections don't have the same 1st order derivatives..
