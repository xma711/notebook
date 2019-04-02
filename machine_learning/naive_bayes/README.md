Naive Bayes
--------------------

Please read the README.md in directory machine_learning/generative_model/

Naive Bayes assumes that each element in x (a vector) is independent.  
Then we can express p(x | y) = PRODUCTS( p(xi | y) ) where xi is an element in x (not each data point in this case).

Explanation
----------------------

The sklearn.naive_bayes page actually provides a very good explanation:  
http://scikit-learn.org/stable/modules/naive_bayes.html

we know that in naive bayes ultimately the most important thing is to estimate p(xi | y) 
where xi is an element in the x vector.

P(y) also has to be estimated if there is no prior assumed.
But p(y) is simply the relative frequency of class y in the training set.

The different naive bayes classifiers differ mainly by the assumptions they make regarding the distribution of p(xi | y).

In sklearn, GaussianNB is a NB with p(xi | y) = normal distribution with an unknown mean and variance.

Sklearn also has MultinominalNB and BernoulliNB.

For BernoulliNB, p(xi | y) = p(i | y) xi + (1 - p(i | y)) (1-xi)
where xi has to be binary.

MultinominalNB is for multinominally distributed data. (need to read more on this)  
it is one of the 2 classic naive bayes variants used in text classification
(where the data are typically represented as a word vector counts)
