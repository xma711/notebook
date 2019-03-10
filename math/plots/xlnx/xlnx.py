#!/home/xma/anaconda2/bin/python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def get_x_y():
	n = 100
	x = np.linspace(0.0001, 1, n)
	y = [ (xi* math.log(xi)) for xi in x]
	return [x,y]

def plot_x_y(x, y, title):
	plt.plot(x,y)
	plt.title(title)
	plt.show()

def plot_xlnx_0to1():
	x,y = get_x_y()
	plot_x_y(x, y, 'xlnx')

def plot_negative_xlnx_0to1():
	x,y = get_x_y()
	y = [(-1*yi) for yi in y]
	plot_x_y(x, y, '-xlnx')

# plot
# plot_xlnx_0to1()
plot_negative_xlnx_0to1()

## the results show that if x is too small or too big (in the 0 to 1 range), -xlnx will be very small.
## if x is somewhat in the middle, -xlnx will be large.
##
## what about the sum of (-xi*ln(xi))? if most xi are small (their -xlnx will be small), and a few xi are large (their -xlnx will be also small), the sum will be small (power coefficients of fft of a spike signal);
## if most of xi are small but not that small, their sum may be large (power coefficients of fft of white noise)
