CNN
------------------------

One good tutorial: https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/

An example following https://www.tensorflow.org/tutorials/layers


Filters in CNN
---------------------------

For an input datapoint (e.g. an image), a filter will map it to the 2nd layer.

Just imagine that a filter is like a torch that move from one region of the image to another region of the image (moving windows);
for each region, there will be an output matrix.

E.g. the input image is 100 (height) x 200 (width) (just 1 color), the filter can be for a region of 10 x 20 on the image;
the filter can be 20 x 5 weights, and the output for the region will be 10 x 5.

Then there will be a 'pooling' such as an average function to map the 10x5 output matrix to 1 scalar. 
With paddling, the 2nd layer for this filter will still be 100x200.

If the image has 3 colors, the filter can be set to be high dimensional accordingly to cover all the elements in the region.
Ultimately the polling layer will bring down the dimension of the output from each filtering action.

No matter what, the number of unknows in the filter is fixed when the filter is chosen, which is not affected by the size of the image.
This is one big advantage of cnn, because the number of unknowns is much less than that for a vanilla fully connected neural network.

Usually there will be multiple filters in parallel.
Just imagine that there are multiple 2nd layers, and 3rd layers, etc.

At some point, we can use another filter with a bigger step in the moving windows to get a small-size layer.
So for each starting filter, there will be a small-size layer at some point (i.e. multiple small-size layers in the same bigger layer),
and then we can use the fully-connected network to link up all the parallel layers in this particular layer.

ultimately, it will be linked back to just 1 or a few output nodes to solve the problem.
