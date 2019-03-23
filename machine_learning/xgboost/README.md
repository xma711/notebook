XGBoost
------------------------

Reference: https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/

"XGBoost is an implementation of gradient boosted decision trees designed for speed and performance."

Some information about Gradient Boosting can be found at [the README.md for Gradient Boosting](../gradient_boosting/README.md)

The name XGBoost stands for eXtreme Gradient Boosting.

XGBoosting is fast comparing to "other implementations of gradient boosting".

XGBoosting is the "go-to algorithm for competition winner on the Kaggle ... platform".

"When in doubt, use xgboost." - Mad Professors.

Both regression and classification are supported by gradient boosting, and of course by XGBoost.


Installation
---------------------------

The default conda installation doesn't have the xgboost package.

To install it, using: conda install -c conda-forge xgboost  
(Reference: https://anaconda.org/conda-forge/xgboost)

After installing xgboost, if there is any problem importing the sklearn packages,
then just update all the packages in the conda env: conda update --all


Usage
--------------------------

Reference: https://xgboost.readthedocs.io/en/latest/python/python_api.html

For classification, there is a XGBClassifier from xgboost.

The way to use it is quite similar to the sklearn packages.  
The standard fit() and predict() functions are supported.

In fact, it can be used inside sklearn's pipeline.
