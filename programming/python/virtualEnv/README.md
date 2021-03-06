1. in host machine. default as python 2.7. install virtualenvwrapper: sudo pip install virtualenvwrapper  

1.1. source /usr/local/bin/virtualenvwrapper.sh (or /usr/bin/virtualenvwrapper.sh depending on where it is installed. just use find.) 

2. make a virtual env with default python as 3.4: mkvirtualenv    --python=/usr/bin/python3.4   envName  

3. now default python in the env is 3.4. now can install requirements.  

4. to return the env, use *workon envName*. to exit, use deactivate (20150520)  

to create a virtual env with packages stored at somewhere else, use something like:    
virtualenv --python=python3.4 PATH_TO_THE_FOLDER  
where PATH_TO_THE_FOLDER is the path to all the new packages.


My understanding:  
virtualEnv still uses the host machine (kernel + filesystem),   
but it is able to use alternative packages like python 3.4 without affecting the host machine.  
New packages installed in the virtual env is also applicable to that particular environment only.  
It is not computing resource isolation but isolation of 'environment'.   
Therefore it is like a partial virtual machine.

Difference to docker:  
 docker uses a fully isolated filesystem, totally independent to host machine.   
Inside the docker container, users cannot touch the host machine 
because host machine is outside its 'universe'.   
In fact, the users inside the container are totally not in the same world of the host machine.  

On the other hand, even inside the virtualEnv, users can do whatever to the host machine,  
although the tools used can have different versions from the same tools in the host machine.  
Even inside the virtual env, the user is still the same as that in the host machine.

In short, virtualEnv allows users to use a different set of tools to do things in the same machine (same kernel + same filesystem).


Export requirements from the virtualEnv
--------------------------------------------

To export: pip freeze > requirements.txt

To install: pip install -r requirements.txt
