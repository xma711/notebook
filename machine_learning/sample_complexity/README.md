sample complexity
---------------------

reference: https://en.wikipedia.org/wiki/Sample_complexity

the right question to ask is:  
what is the sample complexity of a machine learning algorithm?

e.g. what is the sample complexity of the "empirical risk minimization" algorithm (ERM)?

note that "algorithm" in this case can be as general as "empirical risk minimization".  
(other examples of "algos" include structural risk minimization (SRM) and regularized loss minimization (RLM) )
we don't really have to care about how exactly this ERM is performed, 
and we only have to know that ERM will be performed and the hypothesis with the minmium risk will be selected.

the whole point of sample complexity is not to calculate a sample size in order to
get a hypothesis that results in a very small risk (error) for population.  
the correct thinking should be, given a hypothesis class, 
the point about sample complexity is to calculate a sample size 
so that we will be able to find a hypothesis whose pupulation risk is not too larger than the population risk of the best possible hypothesis from this hypothesis class.

this means that when sample complexity is small, it does not mean we can find a good solution when sample size is large. 
it only means that we are able to find a solution that is not too bad compared to the best solution in this hypothesis class.  
if the best solution in the hypothesis class is already very bad, 
then no matter how easily achivable the sample complexity is, we can't get a globally good solution.

also, what exactly is the meaning of risk?  
(reference: textbook chapter 2)  
the risk to be calculated actually depends on the loss function.  
with different loss function, the risk will be calculated differently.  
however, whatever loss function is used, conceptually there is a risk for population given a h and an empirical risk for the sample given a h.  
therefore, we can still claim that sample complexity of an algo is about calculating a sample size such that the algo will be able to obtain a h that has risk not much more than the best possible risk on population, no matter what loss function is used.  
(actually, this means that, when different loss function is used, 
the sample size required to achieve a certain error bound can be different. correct??)


no free lunch theorem (NFL)
---------------------------

NFL means that if we allow any distribution for X and Y, then given an algorithm (e.g. ERM),
we can always find a distributiion of X and Y such that the learning algorithm will fail to learn the globally optimal function, 
no matter how large the sample is.

e.g. given a hypothesis class that contains all possible functions (functions from SVM, random forest, neural network and more),
and a learning algorithm being the ERM,
there is not finite sample size to learn the target function for all distributions of X and Y.

however, if we limit the "size" of the hypothesis class (this size can be represent by the VC dimension of the hypothesis class),
then the sample complexity is finite, even if the distribution of the X and Y is not restricted.

this implies the importance of prior knowledge.  
if we don't even know which hypothesis class is the better one, 
what we can do are: 
randomly pick one --> this may lead to a bad best possible hypothesis,  
or  
pick a very general class --> this leads to a high requirement on the sample size.  
(both ways have some issues.)
 
overall, if we want to have a finite sample complexity, we can do either:  
	- limit the hypothesis class without limiting the distribtuion of X and Y (discrimative methods???) OR
	- limit the space of distribution for X and Y. (e.g. via a parametric approach)


the whole story recapped
----------------------------------

reference: https://en.wikipedia.org/wiki/Sample_complexity

sample complexity of an algo is the sample needed for the algo
to find a good solution for the population 
compared to the best possible solution for the population.

given an algo, if we allow any distribtuions for X and Y,
is there a finite sample size such that the algo will be able to learn a good solution for population compared to the best possible solution for population?

the answer is No, due to the no-free-lunch theorem (NFL).

NFL says taht for an algo, given any sample size, we can always find a distribtuion of X and Y
such that the algo fails to learn a good solution for the population.

then what can we do?  
1. limit the probability distribution space for X and Y. e.g. we can assume the distribution is parameterized and learn the parameters using methods like MLE.  
2. limit the hypothesis class while allowing any distributions for X and Y.  
e.g. we can set the hypothesis class to linear functions. 
then the sample complexity is finite, because linear-functions class has a finite VC dimension.

good solution and overfitting
-------------------

reference: textbook chapter 2

just now when we mention "good solution" or "good hypothesis",
we are talking about general risk/error, not sample risk/error.

