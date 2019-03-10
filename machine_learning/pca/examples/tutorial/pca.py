# reference: http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

import numpy as np
from sklearn.decomposition import PCA

def pca_and_results(x_):
	print ("\ndata is:")
	print (x_)
	pca = PCA(n_components=2)
	print (pca)
	pca.fit(x_)

	#print( "singular values = " + str(pca.singular_values_) )

	print( "mean = " + str(pca.mean_) )

	print( "variance ratio = " + str(pca.explained_variance_ratio_) )
	print ("components:")
	print (pca.components_) # this is sorted by explained_variance_

x1 = np.array( [ [-1,-1], [-2, -1], [-3,-2], [1, 1], [2, 1], [3, 2] ] )
pca_and_results(x1)

x2 = np.array( [ [4, 1], [5, 6], [2, 3], [1, 1], [2, 1], [3, 2] ] )
pca_and_results(x2)

# let's check if the pca algo takes cares of the mean alreday
print ("")
mean2 = np.mean(x2, axis=0) # compute column mean
print ( "mean of x2 = " + str(mean2) )
x2_minus_mean = x2 - mean2
print ("x2-mean =\n" + str(x2_minus_mean))
pca_and_results(x2_minus_mean)
# the results show that we don't have to take care of the mean by ourselves, which is a good news!!
