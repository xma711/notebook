## Online machine learning

reference: https://en.wikipedia.org/wiki/Online_machine_learning

"Online machine learning is a method ... in which data become available in sequential order
and is used to update our best predictor for future data at each step,
as opposed to batch learning techniques which generate the best predictor
by learning on the entire training data set at once."

It is used in two scenarios:  
	- The entire dataset is too big to be trained at one go  
	- For the algo to "dynamically adapt to new patterns in the data", or "when the data itself is generated as a function of time"


## How to achieve this

There are various methods for different learning algorithm.

e.g. for least square, there is an online learning method called recursive least squares.

stochastic gradikent descent seems a natural online learning method,
because it can be performed multiple stochastic gradient passes over the data.  
intuitively, the process can be continued at different times, while the latest model is always more updated than the last.  
(Should the new data points be used directly as a mini batch or merged with the main training data set first before doing random sampling again?)

There is also this online convex optimization.

### Online convex optimization (OCO)

OCO "is a general framework for decision making which leverages convex optimization to allow for efficient algorithms"

OCO is to minimize a concept called regret.

One of the OCO algo is called Follow the leader (FTL).
