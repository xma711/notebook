Theory
--------------------

For Right Continuous Functions..

X' = lambda * J, where
	- X' is the time average gradient of the function
	- lambda = average arrival rate into the system
	- J is the average jumps where J is the average of Jn and -Jn = x(tn+) - x(tn-)

Proof
--------------------
For a Cadlag function x(t), t>=0 : deterministic and right-continuous with left limits x(t-).

Integrate(from 0 to t) x'(s) ds = x(t) - x(0) + Sum(from n=1 to n=N(t)) Jn, where -Jn = x(tn+) - x(tn-).

Divided both sides by n and set n->inf, then left-hand side = X' and right hand side can be derived to lambda * J.

Note that x'(s) the gradient of the function at all places except the jumps. 
Left hand side = the area under the x'(s) without the jumps instances.

Intuition
---------------------

Somethings instantly jumps to x1 at t1 then continuously decreases to some number (0 for e.g.), then x2 at t2, then x3 at t3... 
Then the average gradient = -1 * the sum of jumps / the total duration = (-1 * sum of jumps/ num of jumps) * (num of jumps / total duration) = J * lambda

what is the probability that the waiting time R is larger than a, given the distribution of the inter-arrival time?
-------------------------------------------------------------

Given F(T) (or f(T) or all P(T = an interval)) where T represents any Ti because they all have the same distribution, what is P{R>a}?

1. given y = R(t), the remaining time for a bus to come as seen at t, y = R(t)'s graph will look like: R(t=ti) = Ti (ti are the times the bus arrives), between Ti and T_{i+1} it is a line with gradient -1, until R(t=t_{i+1} - epsilon ) = 0 (epsilon is an extremely small number). of course, R(t=t_{i+1}) = T_{i+1}

2. using RCL, we will have average gradient of R(t) = lambda * (-1) * E(T), i.e. -1 = -lambda*E(T). Or, lambda = 1/E(T). Note that this conclusion applies to any distribution, because we didn't assume any distribution for T.

3. Does this solve the question? No. We have to shift the R(t) graph a bit.  
	- let's shift y = R(t) graph down by a units, and take the positive parts, we will have a new graph y = (R(t) - a)+. 
	- using RCL again, the average gradient of y = (R(t) - a)+  = lambda * (-1) * E[(T - a)+]. 
	- (T-a)+ means that only the portion above t-axis (i.e. x-axis) needs to be counted, and all the y(t = ti) = R(t = ti) -a = Ti - a, which is shorter than the y(t = ti) given y = R(t). 
	- The gradient between R(ti) -a to the point it touches t-axis is still -1, but there is now 0 between this point to the t_{i+1}. This means the average gradient is no longer -1, but something between -1 and 0.
	- the average gradient = the probability of (R(t) - a > 0) * (-1) + the remaining probability * 0 = probability of (R(t) > a)
	- therefore, P{R(t)>a} = lambda * E[(T-a)+]. again, this doesn't assume any distribution for T.
	
4. another way of looking at this problem is that:
	- we want to solve P{R > a}, i.e. P{R - a > 0}, i.e. P{y2 > 0} where y2 = R - a. 
	- P{y2 > 0} is exactly equal to the average gradient of y2 * (-1), because the average gradient = -1 * the ratio of y2 > 0 = -1 * the probability that y2 > 0
	- using RCL we will be able to link this average gradient to the average jumps, or -E[(T-a)+], which is something we know. 
	- in short, we can transform the problem of the remaining waiting time to a problem that has something to do with the distribution of the inter-arrival intervals.

5. an example for T's distribution is exponential distribution (meaning Ti can be from 0 to inf, but the probability drops based on exponential function). in this case, we can show that P{R(t) > a} = P (T > a). to prove this, just expand the E[(T-a)+] with the integration INTEGRATE(0 to inf) {((x-a)+ * f(x)) dx} and then sub in f(x) and solve for a close form.  

Some notes
---------------------

Y = R(t) is one graph on the y-x plane. 
Y = R(t) - a is another different graph on the y-x plane.

Given y =  R(t), if we shift this graph down by a units, then we will have a new graph y = R(t) - a (or y2 = R(t) - a). 

It is not that R(t) becomes R(t) -a. they are two different lines, totally. just that their relationship is that if i take the R(t) line, and shift it down by a units (in the process, it is not R(t) any more), i will get the line for R(t) -a.

When y2 > 0, it means R(t) - a > 0 ==> R(t) > a ==> y > a (the y values in graph 1 > a).

Pls don't confuse y and y2, or R(t) and R(t) - a.


Each Ti is a random variable, but any Ti has the same distribution, represented by P(T < s). we have to collect samples for Ti to get the parameter values for the known distribution for Ti. but we can't. Ti will happen once only. So to get the distribution parameter values for Ti, we will record the outcomes for Ti, Ti+1, Ti+2 ... etc. Then the distribution parameters can be obtained from these samples. 
