ROC curve
------------------------

ROC curve is the plot of true positive rate vs false positive rate (the key word here is 'rate').

true positive rate means the corrected classified positive cases divided by all postive cases in the training data.

let's say N is the test data size.  
and let's assume it is a binary classifier (trained using training data).

after applying the classifier on the test data, we will have the following numbers:  
- True positives (TP): the number of positives classified correctly (ground truth is positive)  
- False positives (FP): the number of cases classified as postives but in fact they are negative  
- True negatives (TN): the number of negatives classified correctly (ground truth is negative).  
- False negatives (FN): the number of cases classified as negatives but in fact they are positive.

Note that TP + FP + TN + FN = N.

true positive rate is therefore = TP / (TP + FN) = TP / ALL_Positives

we can affect the classifer results by changing the threshold (by default it is 50%).
assume that when threshold increases, it is harder for classifier to classify a case as positive.

then when we increase this threshold, we expect the true positive rate to decrease (correct?).

if we set the threshold to 100%, TP = 0 and therefore true positive rate = 0.  
if we set the threshold to 0%, TP = ALL_positives.
	False Negative is 0 because no positive case will be classified as negative.
	so true positive rate = 100% in this case.

then why don't we set the threshold to 0%? i.e. no matter what, classify all cases to positive.

if we do this, the false positive number will be very high.  
therefore, we also have to look at this false postive rate.  
false positive rate = FP / (FP + TN) = FP / ALL_negatives

when threshold is 0%, the false positive rate will be 100%, which is usually bad.  
when threshold is 100%, false positive rate is 0%, because there is no postive classified.  

in short, when threshold is 0%, true positive rate is 100% (good) and false positive rate is 100% (bad).
when threshold is 100%, true positive rate is 0% (bad) and false positive rate is 0% (good).  
clearly, there is a tradeoff between true postive rate and false positive rate.

therefore, when varying threshold, we need to look at both true positive rate and false positive rate.

let's say we increase the threshold from 0% to 20%.
the true positive rate will decrease as some positive cases will be classified as negative.
at the same time, false positive rate will decrease, because less negative cases will be classified as positive.

what about false negative rate?  
false negative rate should equal to FN / ALL_Positives.  

does false negative rate has anything to do with false positive rate?

when threshold increases from 0% to 20%, false negative number will increase from 0 to some number.
when threshold is 100%, false negative rate will be 100% (all positives are classified as negative).

let's do a summary again.
when threshold = 0%, both true and false positive rate is 100%, while false negative rate is 0% (good).
when threshold = 100%, both true and false positive rate is 0%, while false negative rate is 100% (bad).

therefore, when we reduce threshold to increase true positive rate, 
we also cause a higher false positive rate (bad) but a lower false negative rate (good).

anyway, a low threshold is good for 2 rates (true positive and false negative)
but bad for the others (false positive and true negative)
