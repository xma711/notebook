hidden markov model
-------------------------

great news. sklearn has this model.  
reference: http://scikit-learn.sourceforge.net/stable/modules/hmm.html

will study this model in the future.


initial understanding
---------------------------

reference: "A concrete example" in https://en.wikipedia.org/wiki/Hidden_Markov_model

the only observation we have is a sequence of activities,
such as walk, shop and clean (by person A).

we can assume that these activities are emmited by some states, such as different weathers: rainy and sunny.  
note that we do not know the states for each observation.

there is an unknown transition probability matrix.   
if we have this matrix, we can use it to calculate the probability distribution of the states 
given the probability distribution of the states in the last interation.

note that here we assume the state transition has markovian property, 
so the probability distribution of the next iteration is only dependent on 
the probability distribution of the last iteration.

also, there is an unkown emission probability matrix.  
if we know this matrix, given a probability distribution of the states,
we can calculate the probability distribution of the activities.

overall, the whole point here is that given the observations only,
we want to estimate the transition probability matrix and the emission probability matrix.

once we know the estimated transition probability matrix and emission probability matrix,
then given an observation, we will be able to estimate the current probability distribtuion of the states,
and in turn we can estimate the probability distributions in the next iteration
and the probability of the activities in the next iteration. 
