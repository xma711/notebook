Understand Bayes' Rule again
------------------------------------

The rule: p(y|x) = p(x|y)p(y) / p(x) = p(x|y)p(y) / INTEGRATE( p(x|y)p(y)dy )

question: why do we want to express p(y|x) in terms of p(y) and p(x|y)?

Explanation:  

let y be a result of {cat, dog}. x be the images.  
P(y|x) means that given an image, we want to find the probability of y being cat and dog.  
(so that if p(y=cat) is higher, we can classify the image as cat; vice versa.)  

In reality, we can collect data: cat pictures and dog pictures.  
With these 2 sets of data, we can find the distribution of x for the cats pictures, and that for dog pictures, i.e. p(x | y = cat) and p(x | y=dog).  
Of course we know p(y) too, either because we can make an assumption that the distribution of y follow the ratio of number of cat and dog pictures.  

Therefore, in reality, we usually do know p(x|y) and p(y), and then we want to calculate p(y|x).


Bayes' rule
------------------

P(A|B) = P(A) * P(B|A)/P(B)

P(A) and P(B) are probabilities of A and B without regard to each other.

P(A|B), a conditional probability, is the probability of observing event A given that B is true.

P(B|A) is the probability of observing event B given that A is true.


Bayesian interpretation
------------------------------

Probability measures a degree of belief.
Bayes' theorem then links the degree of belief in a proposition before and after accounting for evidence.

P(A): the prior, is the initial degree of belief in A.  
P(A|B): the posterior, is the degree of belief having accounted for B.  
P(B|A)/P(B): represents the support B provides for A.

Reference: https://en.wikipedia.org/wiki/Bayes%27_theorem


intuition
----------------------

Ref: https://www.quora.com/What-is-an-intuitive-explanation-of-Bayes-Rule?redirected_qid=528835

person A says, money can't buy happiness, because only 10% of happy people are rich.  
Wait, this is wrong. this is P(Rich | happy). 
The correct info should P(happy | rich).

Bayes' theorem tells us how to calculate the other, reversed statistic using two more info:  
the percentage of people overall who are happy (let's say 40%) and  
the percentage of people overall who are rich (let's say 5%).

Then P(happy | rich) = P(happy) * P(rich | happy) / P(rich) = 0.4 * 0.1/0.05 = 0.8

"Let's say the population of the whole world is 1000, just to keep it easy. 
Then Fact 1 tells us there are 400 happy people, 
and the Harvard study tells us that 40 of these people are rich. 
So there are 40 people who are both rich and happy. 
According to Fact 2, there are 50 rich people altogether, 
so the fraction of them who are happy is 40/50, or 80%." 


Bayes' rule
------------------

(What is the difference between Bayes' theorem and Bayes' rule? No difference.)

Bayes' rule simply states that  
posterior (after) odds equals prior (before) odds times Bayes factor.

Bayes's rule relates that odds of event A1 to the odds of event A2 before (prior to)
and after (posterior to) conditioning on another event B.

Bayes factor (or likelihood ratio) = conditional probabilities of event B given that
A1 is the case or that A2 is the case, respectively.

When A1 = A, and A2 = not A, the rule is simplified to:  
O(A|B) = O(A) * F(A|B)

