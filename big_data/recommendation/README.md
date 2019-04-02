Content-based
----------------

Each user has a matrix, each row is an item (e.g. a movie),
each column is a feature of this item (actors, e.g.).  
The values in the matrix is 1 or 0.  
For each user, we can have a vector of features he likes.  
Each member in the vector is the average of scores of a column in the matrix (sum of column scores divided by number of rows).

Any new item has a vector too. 
After calculating the cosine similarity of user's preference vector and an item's vector, 
we can have a list of scores for items for this particular user.  
Select the top k items as the recommendations for this user.

Cosine similarity = vector1 . vector2 / (|vector 1| * |vector 2|),  
the larger the value, the larger the similarity between vector 1 and vector 2.

This method is limited, as we can only recommend items that have features in user's preference matrix.


Collaborative
---------------------
A matrix.  
Rows are users, columns are items.  
Each cell in the matrix is a score representing the ranking of user i for item j.

If user 1 has no ranking for item k, then how to estimate?

Firstly, subtract the mean value from each row.
Mean value = sum of scores / number of available scores.  
In this way, each row is normalized. 
No-score items become neutral items.

And then we calculate the cosine similarity between user 1 and all other users.  
Pick the top m users.  
Then estimate the score for item k for user 1 by   
sum ( user i's score for item k * cosine_similarity ) / sum (cosine_similarity)

this method is better most of the time, because it can recommend any thing to user 1.

Check lecture notes for more details.