interesting, so far we have not talked about test data yet.

this means that, when the vc dimension of the hypothesis class is finite
and when the sample size is large enough,
the ERM algorithm is able to find a solution that is not overfitting!!

i think the intuition is that, when there is enough sample,
the sample starts to represent the population well. 
then there is less likely for ERM to find a solution that does not fit the population.

one natural question is that, then what is the use of the test dataset?  
refer to section "test dataset" for answer.


uniform convergence
-------------------------

intuitively given a hypothesis class, if this condition holdes:  
	"when sample size > a certain number  
	each h from the hypothesis class results in a sample risk that is close to the population risk",  
then we can this hypothesis class has the uniform convergence property.

it follows that if H has unifrom convergence property,
the ERM algo is a agnostic PAC learner for H.
i.e. ERM is able to find a good h for population compared to the best possible h for population.


approximation error and estimation error
--------------------------------------------

Let hs be the h learnt by ERM based on sample s.  
LD(hs) is the population error.

we can decompose LD(hs) to LD(hs) = appr_error + est_error,  
where appr_error = min{over H} LD(h) 
and est_error = LD(hs) - appr_error

the approximation error is the minimum risk achivable by a predictor in the hypothesis class, 
which does not depend on the sample size.  
enlarging the hypothesis class can decrease the appr_error.

the estimation error results because the empirical risk is only an estimate of the true risk.  
the quality of this estimation depends on the training set size and
on the complexity of the hypothesis class.

we face a tradeoff, the bias-complexity tradeoff.  
in many cases, the empirical research focuses on designing good hypothesis classes for a certain domain.

note that by now we are always talking about one single set of training data (there is no test data).  
will the existence of the test data change the bias-complexity tradeoff?? (the answer is no. read the next section.)


is it possible to reduce approximation error while maintaining estimation error?
---------------------------------------------

firstly, let's look at training error along.

if we get the best h1 from H1 using ERM and the best h2 from H2 using ERM,
and then pick the better h from {h1, h2} in terms of training error as the overall choice of hypothesis h (this is exactly the same as pick h from H = {h1, h2} using ERM), 
will this h better than either h1 or h2 in terms of population error?

the answer is not necessarily.  
because this h may be overfitting the training data (large estimation error).  
if the sample size is not enough for the full H, the h chosen in this case is very likely overfitting the training data.

therefore, looking at training error alone, this does not violate the bias-complexity tradeoff.  
even if we run EMR on 2 different hypothesis classes, such as SVM and logistic regression, the best ERM h is not necessarily the better one compared to the best ERM h from either SVM or logistic regression.

to ensure the EMR h from {H1, H2} is better than h1 or h2 in terms of population error, we do need more data to do the training.

on the other hand, if we look at the test error and pick the h from {h1, h2} such that h has as smaller test error, 
is h better than either h1 or h2??

the answer seems yes. (but it is wrong when we do this on many Hi!!! read on.)

this time, the h chosen is not necessarily the same as the EMR h from the full H.

does this mean that the existence of test data makes the bias-complexity tradeoff invalid?  
in another words, with the test data, can we reduce the bias (approximation error) and also reduce the estimation error?  
in another another words, does the bias-complexity trade-off only apply when we use the training error along to decide the best h?

one example is that: we run ERM on different hypothesis classes with the sample,
and then pick the h that leads to the smallest test error.  
does this violate the bias-complexity trade-off?

another thing is that if we know the sample size is not enough for the full H, can we chop H up and then run EMR on each Hi, 
and at the end we choose the hi that results in a smallest test error?  
this method should be nicknamed "Test risk minimization"..  
(this seems more complicated than i thought because if there are many Hi, then the test data is essentially the "2nd-level" training data,
and there is a possibility to overfit the test data..)

the h that results in a smallest test error is no longer the best for the population, because this h could be overfitting the test data!!!!!  
This means that the Test Risk Minimization algo has a limit itself!!!  
when the number of hypothesis classes increases to a certain limit, the population error actually increases, because the overall estimation error increases!!!!

