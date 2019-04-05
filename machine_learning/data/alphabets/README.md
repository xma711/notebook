Original data
----------------

The data is images pictures of alphabets.  
It is just 1 and 0 to represent black and white.


Useful info
-------------------

In fact, the alphabets are from a meaningful essay (this is something for us to find out).

One of the column is position of the letter in a word,
which has to be transformed to an one-hot encoder before feeding it to the model.


Shuffle and split data
---------------------------

The Mafefile is designed to shuffle the data and/or split the data to training set and test set with different size options.
