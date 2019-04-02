#!/usr/bin/python2

# reference: http://stackoverflow.com/questions/1057431/loading-all-modules-in-a-folder-in-python/20753073#20753073

## an example showing how to import python files from another directory at another location

# firstly, need to add path to the module to the system path.
# note that sys.path is nothing but a python standard list object; 
# therefore we can modify it using standard method
import sys
sys.path.insert(0, "./another_location")

# then import the module
# which is actually a folder with a __init__.py file
from hellocat import *
#import hellocat  ## if import in this way, need to import again: import hellocat.spam

#import subcat/cat3 # not working this way

# spam.py is one file in the hellokitty/ directory
spam.spamfunc()

# cannot do something like this: hellocat.spam.spamfunc()

# ham.py is another file in hellokitty/ directory
ham.hamfunc()

# another python script that calls another python script in another folder
callSubcatCat3.func()
