Difference between fft and psd
-------------------------------------

Reference1: https://www.quora.com/What-is-the-difference-between-power-spectrum-and-power-spectral-density  
reference2: https://blog.mide.com/vibration-analysis-fft-psd-and-spectrogram

the direct results from fft is analogous to the discrete probability distribution,
while psd is analogous to the continuous probability distribution.

Given the results from fft, one way to derive the psd is to chop frequency to fixed small interval,
and compute the power density for each interval by summing up the power in this interval and divide it by the length of the interval.  
When the length of the interval goes to infinitely small, then the psd resultant will be closer to the true psd.  
In short, psd is like the differentiation function from the fft (i like need to square the coeffients first) w.r.t. frequency.


From taylor series to fourier transform
-----------------------------------------

Reference: https://math.stackexchange.com/questions/7301/connection-between-fourier-transform-and-taylor-series

taylor series is to decompose a function f(x) to a summation of ak * x^k.  
If we extend x to complex number, then taylor series naturally is to decompose a function f(z) to a summation of ak * z^k.

Z can be expressed as e^(i * theta) (assumed magnitude as 1 for simplicity),
then f(z) is f( e^(i*theta)) which can be seen as a function of theta f(theta). 

Also z^k = ( e^(i*theta) )^k = e^(i*k*theta)  (essentially it is a change of angle on the x-y plane)

therefore, f(theta) = summation of ak * e^(i*k*theta), which is the fourier transform.


Fourier series
---------------------------------

Reference: https://en.wikipedia.org/wiki/Fourier_series

a fourier series is a way to represent a function as the sum of simple sine waves.
It decomposes any periodic function into the sum of a set of simple oscillation functions,
namely sines and cosines (or equivalently, complex exponentials)

sin(x) is just a sin function of x. 
The function value is 0 when x is 0, 1 when x is pi/2, 0 when x is pi, -1 when x is 3pi/2 and 0 when x is 2pi.
One cycle is a change of a 2pi angle.

If we express the sin function as sin(rate of angle change * t ) = sin(2pi*f * t),
it means that if frequency f is large, then one unit of time t will results in a bigger angle change.

E.g. if f = 1 cycle per second (1hz), then from t=0 to t=1, the angle has changed from 0 to 2pi.  
Id f = 2 cycles per second (2hz), then from t=0 to t=2, the angle has changed from 0 to 4pi.

Another way is to use period T instead of f (T = 1/f). so t/T is the number of cycles completed so far.
And t/T * 2pi is the angle completed so far, which is somewhat more intuitive but exactly the same as t*f*2pi.

Sin(x) itself doesn't have the concept of frequency or period.
It is only when we use sin(2pi f * t) then the concept of frequency starts to appear.
From the sin() function itself, it simply receives a value and returns the corresponding value.

When f(x) is a periodic function with the overall period of P,
then f(x) can be expressed as A0/2 + SUM_of ( An * sin (2pi * n/P * x   + phi_n ) )

intuitively this means that f(x) is a sum of a dc component, 
a sin function with a period of T (i.e. frequence of 1/T) and phase chage of phi_1,
a sin function with a period of T/2 (i.e. frequency of 2/T) and phase change of phi_2,
and so on.

Like taylor series, these An and phi_n are something we need to find out.
It is like i write the shape of the function componenets first, and then find out the exact parameters for these sub functions.

Ultimately, after some manipulation, f(x) can be expressed as 
SUM_from_minusN_to_N( cn * e^(i 2pi n/P * x) )  
then cn an be computed as a function of P and x0, where P is the period and x0 should be any arbitrary value of x.

One implication seems that we need to know P before we can compute the coefficients.  

If P = 10 seconds, we will have coefficients for component frequencies = 1/10, 2/10, 3/10, and so on.

Example.
Let's take a look at this function s (it has 2 parts):
part 1: s(x) = x/pi for -pi < x < pi (a line between -pi and pi) and
part 2: s(x + 2pi*k) = s(x), for -pi < x < pi and k is a natural integer.

In this case P=2pi. choose x0 to be -pi.
Then we can compute an as 0 and bn as 2*(-1)^(n+1)/(pi*n).
Then s(x) = 2/pi * SUM_from_0_to_inf(bn)*sin(nx) for x-pi not_belong_to 2pi*Z 


fourier transform
-------------------------------

A very good tutorial: https://blog.mide.com/fourier-transform-basics

fourier transform decomposes a function of time into frequencies that make it up.

F(x) = INTEGRATE_from_-inf_to_inf( f(t) * e^(-2pi*i*t*x) * dt )

note that f(x) not_directly_equal_to f(t).

F(x) is a function of frequency, i.e. x is frequency.


Difference between fourier transform and fourier series
--------------------------------------------------------------

Fourier transform is an extension of the fourier series (!!!)
When the period of the represented function is lengthened and allowed to approach infinity.

Another reference: https://www.quora.com/What-are-the-differences-between-the-Fourier-series-and-the-Fourier-transform

fourier series decomposes a periodic signal into a sum of an infinite number of harmonics (sine and cosine functions)
of different frequencies and amplitudes.
These frequencies are discrete (not all frequencies are present).
The more components are considered (starting from the first), the sum is closer to the original signal.

Fourier transform decomposes a non-periodic signal into an infinite number of harmonics
having different frequencies and amplitudes.
These frequencies are continuous, no frequency is missing.
The sum in this case is an integral and can be estimated for simple functions
and for complex function can be estimated thru numerical integration.


My own understanding about fourier series to fourier transform
--------------------------------------------------------------------

Fourier series says that for a period signal with a period of T,
we can express it using component signals with periods of T/2, T/3, T/4, etc.

