Naive Bayes
--------------------

please read the README.md in direcotry machine_learning/generative_model/

Naive Bayes assumes that each element in x (a vector) is independent.  
then we can express p(x | y) = PRODUCTS( p(xi | y) ) where xi is an element in x (not each data point in this case).

explanation
----------------------

the sklearn.naive_bayes page actually provides a very good explanation:  
http://scikit-learn.org/stable/modules/naive_bayes.html

we know that in naive bayes ultimately the most important thing is to estimate p(xi | y) 
where xi is an element in the x vector.

p(y) also has to be estimated if there is no prior assumed.
but p(y) is simply the relative frequency of class y in the training set.

the different naive bayes classifiers differ mainly by the assumptions they make regarding the distribution of p(xi | y).

in sklearn, GaussianNB is a NB with p(xi | y) = normal distribution with an unknown mean and variance.

sklearn also has MultinominalNB and BernoulliNB.

for BernoulliNB, p(xi | y) = p(i | y) xi + (1 - p(i | y)) (1-xi)
where xi has to be binary.

MultinominalNB is for multinominally distributed data. (need to read more on this)  
it is one of the 2 classic naive bayes variants used in text classification
(where the data are typically represented as a word vector counts)
