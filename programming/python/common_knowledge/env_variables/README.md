General
-----------------------

The most direct way is to set environment variables in .bashrc.  
E.g.  
Export ENV_VAR="XXXXXX"

note that this way, all programs are able to read the env variable, not just python.

Alternatively, we can use the dotenv package to load the env variables from a file.
For example:
```
from dotenv import load_dotenv

load_dotenv('./.env')
```

the 2nd way may be better because it is localized to the program only.  
To install dotenv, use 'pip install python-dotenv'
