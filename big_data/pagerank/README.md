Google's method
--------------------

Use weblinks. if webpage A has a link to B, it is recommending B.

Using weblinks, we can form a graph for the whole network, e.g. A->B, B->C, A->C, C->A..

Let's initialize all webpages' rank to be 1/N, where N is the total number of pages.

Then we recalculate the page rank for each page in multiple iterations.

If A has links to both B and C, then A will pass half of its page rank to B and C.  
Each page's rank equals to the sum of all page ranks (based on last iteration's results) that are passed to them,
until the page rank for each webpage no more changes.

However, this way may lead to dead end (someone has no outgoing links) or spider trap (someone points to itself only), 
which will either cause the page ranks to leak from the network in each iteration, 
or to trap all the pagerank.

To solve this, we let each page able to teleport some pagerank to all other pages in the whole network.  
Ultimately, if A has links to B and C, it is no longer 0.5*pagerank to B or C, but 0.5*beta*pagerank to B or C, 
and the rest ( (1-beta)*pagerank ) to all other pages (including itself).

In this way, no one is a dead end or a trap.

Finally, the formula for each webpage is pagerank_this_round = beta * sum of incoming pageranks + (1-beta) * 1/N .
Note that implicitly this formula already assumes the sum of all page ranks = 1.

In fact, using this way, the pagerank is equivalent to a probability that this page will be chosen in the long run.

This is exactly the same as the Markov chain in the module advanced computer networks.  
In the module, each state is the number of people in a queue (0, 1, 2, .. ), 
in this case, each state is a webpage.  
The same problem is to find the probability of a state in the long run, given the state transition conditions.

There are some conditions only under which the steady state of the probabilities will converge (check computer network module).  
Using the teleport mechanism allows the network to satisfy these conditions.

Ultimately, we can solve it at one go, without having to do multiple iterations, if the network size is not too big.
Pagerank_this_round = beta * sum of incoming pageranks + (1-beta) * 1/N , and pagerank_this_round = pagerank_last_round (refer to lecture notes)

for an example, check gradiance/g3/pagerank.py


authority and hubs
--------------------

Another method is that  
each page has two scores, authority (like pagerank) and hubs (experts).

Authority = sum of hubs (those that have links to this page; no need to divide the hub score by the number of links the hub has).  
Hub = sum of authority (those that this page links to; no need to divide the authority score by the number of links)

then normalize authority and hubs, such that auth = auth / sqrt (sum of auth*auth), hub = hum / sqrt(sum of hub*hub).

Repeat this until they converge.

This is quite easy to use matrix. 
Auth_this_round = AT * A * auth_last_round; 
hub_this_round = A * AT * hub_last_round,  
where AT is the nxn matrix that indicate when page i has a link to page j (cell ij will be 1 if there is, and 0 otherwise),  
A is the transport of AT.  
Then normalize auth_this_round and hub_this_round before going to compute the next round results.

Refer to lecture notes if confused.
