Derive Exponential distribution from Poisson distribution
---------------------------------------

Reference: http://stats.stackexchange.com/questions/2092/relationship-between-poisson-and-exponential-distribution

let Nt be the accumulated number of arrivals at time t;  
let Xt be the time taken for one additional arrival to arrive Assuming someone arrived at time t.  
These conditions are equivalent: (Xt > x) === (Nt = Nt+x),  
RHS meaning the accumulated number of arrivals stay the same at time t and t+x.

```
then P(Xt <= x) 
    = 1 - P(Xt > x)  
    = 1 - P( (Nt+x - Nt) = 0 )  
    = 1 - P( Nx = 0 )  
    = 1 - exp(-lambda * x)
```

therefore, the CDF of Xt is that P(Xt < x) = 1 - exp(-lamba * x).  

And this is the expoential distribution, in which the random variable Xt is the time taken for one additional event to occur.

The intuition is that if the time taken for one additional arrival is more than x (the next arrival could happen even later than x), 
it must mean no event has happened in the duration x. this probability can be calculated using poission distribution.  
After knowing this, then we know that the probability that the additional arrival is within x is just 1 - the probability that the arrival happens beyond x.  
In fact, this is equivalent to saying that there is at least one event happens within the duration x.  
If understanding this, it is easy to understand exponential distribution.

The usual confusion i have is that the additional arrival that arrives within the period x means only one arrival happens in period x. 
This is WRONG!  
We are concerning about the time taken for the next arrival to happen, 
but the probability of the time taken being less than x automatically includes the cases that more than one arriaval occurs during period x.


Intuitiion (may not be the best way of explanation)
-------------------

Given the average arrival rate of a bus (lambda), what is the probability at least a bus (can be more) will arrive within x units of time?

F(x) = P(X <= x) = 1 - e^(-lambda * x)

i.e. F(x) = P(X <= x) = 1 - P(no bus arrives from 0 to x) = 1 - e^(-lambda * x)  
where P(no bus arrives from 0 to x) = e^(-lambda * x) is based on possion distribution.  
In fact this is the link between expoential and possion distribution.

F(x) = lambda * e^(-lambda * x)

E[X] = 1/lambda

Var[X] = 1/lambda^2


Memoryless or Markovian property
-----------------------------------
P{X > s+t | X > s} = P{X > t}  meaning whatever has happened doesn't matter to calculating the future probability


other info
-----------------

Reference: https://www.probabilitycourse.com/chapter4/4_2_2_exponential.php

exponential distribution can be viewed as a continuous analogue of the geometric distribution.
