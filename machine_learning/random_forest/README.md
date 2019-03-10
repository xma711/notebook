random forest in sklearn
--------------

An example to declare a random forest using sklearn:
```
forest = RandomForestClassifier( 
	n_estimators=num_trees, 
	min_samples_split=2, 
	min_samples_leaf=1, 
	max_depth=max_depth_rf, 
	random_state=1 ) 
```
there are more parameters that we can set.

n_estimators: is the number of trees in the forest

max_depth: is the maximum depth of a tree

these parameters can be used to control the complexity of the random forest.


cost function - Gini impurity
---------------------------

reference: https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity

Gini impurity is one way of measuring 'how good' a decision tree is.  
Btw another way is the 'information gain'.

Assume a tree is constructed in some way, then each leaf points to a label,
meaning if a data point is channeled to this leaf, then the data point is predicted to have this label.

for this leaf, the best case is that all the data points falling to this leaf really have this label.
let k be this label of the leaf, and pk be the proportion of data points channeled to this leaf that really havve this label.

then for this leaf, the Gini impurity is pk * (1-pk), meaning the proportion of the rightly labelled points x the proportion of wrongly labelled points.  
when all the points are rightly classified at this leaf, then the Gini impurity is 1*(1-1) = 0;
if only half the points are rightly classified, then it is 0.5*(1-0.5) = 0.25. (smaller is better)

the overall Gini impurity is just the sum of these gini impurities for each class.

actually, based on the formula, if there more than 1 leaf that has a particular label, then the gini impurity for this label has to be calculated together - i.e. treating these 2 leaves a 1 leaf (my understanding only).



How a tree is constructed
------------------------------

given that a cost function like Gini Impurity is used, how is a tree constructed ultimately?

based on wikipedia, "Algorithms for constructing decision trees usually work top-down,
by choosing a variable at each step that best splits the set of items."

if features are discrete, then when picking the root node, it just has to try each feature as the root node by splitting using the discrete values of this feature.  
then each feature will has a Gini Impurity score (or other cost metic).
the best feature can be picked as the root node.  
the second level may be similar. try each feature on the second level and pick the best one.
(question: each branch is tested independently or together? if it is together, the depth of each branch will be the same, which is not true.)

based on http://mas.cs.umass.edu/classes/cs683/lectures-2010/Lec23_Learning2-F2010-4up.pdf,
each branch is further constructed independently.
therefore, on the 2nd level of each branch, the feature can be different.

note that at each step, the whole training data is used.

for continuous feature, the algo preprocesses it to find out which ranges give the most useful information for classification purposes (refer to the pdf mentioned above).  
details are that it identify adjacent examples that differ in their true labels (ground truth),
generate a set of candidate thresholds midway between corresponding examples.  
using this way, it is kinda become discrete again.

(the next question is that given that we know how a tree is constructed, then how is a random forest is constructed?)


How random forests are constructed
--------------------------------------------

random forests consists of many decision trees.

each tree is trained using a subset of the features.

the results from the random forests are the average of all trees.

note that each tree has to be uncorrelated.

wikipedia says that "while the predictions of a single tree are highly sensitive to noise in its training seet, the average of many trees is not, as long as the trees are not correlated."

random forests is an extension of decision tree using the 'bagging' idea.
it decreases the variance of the model, without increasing the bias.
