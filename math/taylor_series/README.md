Taylor series
-------------------------

not Taylor Swift..

given a function f(), how to make such an equation valid: f(x) = a0 + a1 x + a2 x^2 + a3 x^3 + ...  
e.g. given e(x), how to express it in terms of  a0 + a1 x + a2 x^2 + a3 x^3 + ... 

firstly, let's assume them are equal. then we proceed to find out the values for ai.  
it is obvious that when x = 0, RHS will be reduced to a0 only.  
therefore, a0 = f(0).

then we can see that df/dx = 0 + a1 + 2 a2 x + 3 a3 x^2 + ...  
if we let x = 0 on both sides, then we can get a1 = df/dx and sub (x=0) = f'(0).  
note that f'() is just a function. f'(0) is when we substitute 0 to the variable.  

by using the same logic, a2 = 1/2 f''(0) and a3 = 1/(3!) f'''(0) and so on.

the above explanation is easy in terms of mathematics, but how about the physical meaning?

let's take one example. f(x) = e^x. as de(x)/dx = e^x
by applying taylor series, we have e^x = e^0 + e^0 x + 1/2 e^0 x^2 + 1/3! e^0 x^3 + ... (equation 1) 
which is  e^x = 1 + x + 1/2 x^2 + 1/3! x^3 + ... 
okay let's take the first 4 terms to make an approximation.  
when x = 1, LHS = 2.718, RHS = 2.67 which is pretty close to the LHS already.
when x = 0.1, LHS = 1.105170, RHS = 1.105167 which is even more closer to LHS.

we can see that when x is smaller, the first 4 terms are better approxmators.  
let's take a look at equation 1 again, what does it mean by the RHS?  
it actually means that we take one point x = 0 and then use this point to calculate f(0), f'(0), f''(0) ...,  
and then from these terms we try to multiply them with a term that has something to do a delta x (which happens to be x in this case).  
if this delta x is smaller, the less terms in the taylor series are needed to approximate the true results.

can we take a "reference" from other value instead of x=0?
the answer is yes.  
let's say we want to take x=1 as the "reference point", then we modify the series to   
f(x) = a0 + a1 (x - 1) + a2 (x - 1)^2 + a3 (x - 1)^3 + ...  
this time, a0 = f(1), a2 = f''(1)/2, a3 = f'''(1)/3!, etc.  

or more generally, f(x) = f(c) + f'(c) (x - c) + 1/2! f''(c) (x - c) where c is a constant. (equation 2)

again, note that f() f''() f'''() are just functions. 
the variable name can be x, or can be anything else, like y, and it won't change the logic of f() or f''().


Application
--------------------

take e^x as an example again.  
assume that we start with a point x0 = 1 and we can calculate f(1), f''(1) and so on, 
how to approximate f(x) when x = 2.5 (x1=2.5)?  
from equation 2, let's substitute x = 2, and c = 1, we will have
f(2.5) = f(1) + f'(1) (2.5 -1) + 1/2 f''(1) (2.5 - 1)^2 + ... 
so f(2.5) = f(1) + f'(1) (1.5) + 1/2 f''(1) (1.5)^2 + ...


what about f(x + k) ?  
the confusing part is that 'x' is usually used as the variable name in a function,
and now it is only part of the input to the function.  
the trick here is don't use x in the equation 2. 
and also remember f() is a function, the variable name doesn't have to be named 'x'. it can be named as anything, like y.  

let's write equation 2 in terms of y:  
f(y) = f(c) + f'(c) (y - c) + 1/2! f''(c) (y-c)^2 + ...   
then, let's sub y = x+k, c = x, then we will have: 
f(x+k) = f(x) + f'(x) * (x+k - x) + 1/2 f''(x) * (x+k - x)^2 + ... 
i.e. f(x+k) = f(x) + f'(x) k + 1/2 f''(x) * k^2

again, note that f'(x) doesn't mean df/dx, because f() may not have to be represented in terms a variable 'x'.  
f'(x) only means the 1st order derivative of function f(), 
and then we calculate the value of f'() when the variable (whatever name it is assigned)  equals to x.

the confusion here is that we have used 'x' for the variable name for a function for so many times,
then i can not easily imagine x is actually a convenient way to name a variable, but not a MUST!!!
f() can be f(y), f(z), f(b) and f() is still f(). it represents a transformation from an input to an output.  
similarly, f'() doesnt mean df/dx if f is not represented in terms of x.
f'() is just f'(), which is a function that represents a transformation from an input to an output.  
and of course f'(x) doesn't mean df/dx!!! it means we sub variable = x into the function f'().  
this is probably the most important point here: f'() is its logic representation itself. it doesn't have to do with variable name 'x'.

in fact, k is the change from x, and k is the delta x. so,  
f(x + deltaX) = f(x) + f'(x) deltaX + 1/2 f''(x) deltaX^2.  
This is exactly the formula in the lecture notes of the media module!!!  
This should be the most easy-to-understand way of deriving this formula.


If i cannot get over the variable 'x', another way to derive it is from the follows 
(not recommended; better follow the above explanation):

we know that f() is a function. so x+k is just the input to the variable.  
maybe a better way to see this is that the function is f(y) when y = x+k.  
let's say that k is the 'variable' we are interested in , so given x is a 'constant', 
how to express f(x+k) in terms of a0 + a1 k + a2 k^2 + ...?  

let y = g(k) = x + k  (from k's point, x is a constant). 
so f(y) = f(x+k) = f( g(k) ) = m(k).  
dm(k)/dk = df(y)/dk = df(y)/dy * dy/dk = df(y)/dy * 1 = df(y)/dy = f'(y) !!!  
this means that dm/dk is exactly the same as f'(y)!!!  
let's apply taylor series on m(k), so  
m(k) = a0 + a1 k + a2 k^2 + ...  
so a0 = m(k) when (k = 0) = f( x + 0) = f(x)  
a1 = dm/dk when (k = 0) = df(y)/dy when (k = 0) = f'(y) when (y = x + 0) = f'(x) !!!!  
a2 = dm/dk when (k = 0) = 1/2 d^2f(y)/dy^2 when (k = 0) = 1/2 f''(y) when (y = x + 0) = 1/2 f''(0).

okay solved!!
