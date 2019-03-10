Definition
--------------------

A stochastic process X = {X(t), t Belongs_to T} is a collection of random variables.
	- each X(t) is a random variable
	- any outcome of X is a sample path


Example: counting process
------------------------

A stochastic process {N(t),t>=0} is a couting process if N(t) represents the number of "events" that have occurred up to time t.  
(each N(t) is a random variable, that can have many different outcomes.)

for s < t, N(t) - N(s) equals the number of events occurred in the interval (s,t].

Example: poisson process
----------------------------
A couting process {N(t), t>=0} is a poisson process with rate lambda > 0 if
	- N(0) = 0
	- has independent increments
	- number of events in any interval of length t is poisson distributed with mean (lambda*t): P{N(t+s)-N(s)=n} = e^(-lambda*t) * (lambda*t)^n / n! and E(N(t+s)-N(s) = lambda*t)

another understanding:  
	- buses arrives at time 0, t1, t2 .. tn, with intervals T0, T1, ... Tn. Therefore, Ti = t_(i+1) - ti 
	- P(T0 > s) = P(no bus from time 0 to s) = e^(-lambda*s)
	- P(Ti > s) = P(no bus from ti to t_(i+1)) = P{N(t_(i+1)) - N(ti) = 0} = e^(-lambda*t)
	- Ti are independent and identically distributed (i.i.d.) exponentail random variables with mean = 1/lambda (every Ti is a random variable, and follows the same exponential distribution)
