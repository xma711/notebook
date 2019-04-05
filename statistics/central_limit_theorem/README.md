Central limit theorem
------------------------------

A variable of something can follow any distribution.
E.g. height of a person could be normal distribution; the number from the dice could be a uniform distribution.

Now the question is: what is the distribution of the sum or average of N observations?

One example is that, if we throw the die 100 times, and get the sum or average, then we ask one person:
what do you think is the distribution of this sum or average?

If you look at the results, of course there is one single number for the sum or average.
But without looking at the result, there are many likely answers for this sum or average, but some answers are more likely than others.
In another words, there should be a distribution for this sum or average.

Interestingly, this distribution for sum or average is kinda independent from the single observation's distribution,
and it turns out to be following a normal distribution!

The parameters for this normal distribution (let's say the mean; but similar for sum) are:  
	mean is the average of the N throws.  
	variance is the single observation's variance divided by N.


In practice, how to observe this distribution experimentally?  
To do it, let's define N as 100. then we do 100 throws and note down the average.
Then repeat the whole process to note down another average.
And so on.  
Intuitively, any of the average should close to 3.5 as we use 100 throws in this case, but there is still a spread.
If we take this average as the variable we are interested at and plots all the averages on a graph, 
we will observe a normal distribution if the number of averages is large enough.