therefore, it seems that with a test dataset, the bias-complexity tradeoff is still there!!!  
because while we are pushing the approximation error to 0, the estimation error starts to increases when the number of hypothesis classes reaches certain number!!!

to reduce the estimation error further, there is no way but to increase the sample size.


test dataset
------------------------

reference: textbook chapter 11

so, for the PAC learnable case, since we are able to get the sample complexity for the ERM algo,
why do we still want to use a test dataset in practice?

a few reasons:  
1. the sample bound we obtain from the VC dimension is for all hypothesis in the class and for all distributions of X and Y,
so the bound can be quite hard to achieve.  
2. the difference between the test dataset risk and the true risk has a smaller bound

therefore, using a test dataset (i.e. validation set) is easier for us to estimate the true risk in practice.

when the test error is large,
we have to rely on both the training error and the test error to 
deduce which component of the sample error is large:  
is it the approximation error or the estimation error?

if it is the approximation error being too large, 
then we should consider expand the hypothesis class (e.g. increase the degrees in the polynomial function) 
or completely change a hypothesis class.

if it is due to a large estimation error, 
then we can increase the sample size if possible.  
we can also consider reduce the hypothesis class complexity.  
(any other ways? check testbook chapter 11)

again, estimation error is the difference between the sample error and the true best possible error.  
again, when the hypothesis class becomes richer, the approximation error will drop while the estimation error increases (given the same sample size).


boosting
-------------------------

is there a way to tune the approximation error (bias??) and estimation error smoothly?

answer: yes.  
example: adaboost.

check chapter 10 for the details of adaboost algorithm.

the idea behind boosting is that  
given a weak learner (e.g. it is a simple hypothesis class and the ERM returns a h that only performs slightly better than random guess),  
theoretically and practically there is a way to boost it to a strong learner.  
how?

one way is adaboost.  
give each example a weight.  
the weights will be changed in the next round. the example that has a wrong prediction will have a higher weight.  
each round the weak learner will return a ht.  
ultimately the hs = linear combination of ht

the number of rounds = T.  
it can be shown that T is the single parameter to tune the appr_error and est_error tradeoff.  
when T is large, appr_error is smaller while est_error is larger.  
using model selection method to find a good T


compuational complexity
--------------------------------

reference: chapter 8

from stat's point of view, when the sample complexity of an algo (e.g. ERM) is 'okay',
we say the problem is learnable using this algo (e.g. ERM)..

however, from computational efficiency's point of view, this may not be true. 

e.g. for the finite class, the class size can be huge, 
and an exhaustive search (ERM) is computationally inefficient.

therefore in practice we have to consider both sample complexity and computational complexity.

for many hypothesis classes and the loss function,
the ERM is very hard to learn, even when the sample size is large enough. (see chapter 8 for some examples)

the linear predictor hypothesis class is popular because it is usually computationally efficient to perform ERM over this class. (not all)

e.g. for logistic regression (with log loss function) and linear regression (with square loss function), it is computationally efficient to learn.

for halfspace with the realizability assumption (0-1 loss), it is also computationally efficient to learn.  
however, for halfspace without the realizability assumption (0-1 loss), it is NP-hard to learn. (ultimately we will use SVM to 'solve' this)


convex function and RLM
--------------------

reference: chapter 12 and 13

convex-Lipschitz-bounded and convex-smooth-bounded are 2 families of learning problems that are learnable.

question: by what algorithm? ERM?  
answer: the 2 families of learning problems are learnable by ERM to a certain extend only; not true for all.

then by what algorithm?  
regularized loss minimizaation is able to learn all convex-lipschitz-bounded and convex-smooth-bounded learning problems.

intuitively, the complexity of the hypothesis is measured by the value of the regularizaton function, and the algorithm balances between low empirical risk and simpler or less complex hypothesis.

one of the most simple regularization function is lambda * ||w||^2, where ||w|| is l2 norm. this type is called Tikhonov regularization.

a usual linear regression + a l2 norm regularization is called ridge regression.  
it can be shown that ridge regression is pac learnable.

