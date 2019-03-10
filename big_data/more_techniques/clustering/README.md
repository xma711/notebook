hierarchical agglomerate cluster
--------------------------------

handle 2d points.

initially, treat each point as a cluster.

find the two clusters that have shortest distance (need to define what shortest distance means in each case).
merge these two clusters.

repeat the process until there is only 1 cluster or at a number that is acceptable by a user.


k-means
-------------------------
handle 2d points. 

randomly generate k points, and use them as centroid.

assign points that are nearest to the centroid as a cluster.

recomputer centroids again based on the new clusters.

re-assign points to the new centroids.

repeat the process until centroids do not change any more.



betweenness hierarchical clustering
------------------------------

handle a graph, like a network of nodes.

computer which link has the biggest betweenness (that has the most shortest paths that pass thru this link).  
break the graph to 2 by breaking the  link.

repeat process until there are k clusters


clique clustering
--------------------------------

clique of size k is a graph in which there are k nodes, and each node has a link to all other nodes.

to get a clique of size >= k, sample a subgraph and remove nodes that has less than k-1 links, repeatedly.

the remaining graph is the clique with size >= k.

to get the maximum clique in a graph, lecture notes says it is a NP-hard problem.


other clustering methods
------------------
refer to lecture notes.
