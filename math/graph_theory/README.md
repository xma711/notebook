Graph Theory
-------------------------

Reference: https://en.wikipedia.org/wiki/Graph_theory

graph theory is the study of graphs.  
Graphs are mathematical structures used to model pairwise relations between objects.

A graph is made up of vertices, which are connected by edges.

A graph may be undirected, meaning there is no distinction between the 2 vertices associated with each edge;  
or its edges may be directed from one vertex to another.


A graph is an ordered pair G=(V,E) comprising a set V of vertices
with a set E of edges, which are 2-element subsets of V.
This type of graph may be described precisely as undirected and simple.

The order of a graph is |V|, its number of vertices.  
The size of a graph is |E|, its number of edges.

The degree of a vertex is the number of edges that connect to it,
where an edge that connects a vertex to itself (a loop) is counted twice.


Types of graphs
-------------------------------

Reference: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph

by default, the term 'graph' refers to 'undirected simple finite graph'.

Undirected graph:  
an undirected graph is a graph in which edges have no orientation.
The maximum number of edges in an undirected graph without a loop is n(n-1)/2,
where n is the number of nodes in the graph.

Directed graph:  
a directed graph or digraph is a graph in which edges have orientations.

There are other types of graphs, such as mixed graph, oriented graph, etc.


Classes of graphs
-------------------------------------

Regular graph: a graph in which each vertex has the same number of neighbors (i.e. same degree).
A regular graph with vertices of degree k is called a k-regular graph.

Complete graph: a graph in which each pair of vertices is joined by an edge.
A complete graph contains all possible edges.

Finite graph: a graph in which the vertex set and the edge set are finite sets.
Otherwise it is called an infinite graph.

Connected graph: an undirected graph in which every unordered pair of vertices in the graph is connected.  
When we say a pair of vertices {x,y} is 'connected', it means there is a path leads from x to y.  
If the requirement for 'connected graph' is not fulfilled, the graph is called disconnected graph.  
A strongly connected graph is a directed graph in which every ordered pair of vertices in the graph is strongly connected (a path between x and y formed by directed edges exists).

Bipartite graph: a graph in which the vertex set can be partitioned into 2 sets, W and X,
so that no 2 vertices in W share a common edge and 
no 2 vertices in X share a common edge.  
(reference for bipartite graph: https://en.wikipedia.org/wiki/Bipartite_graph)  
visually, it means the vertices in W have edges with vertices in X, but vertices in W have no edges among themselves.  
One example is neural network's layer 1 and layer 2 form a bipartite graph because layer 1 have edges to layer 2
but layer 1 have no edges inside and layer 2 have no edges inside.

 
