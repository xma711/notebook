Gaussian classifier
----------------------------

Special application: event detection, e.g. vehicle type detection

for a given event, we can collect a time series of sensor data (assume one single modality for simplicity).  
These serve as the training data.

Assume the size of the single modality of sensor data x (a vector) = n (size of x = n),
we can compute the mean values (a vector) and the covariance matrix (sigma) for x (mu = E(x)). 

For every possible different event, we have to get a mean vector and covariance matrix.

Okay, now we have a model: normal distribution with mu and covariance matrix for each event.

Next, after we collect a new vector of sensor data, we have a question, which event does this vector of data correspond to?  
E.g. given a time series of sound values, what vehicle does the system detect?

We can use maximum likelihood estimation (MLE)!  
Note that this is not the only method. we can use MAP e.g.

So for each different event type, we compute the likelihood value:
L(mu, sigma ; x) = P(x | mu, sigma) = 1/(PI^n det(sigma)) * exp(- Transpose((x-mu)) (sigma_inverse) (x-mu))  
which is basically the normal distribution formula for n-dimensional vector.
(we log both sides to make the formula easier.)

Each different event will give a different value of likelihood.  
We just pick the maximum likelihood, 
and then conclude that with x we detects this event that leads to a maximum likelihood value.

Summary in a formula: C(x) = arg max_j=1,..,M P(x | wj)  
where M is the total number of event types, 
wj is the event, represented by the mu and sigma in the Gaussian model.

Refer to EE5132 chapter 10 for more details.


For multiple measurements from multiple sensor modalities, 
simply concatenate the multiple xk vectors to a long x vector. 
Then compute the mean and sigma for x too. 
The rest is the same.

