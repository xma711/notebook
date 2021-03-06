Stationary process
--------------------------

Reference: https://en.wikipedia.org/wiki/Stationary_process

a stationary process is a stochastic process whose unconditional joint probability (should be p(x,y)) does not change when shifted in time.  
Consequently, parameters such as mean and variance also do not change over time.

Since stationarity is an assumption underlying many statistical procedures used in time series analysis,
non-stationary data is often transformed to become stationary.


Cause of violation of stationarity
----------------------------------------

The most common causes is a trend in the mean, 
which can be due either to  
1. the presence of a unit root or  
2. of a deterministic trend (such a non-stationary process is called a trend stationary process)

A trend stationary process can easily be transformed into a stationary process by removing the underlying trend (by the AR part in ARMA or ARIMA),
which is solely a function of time.

Processes with one or more unit roots can be made stationary through differencing (e.g. [the differencing in ARIMA](../ARIMA/README.md)).

There is another type of non-stationary process that does not include a trend-like behavior - a cyclostationary process,
which is a stochastic process that varies cyclically with time.


