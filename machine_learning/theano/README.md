Difference between theano and tensorflow
-------------------------------------------

They have different ordering of dimensions.
Tensorflow has channels at the end while theano has it in 2nd position for image data.

Theano: [batch, channels, width, height]  
tensorflow: [batch, width, height, channels]

After 1.0 release at the end of 2017, major development would cease.

Google's tensorflow and Microsoft cognitive toolkit 2 largely superseded theano.

