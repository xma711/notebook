ARIMA
-------------

please read the [README.md for ARMA](../ARMA/README.md) first.

ARIMA stands for autoregressive integrated moving average model.

obviously, autoregressive is the AR, moving average is the MA.
What is new here is the I, the 'integrated' part.

reference: https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average

ARIMA models are applied in some cases where data show evidence of non-stationarity.  
(please read the [README.md for stationarity](../stationarity/README.md).)

ARIMA is usually denoted as ARIMA(p,d,q).
d is for the I part, and p and q are for the AR and MA.

we know that ARMA(p',q) equation can be written as:  
phi(L) xt = theta(L) et or  
( 1 - (phi1 L1 + ... + phi_p' Lp') ) xt = ( 1 + (theta1 L1 + ... + theta_q Lq) ) et


Assume now phi(L) has a unit root of multiplicity d (meaning?), then  
phi(L) = 1 - (phi1 L1 + ... + phi_p' Lp')  
= ( 1 - ( phi1 L1 + phi2 L2 + ... + phi_(p'-d) L(p'-d) ) ) (1 - L)**d

wait, what is the meaning of (1-L)**d when L is an operator?  
is it to expand it? e.g. when d = 2, (1-L)**2 = 1 - 2L + L2?  
let's try.  
let p' = 5 (in ARMA) and d=2.  
( 1 - ( phi1 L1 + phi2 L2 + phi_(5-2) L(5-2) ) ) (1 - L)**2  
= ( 1 - ( phi1 L1 + phi2 L2 + phi3 L3 ) ) (1 - 2L + L2)  
= (1 - 2L + L2) - ( phi1 L1 + phi2 L2 + phi3 L3 ) (1 - 2L + L2)  
= 1 - 2L + L2 - ( phi1 L1 - 2 phi1 L2 + phi1 L3 + phi2 L2 - 2 phi2 L3 + phi2 L4 + phi3 L3 - 2 phi3 L4 + phi3 L5  )  
= 1 + (-2 - phi1)L1 + (1 - 2phi + phi2)L2 + (-phi1 + 2phi2 - phi3)L3 + (-phi2 + 2phi3)L4 + (phi3)L5  
= a polynomial of L with degrees of 5 which is exactly p' in ARMA.

thus, ARIMA(p, d, q) can be thought as a particular case of an ARMA(p+d, q).

ARIMA(p,d,q) expresses this polynomial factorisation property with p = p' - d, where p' is the parameter in ARMA (i.e. ARMA(p', q)).

thus, the equation for ARIMA(p,d,q) can be written as:  
phi(L)(1-L)**d xt = theta(L) et

the unknowns are still the phi(s) and theta(s) but we have to determine p,d,q (instead of just p' and q in ARMA).


d in ARIMA
----------------------

ultimately d in ARIMA refers to 'differencing'.  
e.g. xt' = xt - xt-1

ARIMA(0,1,0) is xt = xt-1 + et, or xt - xt-1 = et  
ARIMA(0,2,2) is xt = xt-1 + xt-1 - xt-2 + (sth1) et-1 + (sth2)et-2 + et, or
xt - xt-1 = xt-1 - xt-2 + (sth2)et-2 + et

using ARIMA(0,1,0) or ARIMA(0,2,2), it is easy to see how data set is prepared 
(dependent variable is xt - xt-1 which is directly observable/obtainable, while et has to be estimated in a first step like the MA model)

if it is ARIMA(1,1,0), it should be xt - xt-1 = phi1 xt-1 + et,
where the dataset can be prepared quite easily too.

assume that we have fitted/trained an ARIMA model, what we predict from the model is the estimated change for the next step.
as we know xt, then xt+1 = xt + the estimated change.


next
--------------------
the next question is: how come taking out d from the p' helps dealing with non-stationary data?

the answer should be relating to the differencing thing in the ARIMA model.
but why differencing is able to handle non-stationary data is not so clear to me now.

the overall feeling is that if the data is not stationary, we try to make it stationary first.

all these AR, MA, ARMA, ARIMA ultimately is a linear regression,
but each of them requires data to be preprocessed by some ways to make it stationary before LSM can be applied.


the other interesting questions include:  
1. what is the relationship between these ARMA models and signal processing?  
2. what is the relationship between these ARMA models and (some) machine learning models?

need to think about these questions.


regarding q2, we can think it this way (using ARMA(p', q) as an example):  
in machine learning terminology, we want to predict x in the next phase.  
the raw data set is the all the xt.  
the features we want to obtain are xt-1 to xt-p' and et to et-q.  
then we preprocess the data to obtain these features.  
as we have the xt and the features now, we can use regression method to train a model.

in the ARIMA case, we want to predict the difference between the x in the next phase and the x in the current phase.  
then we can prepare the xt - xt-1 as the column of data to be predicted.  
then features can be obtained in the same way.  
subsequently a regression model can be trained.

the reason that we want to extract features in this way is that we somehow know that the data is not stationary
so we want to process the data in this way so that the training data (made of the features and Ys) are stationary.