Notice that there won't be components having a period larger than T.

However, if you make T towards infinity, there will be 'more' components signals covering more frequencies/periods.

Fourier transform is to find out the 'spread' of the power along all frequencies,
which is a result of pushing the period to infinitely long. 


Discrete fourier transform
------------------------------------

The discrete fourier transform transforms a sequence of N complex numbers xn (real numbers are also complex number, and one example is the time series data sampled at a fixed sampling frequency)
to another sequence of complex numbers Xk (coefficients for each complex sindusoial components).

Xk = SUM_from_0_to_Nminus1(xn * e^(-2pi * i/N * k * n))

the frequency for each Xk is k cycles per N samples (???).

Anyway in practice the maximum detectable frequency is half of the sampling frequency.
And the number of samples determine the resolution from 0 to the maximum detectable frequencies.


A very good tutorial: https://blog.mide.com/fourier-transform-basics

using the formula above, k is the index of the frequency.
It has to be converted to the real frequency using the information of N and the sampling frequency/period.

The real frequency for k is k*fs/N (or k/(Ts*N)).  
The higher the fs, the higher the maximum frequency component to be obtained.

To obtain Xk, the most direct way is apply the formula for k=0, then again for k=1, and so on.
Ultimately for each k, we will have the complex number that represents both the magnitude and the phase shift at this 'k' frequency.

Note that a larger N will lead to a larger resolution but does not affect the maximum frequency component that can be obtained.

One important thing is that from the formula we know that we can get results for k=0 to k=N-1, 
but actually the higher frequencies components above fs/2 obtained are ghost components if the lower frequencies are really the true thing in the signal..  
Conversely, if the higher frequencies components are really the true thing in the signal, the DFT will give ghost components at lower frequencies, which do not exist in the original signal at all.  
The higher frequency components obtained are not useful anyway so we will discard them in DTF.  
All these mean that due to this limitation, to get the correct picture of the signal, we need to use a sampling rate at least twice as large as the largest freqency component in the original signal.  
If this requirement is not met, the we cannot really tell the low frequency component are the real low frequency component or the ghost component of the high frequency component.

E.g. when x(t) = sin(2pi 1000t) + sin(2pi 4000t + pi/4), using 10 samples at 100us (fs=10k Hz),
we will have non-zero components at frequency=1000 (correct), 4000 (correct), 6000 (wrong - ghost of 4000), 9000 (wrong - ghost of 1000).  
Therefore we have to discard components beyond 5k Hz!


Periodic signal
------------------------

For a periodic signal, there is a period T, which is the time taken for a cycle in the signal to repeat itself.  
Frequency f equals to 1/T.  
Frequency means how many repetition of the cycles in a second.
E.g. if the period is 0.1 second, the the frequency is 10 Hz.

There is another concept called angular frequency.  
It means the the 'amount' of angle changed (in rad) in one second.

We know that one cycle ressponds to an angle of 2pi rad,
so the angular frequency w is 2pi * frequency.  
Using the same example, the angular frequency is 20pi rad/s.

One example of a simple periodic signal is x(t) = cos(20pi * t)


aperiodic signal
-------------------------

Intuitively, an aperiodic signal is one that does not repeat itself.

However, like Taylor series, an aperiodic signal can be decomposed to a summation of multiple periodic signal. (not sure if this is always the case)


energy and power
-------------------

Let's say x(t) is a current signal.
The instaneous power of the device with R ohm and a current of x(t) is x(t)^2 * R (i.e. I^2 * R).  
The R is the scalling factor, so we can leave it out for simplicity.

If x(t) = 3 cos(100pi * t),
the instaneous power p(t) = |x(t)|^2 = 9/2 + 9/2cos(200pi * t) 

the average power of signal x(t) from t1 to t2 is INTEGRATE_from_t2_to_t2( p(t) ) / (t2 - t1),
where the numerator is the total energy of the signal from t2 to t1 (of course, the longer the period, the larger the energy).


Complex signal
-------------------------

What is a complex signal in the first place?  
We can treat it as a signal with partialy real, and partially imaginary.  
Certainly one single complex signal does not exist in the real world, 
but the addition of multiple complex signal can be used to represent one real signal,
as the imaginary parts can be clearly cancelled out in some ways.

But why do we want to represent a real signal by the addtion of multiple complex signal?  
Because complex signal is much easier to be handled mathematically.
(e.g. complex number can be differentiated easily, and the output is of a similar form.)

E.g. x(t) = 3 e^(j 100pi * t) = 3cos(100pi * t) + j 3sin(100pi * t)

total energy e from T/2 to -T/2 = INTEGRATE_from_T/2_to_-T/2 (|x(t)|^2) = 9T,  
because |x(t)| = 3.  
Note that in this case the || has a big effect, as it obtains the coefficient only
(e^(jx) is on a circle with radius = 1 regardless what x is, so the magnitude is 1 anyway)

average power p when T is very big = e/T = 9,
which is the same as the average power for the signal x(t) = 3cos(100pi * t)  
(is average power is determined by the amplitude only? not by frequency?)


Spectral_flatness or Wiener entropy
------------------------

Reference: https://en.wikipedia.org/wiki/Spectral_flatness

a high spectral flatness (approaching 1.0 for white noise) indicates that the spectrum has a similar amount of power in all spectral bands.  
A low spectral flatness (approaching 0.0 for a pure tone) indicates that the spectral power is concentrated in a relatively small number of bands - the spectrum would appear 'spiky'.

The spectral flatness is calculated by dividing the geometric mean of the power spectrum by the arithmetic mean of the power spectrum.


