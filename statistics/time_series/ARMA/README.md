# Autoregressive-moving-average model (ARMA)

Firstly let's try to understand the AR and MA separately.


AR
-------------------
Reference: https://en.wikipedia.org/wiki/Autoregressive%E2%80%93moving-average_model

AR is the autoregressive part, which is easy to understand.  
E.g. xt = c + phi1 xt-1 + phi2 xt-2 + ... phi_p xt-p + epsilon_t, where epsilon_t (or simply et) is the white noise.
( btw this example can be summarized by the term AR(p) )

Wikipedia says that some constraints are necessary on the values of parameters so that the model remains stationary.
(what is the meaning of stationary?)
E.g. processes in the AR(1) model with |phi1|>= 1 are not stationary.  
(please read the [README.md for stationarity](../stationarity/README.md).)

MA
------------------------
MA refers to the moving-average model.

MA(q) refers to:  
xt = mu + et + theta1 et-1 + theta2 et-2 + ... + theta_q et-q  
where theta are the parameters of the model (unknowns),
mu is the expectation of xt (often assumed to be 0),
and the epsilons are white noise error terms.

The dataset for AR is intuitively easy to prepare.
E.g. To train an AR(1), all the xt will be y (the dependent variable) and xt-1 will be x (the independent variable).

However, how to prepare the dataset for MA?

MA seems to imply that xt is a linear regression of the error terms,
but how are the error terms known when preparing the dataset?

From https://en.wikipedia.org/wiki/Moving-average_model,
it says "a moving-average model is conceptually a linear regression of the current value of the series
against current and previous (observed) white noise error terms or random shocks.
The random shocks at each point are assumed to be mutually independent and to come from the same distribution,
typically a normal distribution, with location at zero and constant scale."

"Fitting the MA estimates is more complicated than it is in AR model,
because the lagged error terms are not observable.
This means that iterative non-linear fitting procedures need to be used in place of linear least squares."

In fact, based on https://www.it.uu.se/research/publications/reports/2006-022/2006-022-nc.pdf,
there seems to be multiple methods to estimate the parameters in MA model.

The most widely used technique is Durbin's method (DM).  
It is also known as the 2-stage LSM.  
Step 1: fitting an AR model of order p > q.
The estimated AR parameters can be obtained via LSM.
Then, estimates of epsilon_t can be computed as  
et = xt + phi1 xt-1 + phi2 xt-2 + ... + phi_p xt-p (wait.. shouldn't it be xt - (phi_i xt-i)?)

Step 2: as we have all the et, then MA can be solved by LSM.  
The dependent variable can be xt - et, and the independent variables can be et-1 to et-q.

Other methods can be read in the 2006-022-nc.pdf.


ARMA
-----------------------

ARMA is to combine AR and MA in one model.  
ARMA(p,q) refers to:  
xt = c + et + phi1 xt-1 + ... + phi_p xt-p + theta1 et-1 + ... + theta_q et-q.

I think similar to the MA model, the et terms in the ARMA model can be estimated using one AR model first.
Then ARMA can be mapped to a linear regression with all the dependent variables known.

When fitting ARMA, we have to pick p and q first.
In fact, when fitting AR model or MA model, we also have to pick the p for AR and q for MA in some ways.

There is AIC (Akaike information criterion) that can be used to finding p and q.
(may try to understand this in the future. for now skip.)


Applications of ARMA
---------------------------

ARMA is appropriate when a system is a function of a series of unobserved shocks (the MA part)
as well as its own behavior.  
E.g. stock prices may be shocked by fundamental information as well as exhibiting technical trending
and mean-reversion effects due to market participants.


Another way of writing ARMA equation
------------------------------------

Let L be the lag operator.  
L1 xt = xt-1

then the equation of ARMA becomes:  
xt = c + et + phi1 L1 xt + ... + phi_p Lp xt + theta1 L1 et + ... + theta_q Lq et  
then xt - (phi1 L1 xt + ... + phi_p Lp) xt = et + theta1 L1 et + ... + theta_q Lq et  
then ( 1 - (phi1 L1 + ... + phi_p Lp) ) xt = ( 1 + (theta1 L1 + ... + theta_q Lq) ) et

let phi(L) =  1 - (phi1 L1 + ... + phi_p Lp)  
and theta(L) = 1 + (theta1 L1 + ... + theta_q Lq)

the equation becomes:  
phi(L) xt = theta(L) et
