Gradient Boosting
--------------------------------

Reference: https://en.wikipedia.org/wiki/Gradient_boosting

On the high level, the logic is quite simple.

Let's say at stage m we managed to find a weak learner Fm for a classification problem.  
Our aim in the next stage (i.e. m+1) is to find a better model Fm+1(x) = Fm(x) + h(x),
where h is the hypothesis from a hypothesis class.

If h is perfect, it implies Fm+1(x) = y, or Fm(x)+h(x) = y,  
or h(x) = y - Fm(x).  
What it means is that if h is perfect, we can classify each x correctly to the corresponding y using Fm+1.

At stage m+1, Fm(x) is known, and y is known, so y-Fm(x) is also known (y-Fm(x) is the residul).
Then in order to find h, we can fit h(x) = y, which is just another usual fitting problem.

This process can go on until we reach a small enough error or a stationary error.

Like other boosting methods, gradient boosting is able to combine week learners into a single strong learner.


Other notes
------------------

The book "Artificial intelligence, machine learning, and deep learning" chapter 1 mentions that 
"In 2016 and 2017, Kaggle was dominated by two approaches: gradient boosting machines and deep learning."


How to use
------------------------------

Reference: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html

sklearn has a package, so it is quite straightforward to use it.
