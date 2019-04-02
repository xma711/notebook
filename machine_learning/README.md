Practical guide of solving problem
------------------------------

1. get data X and Y

2. decide if the problem is regression, classification or others

3. pick a hypothesis class accordingly.  
	e.g. regression problem: pick linear regression;  
	e.g classification problem: pick svm, logistic regression or neural network.

4. decide some hardcoded parameters in the hypothesis class if needed.  
	e.g. the parameter for l2 norm regularizer.

5. pick a loss function. 
Usually you do not have to pick, because popular hypothesis class has its popular choice of loss function.  
	e.g. linear regression: square loss function;  
		svm: hinge loss function;  
		logistic regression: log loss function.

6. split the data to training set and test set

7. use empirical risk minimization (ERM) algorithm to pick the best hypothesis 
	from the chosen hypothesis class to fit the training data, as best as you can.  
	how exactly the ERM algorithm is carried out base on the hypothesis class and the loss function chosen.  
	e.g. linear regression: there is a closed-form solution;  
		svm: stochastic gradient descent;  
		logistic regression:  Maximum likelihood estimation

8. use the hypothesis obtained from ERM to get the risk/error from the test set.  
	if the risk is too large, analyze if it is due to 
		approximation error (too restrictive or unsuitable hypothesis class will lead to large approximation error) 
		or estimation error (not enough sample data, causing overfitting)  
	(refer to textbook chapter 11 to know how to analyze what type of error it is..)

9. deal the error accordingly.  
	if it is due to appr error, try to use another hypothesis class or change some hardcoded parameters and repeat from step 3.  
	if it is due to estimation error, try to increase the sample size. if this is impossible, try to reduce the hypothesis class complexity. Or do some dimension reduction (using PCA e.g.). then repeat from step 3.  
	if totally don't know what component the error is accounted for, maybe just try another hypothesis class.

10. if risk in test set is small enough, then accept the hypothesis.


Sample size needed
------------------

For theoretical aspects, read README.md in directory sample_complexity/

in practice, the n/d ratio 
between the number of instances n available in the training set
and the dimension d of the feature-space 
must be at least 10.  
Reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3244008/  

stationarity and machine learning
-----------------------------------------

Reference: https://www.quora.com/Why-cant-machine-learning-algorithms-handle-non-stationary-data

similar to time series, machine learning requires the data to be stationary.
I.e. the training data and the test data and the future data (when the model is used for) should draw from the same distribution.

Before applying any machine learning algo, always think about if p(x,y) is stable (i.e. not changing).

If some features are not captured, it won't be too bad if the data has randomized values for these features (e.g. half data is male and half is female but gender is not in the feature set).  
(however, it is definitely better if such features exist if there are enough data points.)

The bad thing is that the missing features are not well represented by the collected data set.
E.g. if we only collect data from males, the model trained may be poor for data from female because the underlying distribution for female may be quite different.  
This actually means that the distribution of the data is not stable.

Another problem is unbalanced data.
It means the the model may not learn the distribution for one class well.  
E.g. if most points are from male and only some points are from female,
even if we put the gender in the feature set, the female distribution may not be able to be learnt.  
Another example is the label set.
If one class has a lot of points and the other barely has any points,
discriminative methods may overly biased towards the class with many points.

In this sense, generative methods may be slightly better.
We need to learn the distribution of the features for each class
and predict the results using the combined distributions.

The dimension of the dataset seems to be limited by the smaller dataset with the least frequent label/class,
because it is hard to learn the distribution for that class if data points are not enough.


Stats and machine learning (thinking in progress, may not be correct)
---------------------------------------

For a data set of (xi, yi),
if we estimate the joint probability distribution of (x, y) (i.e. p(x,y)),
then we solve the problem.  
Because given p(x,y), for any xi, we can get the most likely y from p(xi, y).

This seems to imply that the joint distribution for each (xi,yi) is the same.  
Is this assumption a necessary requirement for the typical machine learning algo?  
Or is it only necessary for the generative machine learning methods?    
(again, generative method estimates p(x,y) in order to ultimately obtain p(y|x) thru Bayes' theorem.)  
And what happen if this assumption is invalid?


I think, if the assumption is invalid, we need to change the xi (or yi) to make the assumption valid,
at least for the generative methods.  


Actually, what we really care about is p(y|xi),
which seems to say that we don't care about the distribution of xi,
as long as we know the probability of y given xi (discriminative methods)

discriminative methods seems to be more relaxed on the distribution of xi.  
If we know the conditional distribution of y given all the elements inside on xi (xi is one data point, a vector, in this case),
then we can obtain the best y for the particular xi.

In the case of time series, when we do an autoregression of xt+1 vs xt,
clearly xt doesn't follow a single distribution, 
but (xt+1 - xt) follows a normal distribution (if such an AR is valid).  
This should be considered a discriminative method,
which implies xi doesn't have to follow a single distribution.
