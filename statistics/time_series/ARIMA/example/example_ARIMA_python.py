# run this this ~/anaconda2/bin/python
# reference: https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
# Data can be downloaded from: https://datamarket.com/data/set/22r0/sales-of-shampoo-over-a-three-year-period#!ds=22r0&display=line

import pandas as pd
from matplotlib import pyplot as plt

def parser(x):
	return pd.datetime.strptime('190'+x, '%Y-%m')

data_file = 'shampoo-sales.csv'
series = pd.read_csv(data_file, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
print (series.head())

series.plot()
img_name = "shampoo-sales-raw.png"
plt.savefig(img_name)
print ("the raw data is plotted in {}".format(img_name))

# the following graph is the 'autocorrelation' vs number of lags;
# so it should be x_{t} ~ x_{t-i}, where i is the x-axis
pd.plotting.autocorrelation_plot(series)
img_name = "shampoo-sales-autocorrelation.png"
plt.savefig(img_name)
print ("the autocorrelation graph is plotted in {}".format(img_name))

# after observing this graph, it seems the first 5 lags have significant correlation (cofficient >= 0.5)
# the p value (i.e. the parameter for AR) can be set to 5.

print ("let's try a ARIMA(5,1,0) model.")

from statsmodels.tsa.arima_model import ARIMA

model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp=0) # what is disp?
print (model_fit.summary())

# plot residual errors
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
img_name = "shampoo-sales-arima510-residuals.png"
plt.savefig(img_name)
print ("the residuals for ARIMA(5,1,0) is plotted in {}".format(img_name))

residuals.plot(kind='kde')
img_name = "shampoo-sales-arima510-residuals-kde.png"
plt.savefig(img_name)
print ("the residuals (kde) for ARIMA(5,1,0) is plotted in {}".format(img_name))

print (residuals.describe())


# continue to read the tutorial other times...
