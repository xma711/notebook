Little's Law: L = lambda * W, where
	- L is the long term average of items/ppl/pkts in the system
	- lambda is the long term average rate of arrival to the system
	- W is the long term average processing time of one item in the system

from Wikipedia: The long-term average number of customers in a stable system L is equal to  
the long-term average effective arrival rate, lambda,  
multiplied by the (Palm-)average time a customer spends in the system, W.

This is a remarkable result, as the relationship is "not influenced by the arrival process distribution,  
the service distribution, the service order, or practically anything else."

To prove the law, first we have   
	- (part 1) for all customers who have come in and exited the system, the sum of all times of their stay in the system in from t=0 to t=T is smaller or equal to  
	- (part 2) the sum of all times of all customers' stay in the system so far, which is smaller or equal to
	- (part 3) the sum of all times of all customers' stay in the system + the times of all customer expected to stay in the system 
	
we can then show that (1/T)*(part 3) and (1/T)*(part 1) tend to be lambda*W when T goes to infinity.  
Then (1/T)*(part 2) must be lambda*W when T goes to infinity.   
Note that (1/T)*(part 2) is exactly the long term average number of customers in the system, L. 
