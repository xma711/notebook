FFT
-------------

FFT is fast Fourier transform, which is to convert a time series data to frequency-domain data.

Python has a FFT function, in both numpy and scipy.

Assume we use numpy's fft.

Let's say x is the time series data with a period of dt.
The number of elements inside x is N.  
When we do fftx = np.fft.fft(x)
we will get an array fftx with the same length of x (i.e. N).

Now the question is what is the frequency of each element in fftx corresponds to?

One thing is that fftx is somewhat symmetric, only the first half is useful.  
Therefore we can do fftx = fftx[0:N/2] to chop half of it from itself.

To get the corresponding frequency, we can do this:
freq_fftx = np.linspace(0, 1/(2*dt), N/2 )  
which means the minimum freq is 0 and the maximum frequency is 1/(2*dt) and there will be N/2 elements.

The we can plot it using: plot(freq_fftx, abs(fftx)**2)  
where abs(fftx)**2 is the power spectrum


Wait!! is dt the sampling period? should be yes.

Another question: do we need to divide fftx by n to normalize the vector?


Applying window function on the time series data before applying fft
--------------------------------------------------------------------------

If the time series data does not start with a 'good' number and end with a 'good' number, 
the fft may give funny results.

The solution is to apply a window function on the original time series data.

This window function ultimately is to actively distort the original time series,
so as to amplify some parts while depressing some other others.
After applying the fft on the distorted time series, the results will be more accurate.

One popular choice is the Hanning function.
