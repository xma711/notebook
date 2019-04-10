How to handle imbalanced dataset
--------------------------------------

Reference: https://www.analyticsvidhya.com/blog/2017/03/imbalanced-classification-problem/

The common methods include:  
	- oversampling  
	- undersampling  
	- some special classifiers that can handle imbalanced data better than others, such as gradient boosting


How to handle in practice
---------------------------------------

Interestingly, sklearn also has such a package 'imbalanced-learn' that can be used to do oversampling, undersampling or some classifiers.

Github Link: https://github.com/scikit-learn-contrib/imbalanced-learn  
API documentation: https://imbalanced-learn.readthedocs.io/en/stable/api.html

To install the package using conda: conda install -c conda-forge imbalanced-learn
