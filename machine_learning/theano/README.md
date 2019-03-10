difference between theano and tensorflow
-------------------------------------------

they have different ordering of dimensiions.
tensorflow has channels at the end while theano has it in 2nd position for image data.

theano: [batch, channels, width, height]  
tensorflow: [batch, width, height, channels]

after 1.0 release at the end of 2017, major development would cease..

google's tensorflow and microsoft cognitive toolkit 2 largely superseded theano...


notes
----------------------------

btw the autoencoder i implemented during my masters is implemented using theano..
