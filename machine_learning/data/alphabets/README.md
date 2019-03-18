Original data
----------------

The original data can be downloaded from dropbox, the machine learning module, kaggle assignment.

The data is images pictures of alphabets.  
It is just 1 and 0 to represent black and white.

In fact, the data is a meaningful piece of essay (this is something for us to find out).

One of the column is position of the letter in a word.  
In the assignment i used the raw value, which is wrong.

I should convert it to a vector with only one 1 in the vector.
That's the main thing i am going to do here.

This is done by the preprocess.py


shuffle and split data
---------------------------

Beside, i have to shuffle the data and split them to a training set and test set.

There is actually another test set; however, we don't know the true results.
That's why we have to rely on the original training set for both training and testing.

The Mafefile is designed to shuffle the data and/or split the data to training set and test set with different size options.
