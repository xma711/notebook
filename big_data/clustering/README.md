Hierarchical agglomerate cluster
--------------------------------

Handle 2d points.

Initially, treat each point as a cluster.

Find the two clusters that have shortest distance (need to define what shortest distance means in each case).
Merge these two clusters.

Repeat the process until there is only 1 cluster or at a number that is acceptable by a user.


K-means
-------------------------
Handle 2d points. 

Randomly generate k points, and use them as centroid.

Assign points that are nearest to the centroid as a cluster.

Recompute centroids again based on the new clusters.

Re-assign points to the new centroids.

Repeat the process until centroids do not change any more.



Betweenness hierarchical clustering
------------------------------

Handle a graph, like a network of nodes.

Computer which link has the biggest betweenness (that has the most shortest paths that pass thru this link).  
Break the graph to 2 by breaking the  link.

Repeat process until there are k clusters


clique clustering
--------------------------------

Clique of size k is a graph in which there are k nodes, and each node has a link to all other nodes.

To get a clique of size >= k, sample a subgraph and remove nodes that has less than k-1 links, repeatedly.

The remaining graph is the clique with size >= k.

To get the maximum clique in a graph, lecture notes says it is a NP-hard problem.


Other clustering methods
------------------
Refer to lecture notes.
