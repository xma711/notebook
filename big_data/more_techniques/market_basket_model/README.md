objective
----------------

find association between items in a dataset, using the market-basket model.

e.g. given a set of transactions (the products that each shopper buys in one trip),
find rules that will predict the occurrence of an item based on 
the occurrence of other items in the transactions.
(implies co-occurrence, not causality!)

the market-basket model
---------------------------

items: e.g objects sold in a supermarket 

baskets: each is a small subset of items; e.g. objects a customer buys in a shopping trip

our interests: relationships between items (not baskets)  
	- e.g. people whol bought diaper tend to buy beer

note that this is just the model and the supermarket imagination is just a convenience.  
the model can be applied to many different applications:  
	- recommendation system in amazon (similar to the supermarket example)  
	- with items being documents, a basket being a containers that contains documents with a same sentence, find plagiarism  
	- with items being drugs and side-effects, a basket being a patient who takes drugs, detect combinations of drugs that lead to particular side effects


technical - preliminaries
--------------------------

items: all possible items in the study. e.g. all products in a supermarket

itemset: a collection of one or more items  
	- with num(items) = 10, num(possible itemsets) = 10c1 + 10c2 + .. + 10c10 = 10 + 45 + 120 + ... + 1 = 2^10 - 1 = 1023 (need to verify)

k-itemset: an itemset that contains k items  
	- with num(items) = 10, num(k-itemset) =  10 c k

support count: the number of occurrence of an itemset in all itemsets that have happened  
	- all the itemsets that contain a subset == this particular itemset need to be counted  
	- e.g. support_count({milk, diaper}) = count({milk, diaper}) + count({milk, diaper, beer}) + count({milk, diaper, x, y, z ...}) + ...  

support of an itemset: fraction of baskets that contain an itemset. it is a ratio, which = support_count(itemset)/count(all itemsets happened)

association rule: for an itemset = X union Y (while X intersects Y = Null set), 
X -> Y is an association rule that a basket containing X is likely to contain Y  
	- there are many rules that can be created from an itemset.  
	- note that X and Y must form the full itemset. therefore, the number of possilbe rules from this k-itemset = kc1 + kc2 + .. + kc(k-1)  
	- with num(all items) = d, each itemset formed from this d items can have many rules; and the total number of rules can be overwhelmingly large with a big d

support of a rule: the fraction of baskets containing both X and Y

confidence of a rule: the fraction of baskets cotaining both X and Y with respect to the number of baskets containing X

support and confidence are two metrics to see if a rule is valid.

The association rules (AR) mining task: given minsup (minimun support threshold) and minconf (minimum confidence threshold), 
find all rules that have support >= minsup and confidence >= minconf

the most direct but inefficient method is to list down all the possible rules based on the items, 
and then check each possible rule's support and confidence.  
This can be extrememly slow with a big number of items (d).


Mining Assocation Rules: Decoupling
---------------------------------

observations:  
	- rules originating from the same itemset have identical support but can have different confidence  
	- why support is the same? the support of each itemset and the support of each rule from this itemset share the same support count: support_count(itemset) == support_count(X Union Y); and of course the denominator (total count of itemsets happened) is the same  
 	- why confidence is different? the nominator is the same but the denominator of confidence is different. the denominator is the support count of itemset X, and X is different for each rule. 

Therefore, do the task in 2 phases.

phase 1:  
	- find all frequent itemsets I (i.e. the support of itemsets I must be >= minsupport)  
	- remember that the support of rules originating from an itemset is the same as the support of the itemset
	- phase 1 is the conputationally expensive phase! (a bit anti-intuitive)

phase 2:  
	- for itemsets I, generate rules X->I Minus X (i.e. X->Y, Y= I Minus X, and X is a subset of Y)  
	- as mentioned before, the number of rules from a k-itemset = 2^k - 2 

Phase 1
-------------------

use apriori algorithm.

we know that if A is not frequent, AB (or any other AXXX) must be not frequent.  
Good, then we get the list of frequent 1-itemset first in the so called pass 1.  
Then in pass 2, we form 2-itemsets from thsi frequent 1-itemset list as the potential candidates.  
count the number of occurrence for these candidates and then get the true list of frequent 2-itemsets.  
this step will be the most memory-consuming coz there are too many 2-itemsets.  
and then form a candidate list of 3-itemsets from these true frequent 2-itemsets, and then count thier number in pass 3.  
and so on until there is no more candidates to form.

improvement for phase 1 ----> PCY alogrithm.  
in pass 1, get the list of frequent 1-itemset as usual,   
but for each basket, also hash all possible pairs (2 items) to a big hash table (as big as the memory allows).  
then compress the hash table to 1bit each slot hash table in pass 2.
each bit indicate whether pairs that have been hashed into this hash map are frequent or not. not care about the numbers.  
in pass 2, just check each potential 2-itemset to see if it meets the conditions:  
	a. two items in the 2-itemset are both frequent  
	b. the pair has been hashed to a frequent hash map  
if yes, count this pair. else, ignore.  
in this case, there will be much less pairs to be counted so the memory required in pass 2 will be less (if the frequent pairs are much less than pairs that have counts)
