Newton-Raphson Method
------------------

for a general function f(x), we want to get x for f(x) = 0.

let y = f(x), then dy/dx = y' = f'(x).

1. set arbitrarily x = x0
2. y0 = f(x0). 
3. with (x0, y0) and y' when x = x0 = f'(x0), we can get a line equation y = ax + b for the tangent line at point (x0, y0).  
	- b = y0 - f'(x0) * x0, so the equation will be y = f'(x0) x + (y0 - f'(x0)*x0).  
4. for this line, to get the solution of x when y = 0, x = (f'(x0)*x0 - y0) / f'(x0) = x0 - y0/f'(x0) = x0 - f(x0)/f'(x0).

by repeating step 1 to 4, we will have xi = x_{i-1} - f(x_{i-1})/f'(x_{i-1}). This is newton-raphson method.

If there is a converge, the answer will satisfy f(x) = 0;

If there are multiple answers, i can try and error with a few different x0.

Example
------------------

newton_raphson.cy
