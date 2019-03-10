fft
-------------

fft is fast fourier transform, which is to convert a time series data to frequency-domain data.

python has a fft function, in both numpy and scipy.

assume we use numpy's fft.

let's say x is the time series data with a period of dt.
the number of elements inside x is N.  
when we do fftx = np.fft.fft(x)
we will get an array fftx with the same length of x (i.e. N).

now the question is what is the frequency of each element in fftx corresponds to?

one thing is that fftx is somewhat symmetric, only the first half is useful.  
therefore we can do fftx = fftx[0:N/2] to chop half of it from itself.

to get the corresponding frequency, we can do this:
freq_fftx = np.linspace(0, 1/(2*dt), N/2 )  
which means the minimum freq is 0 and the maximum frequency is 1/(2*dt) and there will be N/2 elements.

the we can plot it using: plot(freq_fftx, abs(fftx)**2)  
where abs(fftx)**2 is the power spectrum


Wait!! is dt the sampling period? should be yes.

another question: do we need to divide fftx by n to normalize the vector?


applying window function on the time series data before applying fft
--------------------------------------------------------------------------

if the time series data does not start with a 'good' number and end with a 'good' number, 
the fft may give funny results.

the solution is to apply a window function on the original time series data.

this window function ultimately is to actively distort the original time series,
so as to amplify some parts while depressing some other others.
after applying the fft on the distorted time series, the results will be more accurate.

one popular choice is the hanning function.
