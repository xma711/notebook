General
-----------------------

the most direct way is to set environment variables in .bashrc.  
e.g.  
export ENV_VAR="XXXXXX"

note that this way, all programs are able to read the env variable, not just python.

alternatively, we can use the dotenv package to load the env variables from a file.
for example:
```
from dotenv import load_dotenv

load_dotenv('./.env')
```

the 2nd way may be better because it is localized to the program only.  
to install dotenv, use 'pip install python-dotenv'
