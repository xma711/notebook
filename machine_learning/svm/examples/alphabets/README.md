data
-------------------

The original data is for the assignment at masters/sem4_machine_learning_cs5339/kaggle  

the Makefile there has several options to manipulate the original training data. (obsolete)  
btw the labels in the original test data are deliberately incorrect; so we can only rely on the original train data

to get the data for this test, use the preprocess code and the Makefile at machine_learning/data/alphabets/ to generate the train and test data.  
after preprocessing, the position data inside will be transformed to one-hot vectors.  
shuffling and splitting help create the train and test data.


svm.py
-------------------------

this code runs on the data that have been preprocessed, NOT the original data!


