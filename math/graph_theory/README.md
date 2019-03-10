Graph Theory
-------------------------

reference: https://en.wikipedia.org/wiki/Graph_theory

graph theory is the study of graphs.  
graphs are mathematical structures used to model pairwise relations between objects.

a graph is made up of vertices, which are connected by edges.

a graph may be undirected, meaning there is no distinction between the 2 vertices associated with each edge;  
or its edges may be directed from one vertex to another.


a graph is an ordered pair G=(V,E) comprising a set V of vertices
with a set E of edges, which are 2-element subsets of V.
this type of graph may be described precisely as undirected and simple.

the order of a graph is |V|, its number of vertices.  
the size of a graph is |E|, its number of edges.

the degree of a vertex is the number of edges that connect to it,
where an edge that connects a vertex to itself (a loop) is counted twice.


types of graphs
-------------------------------

reference: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph

by default, the term 'graph' refers to 'undirected simple finite graph'.

Undirected graph:  
an undirected graph is a graph in which edges have no orientation.
the maximum number of edges in an undirected graph without a loop is n(n-1)/2,
where n is the number of nodes in the graph.

Directed graph:  
a directed graph or digraph is a graph in which edges have orientations.

there are other types of graphs, such as mixed graph, oriented graph, etc.


classes of graphs
-------------------------------------

regular graph: a graph in which each vertex has the same number of neighbors (i.e. same degree).
a regular graph with vertices of degree k is called a k-regular graph.

complete graph: a graph in which each pair of vertices is joined by an edge.
a complete graph contains all possible edges.

finit graph: a graph in which the vertex set and the edge set are finite sets.
otherwise it is called an infinite graph.

connected graph: an undirected graph in which every unordered pair of vertices in the graph is connected.  
when we say a pair of vertices {x,y} is 'connected', it means there is a path leads from x to y.  
if the requirement for 'connected graph' is not fulfilled, the graph is called disconnected graph.  
a stronlgy connected graph is a directed graph in which every ordered pair of vertices in the graph is strongly connected (a path between x and y formed by directed edges exists).

bipartite graph: a graph in which the vertex set can be partitioned into 2 sets, W and X,
so that no 2 vertices in W share a common edge and 
no 2 vertices in X share a common edge.  
(reference for bipartite graph: https://en.wikipedia.org/wiki/Bipartite_graph)  
visually, it means the vertices in W have edges with vertices in X, but vertices in W have no edges among themselves.  
one example is neural network's layer 1 and layer 2 form a bipartite graph because layer 1 have edges to layer 2
but layer 1 have no edges inside and layer 2 have no edges inside.

 
