M/M/1
-------------------------

First M: Markovian property for arrivals of customers
second M: Markovian for processing time in the server
1: there is only one server.

There are others like M/G/1, M/M/2, M/M/n.

M/M/n is like a calling centres with n workers to pick up phones.


The things we are interested in are, given the average arrival rate (lambda) and average processing rate (mu):
	- what is the average queuing delay?
	- what is the average size of the queue?
	- what is the probability that the queue == certain number in the long run?
	- what is the ratio that the server is idle? (the value of pi0, the probability that the system is in state 0)

for M/M/1 processing to be valid, it must be markovian. 
For continuous time markov chain, it must be exponential. therefore, M is equivalent to exponential too.

Markovian
----------------------

Memoryless!

Whether it is discrete or continuous, the current state only depends on the previous state.  
It is easier to understand the discrete state scenario.  

For the continuous case, it means that if i pick a time (tp) in the past with state i, the future state at t depends only on state i at tp and the duration (t-tp), not any time before tp.
One example is the the number of buses that have arrived. 
If i know that since 10am there are 20 buses, what is the number of buses one hour later? 
The expected number of buses arrive in one hour can be calculated from the poisson distribution, which doesn't need any information before 10am..  

The inter-arrival intervals actually (have to) follow an exponential distribution.  
As far as i know, exponential distribution is the only one with the memoryless property.

Limiting distribution (pi) of the system state exists when
	- all states can be reached from any other state. 
	- no state is transient. "transient" means that the state may happen in the past, but with certain probability that it will never happen again. 
	- the expected time to return to a state is finite.


Solve for M/M/1
-------------------------

Draw each state in a bubble. put the arrival rate (lambda) at the arrow pointing from a bubble to a buble at its right.  
Put the process rate (mu) at the arrow pointing from a bubble to one at its left.

At equilibrium (in the long term), the probability that each state can happen has a fixed value. represented by pi0, pi1, pi2 ...
Equation 1: sum of pi0, pi1, pi2... = 1.

Then, for each bubble, at equilibrium, the rate into the bubble = the rate go out of the bubble.  
E.g. for bubble with state 0, pi0 * lambda = pi1 * mu;  
for bubble with state 1, pi0 * lambda + pi3 *mu = pi1 * mu + pi1 * lambda , which can be simplified to pi1 * lambda = pi2 * mu,  
and so on.

Ultimately we have n equations (n = num of states) and then we can solve all pi. 

Note that pi0 is the ratio of time that the server is idle.

After getting all pi, the average number of customers in the system (both queue and server) can be obtained by sum of all (pi_i * state_i), by probability theory.

With the average size of customers in the system (L) and average arrival rate, by little's law (L=lambda * W) we can have the average time (sojourn time) in the system:  
W = L/lambda.

To calcuate the average size of the queue (Q), the result = sum of all (pi_i * (state_i - 1)) for M/M/1. this is because if there are n customers, 1 must be in the server.  
With Q, we can have to average delay D = Q/lambda by little's law.

The average number of customers in the server = L - Q.  
The average time in the server = W - D = 1/mu (interesting result. need to double check).

For a system that always has customers, the average time in the server = 1/mu without doubts. 
What about the case that there can be 0 customers. the average time for all customers in the server is still 1/mu? seems this is the case. 


M/G/1
----------------
G means the distribution of the processing time/rate in server is general. it can be exponential, or normal, anything.

M/G/1 is a superset of M/M/1.

Firstly, without proof, we have PASTA (Possion arrivals see time averages).
	- it means if arrivals are poisson, then the proportion of time a queueing system spends in a given state pi_i is equal to the proportion pi_i' of the arrivals who observe the system in that state.
	- in math, the equation is lim(t->inf) 1/t * INTEGRATE (0 to t) {f(X(s)) ds} = lim(n->inf) 1/n * SUM (0 to n) {f(X(tj-))}, where f is any real bounded function.

To use PASTA, we need to sub in X(s) and f() with meaningful things. 
E.g. X(s) = V(s), the workload in the system. f(y) = 1 {if y<=x}.
Then, lim(t->inf) 1/t * INTEGRATE(0 to t) {1{if V(s) <= x} ds} = lim(n->inf) 1/n * SUM(j=0 to n) {1 {if V(tj-) <= x}} and
1 {if V(tj-) <= x} = P{D(tj-) <= x}. 
This shows V and D have the same distribution.

Anyway, ultimately we have E[V] = E[D] for M/G/1. 

For G/G/1 and FIFO, we have Brumelle's Formula, E[V] = lambda E[SD] + lambda/2 * E[s^2] = lambda E[S] E[D] + lambda/2 E[S^2] = p E[D] + p E[Rs] where p = lambda * E[S], E[Rs] = E[S^2]/(2E[S]) using RCL. 
It means the average workload = average delay in the queue + average delay in the server. 
(average delay doesn't consider the time the system is empty, so need a p to calculate the average delay in the queue.) 

For M/G/1, E[V] = E[D], so E[D] = p E[D] + p E[Rs] ==> E[D] = p/(1-p) * E[Rs] = lambda E[S^2]/(2(1-p)). Again this applies to M/M/1. 
E[S^2] relates to the variance of the processing time in the server. 
The higher the variance, the larger the average delay.

After obtaining E[D], we can get E[W] = E[D] + D[S], E[Q] = lambda * E[D] and E[L] = lambda * E[W].

How about LIFO? E[V] = E[Vq + Vs] = E[Vq] + E[Vs] where 
	- E[Vs] = (1-p) 0 + p E[Rs] = p E[Rs] and
	- E[Vq] = E[SUM(i to Q) {Si}] = SUM(q=0 to q=inf) { E[S0 + S1 + S2 + .. Sq] * P{Q = q}} =  E[S] * P{Q=1} + 2E[S] * P{Q=2} + 3E[S] * P{Q=3} + ... = E[S] * (1* P{Q=1} + 2* P{Q=2} + 3* P{Q=3} + ...) =  E[S] * E[Q] = E[S] lambda E[D] = P * E[D]
	- Therefore, E[V] = p * E[D] + p E[Rs] which is exactly the same as FIFO. This means Brumelle's formula holds for LIFO too.
	- Does E[V] = E[D]? should be the same. back to the PASTA equation.


Some intuition
---------------------

When there are multiple queues, each queue's arrival rate is relatively smaller. 
This means the average idle intervals in each queue is longer, causing some servers to be idle.

When the queues are combined, the arrvial rate is the combination of all arrival rates. 
Obviously the idle intervals in this single queue is much smaller.  
All the servers then are able to serve the customers in the queue with less idle times.
