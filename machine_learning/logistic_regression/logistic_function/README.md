Logit Function
--------------------------

Reference: http://www.theanalysisfactor.com/what-is-logit-function/

"A link function is simply a function of the mean of the response variable Y 
that we use as the response 
instead of Y itself."

The logit function is one of such link functions.

This means that "when Y is categorical, we use the logit of Y as the response" in our regression equation instead of just Y:  
ln(P/(1-P)) = h(x),  
where P is defined as the probability that Y=1, and h(x) is a linear combination of xi (x is a vector).

(   btw, after exp both sides and rearrange, we can get the familiar P = 1/( 1+ exp( -h(x) ) )   )

why doing it this way?  
If we plot Y with x directly and try to obtain the best fitted line, the line obtained will not be able to represent the relationship between X and Y well. 
(see reference.)  
But if plot the probability that Y=1 when X=x (some binning should be needed) against X, 
the graph looks 'better' (less gaps; more continuous..).  
Based on the shape of the graph (S shape), there could be quite some functions that can describe the relationship.  
Logistic function happens to be one of them and its results are relatively easy to interpret.


Logistic regression
------------------------------

Reference: https://en.wikipedia.org/wiki/Logistic_regression

logistic regression is a regression model where the dependent variable is categorical.


Train the model
---------------------

Reference: http://machinelearningmastery.com/logistic-regression-tutorial-for-machine-learning/

If Y = 1 or 0, then it is easier because we can use Yi as the observed probability to compare with the estimated probability from the model (from 0 to 1).  

If Y is something like 1 and -1, we may have to represent -1 by 0, meaning it is not 1.
Then we can use the same way to estimate the unknown parameters inside the model.

What exactly is the cost function?  
Reference: https://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html  
cost = -log( predicted probability from xi) if the true yi = 1 and
cost = log (1 - predicted probability from xi) if the true yi = 0

In both cases, cost = 0 if the predicted probability is the same as y and cost increases if the 2 values divert.

The cost can be combined to one single equation: -1/m SUM{ yi log(pi) + (1-yi)log(1-pi) }
where pi is the predicted probability from xi.


Question: Can we compute the ln(P/(1-P)) from Y for each x (some binning is needed), and then use the traditional least square to obtain the weights?
