Rigid transformation
--------------------

Note that for any registration, the "data" pi of the reference object refer to location coordinates; not the value of the whatever data at the location!  
Same for qi, the locations of corresponding points on the target object.

Given a set of corresponding points between target object (the broken skull, qi) and reference object (a skull model, pi),
try to find a transformation function T to transform reference object to the target object without changing the shape of the reference object, 
and T will minimize || qi - T(pi) ||.

The size of reference object can be changed; it can be rotated or translated, but the shape cannot be changed.

The model is qi = sRpi + T.

It looks like linear fitting but we cannot apply it here because it will change the shape of the reference object.  
To solve it, just follow the lecture notes.. 


(Rigid) ICP - Iterative Closest Point
-------------------------------------

Same as the problem for rigid transformation, except that we don't know the corresponding points qi on the target object..  
In this case, the thing to solve is to minimize || f(pi) - T(pi) ||, 
where f is a function to estimate the corresponding points on target object based on pi.  
One educated choice is to find the closest points on target object.  

The algorithm is an alternative optimization.

Step 1: set pi' = pi;  
step 2: run until converged:  
	2.1 get corresponding points qi = f(pi');  
	2.2 based on qi and pi, run normal rigid transformation; we will get s R T for this round;  
	2.3 ok get pi' = sRpi + T;  
outputs: s, R, T, pi'

(seems quite straightforward..)


Affine transformation: a non-rigid transformation 
---------------------------------------------------

In fact, this is easier than the rigid transformation.  
Same problem, except this time we are free to change the shape of the reference object.  
The easiest method is probably the Affine transformation.

It is similar to the model in rigid transformation qi = sRpi + T  
but this time we can use linear fitting.  
Let qi = ui = (u v w).T, and pi = (x1, x2, x3).T, 
from the equation we can have  
u = sR11 x1 + sR12 x2 + sR13 x3 + T1, or
u = a11 x1 + a12 x2 + a13 x3 + a14 , which is clearly a linear function.  
Same for v and w.  
In fact, we can solve u v and w at one go:  
U = D A.T, where each row of U is one data point of qi (target), 
each row od D is one data point of pi (reference), 
and each column of A.T is the coefficients for each dimension (e.g. first column is the coefficients for u).  
The answer: A.T = (D.T D)^(-1) D.T U.

This should be approximation when there are quite some points.

Nonrigid ICP (Iterative Closest Point)
------------------------------------------

It is better to read the original paper if this technique is ever needed..

This method is to locally apply Affine transformation..

Pi: position of mesh vertex i on reference surface. 
I think, to understand this, just imagine there is a 2d plane on the x-y space, and each pi is a point on the plane, like (1, 1), (1,2), (2,2), etc.

What we are going to do is to get 3 error functions and somehow arrange them in a linear way so that it can be solved by linear fitting..

Q1: is nonrigid ICP approximation or interpolation?  -ans: approximation.

Q2: are landmark points known? is the corresponding landmark point for each pi known?  
	- ans: some landmarks are known, which are used in the El term.

From lecture notes, "As for ICP, find the closest point ui on target surface to pi". 
So this ui is not known beforehand? we estimate it using a function f()?

The first error function is Ed = SUM{wi || Ai pi - ui ||^2}, why do we need the wi?  
The lecture notes explain that "wi = 1 for vertices with correspondence; 0 otherwise".  
However, if ui is estimated, then we should be able to get a ui for each pi isn't it? then why do we need wi?

In the normal Affine transformation, we have A.T has unknowns, but we have many pairs of known (pi, ui) to estimate A.T.  
However, in this case, for each Affine transformation, we have only 3 equations for each data point,
exactly because the one Affine transformation applies on one single pair of points..  
One affine transformation introduces 12 unknowns for a 3d point (u,v,w), i.e. the number of elements in A.T.  
Clearly there are not enough equations to solve them.
We need extra information.

2nd piece of information, we know a list of corresponding points L = {(pi, qi)}.
The qi here are not estimated; they are exact.  
The 2nd error function: El = SUM{ || Ai pi - qi ||^2 }

q3: is this pi same as the pi in Ed? should be another set right?  
	- same set, just that some of them have corresponding landmarks.

A 3rd error function is Es = SUM{|| (Ai - Aj) G||^2 @F }, 
meaning the affine transformation of connected neighbours should not differ too much.  
This means that (i,j) is something we already know. in fact we can know because we have pi.  
@F means the Frobenius norm, which says the sum of each element^2 in a matrix.

Finally, we have the overall error function E = Ed + alpha Es + beta El

for the first error Ed, arrange it in a more compact way.  
Let D = diag(pi.T), so it is a nx4n matrix. it is 4 because i need to add a 1 to each pi. 
A = [A1 .. An].T, as Ai is 3x4 matrix, so A is (3x4n).T = 4nx3 matrix.  
U = [u1 .. un].T, as ui is 3x1, U is nx3 matrix.  
W = diag(w1, .., wn) so it is a nxn matrix
then Ed can be rearranged as Ed = || W(DA - U) ||^2 @F.  
Inside it is a nx3 matrix.

For the 2nd error El, similarly we have El = ||Dl A - Q||^2 @F, 
where Dl = diag(p1.T .. pn.T) where pi contains only the pi that have exact correspondences (i guess other rows are just 0), a nx4n matrix;  
A should be the same, 4nx3 matrix,  
Q = [q1 .. qn].T (contains only corresponding qi) is a nx3 matrix..   
Inside El it is a nx3 matrix.

To represent Es in a more compact way is more complicated.  
We need to have an incidence matrix M, in which each column is mesh vertex and each row is a mesh edge that connects two vertices, 
such that M[r, i] = 1, M[r, j] = -1 if r connects vertices i and j, i>j.  
Q4: what does this mean exactly?   
	- each column is an vertex index; each row corresponds to an edge. e.g. if edge with id 1 connects node 2 and node 3, then first row will have a 1 in column 3 and -1 in column 2, and 0 for other columns. 

Anyway we will have Es = || (M Kx G) A ||^2 @F, where kx means Kronecker product.  
When a mxn matrix Kx A pxq matrix, the resultant matrix will be a (mxp)x(nxq) matrix.  
Anyway M is a nxn matrix ?, G is a 4x4 matrix ?, so M kx G is a 4n x 4n matrix ?. (need further thinking) 
so in Es it is a 4n x 3 matrix ?

Ultimately we can arrange E = Ed + alpha Es + beta El together in a compact way:  
E = || [ (WD) (alpha M Kx G) (beta Dl) ].T * A - [ (WU), (0), (Q) ].T ||^2 @F.  
Note that the [].T here is not to transpose everything. just make the 3 items in the bracket stacking vertically.  
It can be written as E =|| BA - C ||^2 @F.  
Therefore, the answer for A = (B.T B)^(-1) B.T C


TPS (Thin plate spline)
-------------------

Thin plate spline leads to an algo of a global affine transform + some terms to take care of the nonlinear parts.  
This algo minimizes the bending energy of the resultant "metal sheet". 

For each pi on reference, we have a known vi in the target.

Anyway, let x be a point on reference, each mapped point of x on target = affine transform of x + SUM{ wi * U(||x - pi||) }, 
where pi are points on the reference.  
There are n unknown w and 12 unknown parameters for affine transform (assume a point is 3d, each component has 4 unknowns), 
there will be exactly n + 12 equations at the end.  
Why? aren't there only n equations? that's why. we still need 12 more equations.  
One more constraint is sum of wi is 0 and sum of wi*pi is 0. 
This creates 12 more equations.  
At the end, we can solve wi and affine transform exactly and the resultant plate passes thru landmarks points exactly.


Laplacian deformation
-------------------------------

For each pi on reference, we know some of the corresponding landmarks on target, which are called di.
For the other pi, we don't know the corresponding points.

Laplacian aims to make sure the known landmarks on target will be passed thru exactly (condition 1),
while keeping the surface normal of each point as close to the original as possible (condition 2).

With condition 1, we have Cx = d. 
X is all the corresponding points on target we want to find. 
Each point is vertical (3x1), so x is a 3nx1 slim column matrix.  
D are the known landmarks, expressed in the same long column way.  
C is a big matrix, but each row has at most one 1, and the rest 0. 
For example, if p1 = d1, it will be broken down to p1x=d1x; p1y=d1y; p1z=d1z.
Then first row of C is just [1 0 0 0 0 0...] meaning x1 = d1 which means p1x = d1x.  
Of course all the points with corresponding landmarks have to come on top in x.

A point's surface normal can be approximated by L(pi) = pi - 1/Ni SUM(neighbors of pi).  
For each of pi on reference, we know the exact answers because each pi is known, and each pi's neighbors are known.  
For each of the corresponding on target (x), we don't know the exact answer but we know how to calculate them.  
So if q1 is q2's neighbor (qi are resulant points on target), then the surface normal of q1 can be estimated as q1 - 1/N1 * SUM{ q2 + others if any }.
This can be expressed in one equation using the long column matrix x.  
Anyway ultimately we will have Ax - b, where b is the surface normals for all pi; 
while each row of A represent an equation to express one qi's surface normal.

Then we have the problem statement:  
min_x ||Ax - b|| s.t. Cx = d.  

This is a constraint least square problem.

One familiar way to solve this is the lagrange multiplier method, but it only gives approximated answer.

Another way is QR factorization, which gives exact answer.
Here i won't go to details. just refer to notes.
