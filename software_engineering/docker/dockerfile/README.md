notes
---------------

an example that shows how to build a new docker image.

the base image is ubuntu 16.04.
what we want it is to install ping tool and create a new image.

to build the new image (in this directory): docker build -t ubuntu:16.04.ping .

to run the command: docker run --rm run ubuntu:16.04.ping ping google.com
