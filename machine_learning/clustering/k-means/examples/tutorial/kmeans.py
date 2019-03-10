# reference: http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans

from sklearn.cluster import KMeans
import numpy as np

x = np.array( [ [1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0] ] )
print ("training data:")
print (x)
print ("x.shape = " + str(x.shape))

kmeans = KMeans(n_clusters=2, random_state=0)
print (kmeans)

kmeans.fit(x)

print ("labels = " + str(kmeans.labels_))
print ("cluster centers:")
print (kmeans.cluster_centers_)

x2 = np.array( [ [0, 0], [4, 4] ] )
print ("predict data:")
print (x2)

results = kmeans.predict(x2)
print ("results:")
print (results)
