Understand gradient descent
--------------------------------

Firstly, please understand Taylor series.

Given a function f(), we want to find the minimum value in this function.

If there is 1 variable, e.g. x, we can easily find the solution by using df/dx = 0 and then solve for x.

But what if we can get the expression for df/dx but it is extremely complicated solve df/dx = 0?  
What if there are multiple variables, e.g. x1 to x100? 

One way to solve this is gradient descent.

Using Taylor series, we know f(y) = a0 + a1 (y - a) + a2 (y-a)^2 + ... where
a0 = f(a), a1 = f'(a), a2 = f"(a)/2 ...  

Let y = x + deltaX, and a be x 
f(x + deltaX) =~  f(x) + f'(x) (deltaX) + f"(x) (deltaX^2)/2

note that f(x) is the result of the function given x.  
Now we try to find a deltaX such that f(x + deltaX) will be smaller than f(x).  

One way to do this is to minimize f(x + deltaX) wrt deltaX and make it = 0:  
0 + f'(x) + f"(x) deltaX = 0  
so deltaX = - f'(x) / f"(x)

therefore, given the expression of f'() and f"(), we can pick an initial x0, 
and then keep doing this: x(k+1) = xk + deltaX = xk - f'(xk)/f"(xk)  
and then (hopefully) we will get to the bottom of the function f.

When there are multiple variables, the expression for deltaX becomes:  
deltaX = - Hessian(x)^-1 * delta_f(x) where both Hessian(x) and delta_f(x) are matrix. 

Therefore x(k+1) = xk - Hessian(xk)^-1 * delta_f(xk).  
This is actually Newton's method, and it is a superset of many methods, including gradient descent.

So what is gradient descent?  
Because Hessian is very hard to compute, so in gradient descent, we simply set it to an identity matrix I (equivalent to non-exist).

Then we set an value named alpha to control the step length of decreasing x(k+1).  
Ultimately, the expression for gradient descent looks like:  
x(k+1) = xk - alpha * delta_f(xk)

intuitively, for a given array of xk, and because we know the expression of delta_f(), 
we can compute the gradient of f when x = xk.
It is  delta_f(xk), which is a column matrix because f needs to be differentiated against each xi.  
After knowing the gradient, we change xk in the opposite direction of the gradient and make it x(k+1),
and so on, until at some point when x = x(k+1) function f is almost at the minimum value.

There are a few things to be noted:  
1. alpha has to be set carefully. if it is too large, we may get further and further away from the bottom. 
If it is too small, each step changes too little and it takes forever to get to the bottom.  
2. there are some methods to choose a reasonable alpha, such as line search.  
3. gradient descent is such one special case of the newton's method. 
There are other methods that try to estimate the Hessian term to make the method closer to the newton's method.


Compare nonlinear function and linear function
---------------------------------------

Linear function: it is linear w.r.t a, the parameters.  
E.g. v = a0 + a1 x + a2 y + a3 z 

when we solve this, most likely we are using an error function of sum square errors.  
But as long as the original function is linear wrt a, it is easy to solve, because it has a close-loop answer.

Nonlinear function is a function that is not linear wrt a ..  
E.g. v = x^2 / (a1 + x^2) + y^2 / (a2 + y^2) + z^2 / (a3 + z^2)  
the error function can still be sum square errors, i.e. E = SUM{ (ve_i - v_i)^2 } where ve is the estimated v. 
It is not easy to solve this one by simple differentiation and make it equal to 0.  
One solution is to use gradient descent!

Firstly, we need to obtain dE/da (the gradient).  
DE/da = SUM {2 (ve_i - v_i) dve_i/da } 
      = [ SUM{2(ve_i - v_i) * dve_i/da1}, SUM{2(ve_i - v_i) * dve_i/da2}, SUM{2(ve_i - v_i) * dve_i/da3} ]  

for one input a, and one of the data point (xi, yi, zi) and the corresponding true vi, 
we can get the ve_i - v_i part.   
We also know dv/da1, dv/da2 and dv/da3, so we can also get each dve_i/da1 (i.e. dv/da1 | a1 = a1_input, xyz = xyz_input), 
and same for dve_i/da2 and dve_i/da3.  
Then just keep doing the a = a - alpha * gradient with a proper alpha, and ultimately we will get a (local) minimum of a.
