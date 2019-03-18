Notes
---------------

An example that shows how to build a new docker image.

The base image is ubuntu 16.04.
What we want it is to install ping tool and create a new image.

To build the new image (in this directory): docker build -t ubuntu:16.04.ping .

To run the command: docker run --rm run ubuntu:16.04.ping ping google.com
