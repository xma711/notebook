Install the latest version
---------------------------------

Install from github directly: https://github.com/docker/compose/releases/

then choose the latest tag, e.g. 1.15.0.

Then go to Downloads to download the docker-compose-Linux-x86_64. 

Move it to /usr/local/bin/docker-compose and "chmod +x" it.

Or simply use one command line (do a "sudo -i" to change to root):  
curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
