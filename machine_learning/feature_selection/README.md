Feature selection
-------------------------------

The way we encode real world objects as an instance space X is by itself prior knowledge about the problem.

There are some methods to do feature selections.

1. filter method.  
This way is that we access individual features independently of other features. 
Then we select the k features that achieve the highest score.  
The most straightforward approach is to set the score of a feature according to the error rate of a predictor that is trained solely by that feature.


2. greedy selection approaches.  
There is this forward greedy selection. 
We start with an empty set of features, and then gradually add one feature at a time to the set of selected features.  
Given the current set of selected features I, we go over each feature in the remaining features,
and apply the learning algo on the set of features I U feature_i.  
Then we choose the feature that yields the predictor with the smallest risk.  
Another greedy selection approach is backward elimination, 
which starts with the full set of features instead 
and then eliminate one feature at a time.

3. sparsity-inducing norms.  
Using l1 norm as the regularizer is able to induce sparse solution.

4. feature learning.  
PCA!! or other autoencoders.  
K-means can be used too. each example is map to a binary vector indicating which cluster it belongs to. (this is a bit naive..)  
Both k-means and PCA approaches can be regarded as special cases of autoencoders.  
These are similar to dictionary learning.


My own thinking
-------------------------

As we need to make sure each data point is iid,
it seems that we should try our best to capture all the inter-dependencies in one single data point.

E.g. in time series, the raw data of yesterday and the day before yesterday could affect today's behavior,
then we could include these 2 in one single data point.

Will this make different data points in the data set iid?  
Seems so..  
One way to approach this question is to ask one question:  
if we randomize the order of the data, will it matter?  
I.e. is ordering important here?  
It seems that if we include multiple days' data in one data point,
it does not matter if we randomize the order of the data.


How to handle time series data using machine learning methods?  
One reference: https://www.quora.com/Data-Science-Can-machine-learning-be-used-for-time-series-analysis

"rather than worrying about whether a time series is stationary, you can handle everything with features":  
	- break out seasonality using dummy variables - day of week, weekends, public holidays, seasons, time of day, etc  
	- introduce lags as features  
	- use the same transformations of features (e.g polynomials)

maybe instead of using day as a unit, we can use hour as the unit,
but introduce lags as the features.  
In this case, we seem to be able to handle different people's preferences of time on different activities (e.g. some ppl sleep early, some sleep late..)  
At the same time, we will also include the hour of the day, the day of the week into the features. 
The hour of the day will have a strong indication of what type of activity they will do.  

Maybe we can use hours of features to predict the features in the next hour; 
and then classify the predicted features to an activity..
