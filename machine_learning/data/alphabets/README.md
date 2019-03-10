original data
----------------

the original data can be downloaded from dropbox, the machine learning module, kaggle assignment.

the data is images pictures of alphabets.  
it is just 1 and 0 to represent black and white.

in fact, the data is a meaningful piece of essay (this is something for us to find out).

one of the column is position of the letter in a word.  
in the assignment i used the raw value, which is wrong.

i should convert it to a vector with only one 1 in the vector.
that's the main thing i am going to do here.

this is done by the preprocess.py


shuffle and split data
---------------------------

beside, i have to shuffle the data and split them to a training set and test set.

there is actually another test set; however, we don't know the true results.
that's why we have to rely on the original training set for both training and testing.

the Mafefile is designed to shuffle the data and/or split the data to training set and test set with different size options.
