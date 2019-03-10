how to use
-------------------

create a conda environment named test: conda create -n test

the folder for this particular env can be found in ~/anaconda2/envs/test  
(this means conda is very similar to virtualenv. the later creates a folder somewhere else)


to create an env with python3: conda create -n py3conda python=3.5

to see a list of conda env: conda info --envs ,  
and the currently active env is the one with an asterisk (*)

to activate a conda env: source activate test  
(the env name with a bracket will appear)

example to activate a conda env not in the default path (e.g. in anaconda's folder):
	source activate /home/xma/anaconda3/envs/py3updatePandas

note that by default, when i use 'conda', i am already inside the default env, which is the base 'anaconda' folder!!!!
therefore conda is always in an environment.
so be careful when using conda to install anything.

to deactivate a conda env: source deactivate

to install a package, firstly make sure you are in the right env, and then install it.
e.g.
```
source activate test
conda info --envs  # double check
conda install numpy
```

similarly, to uninstall a package from a conda env (make sure you are in the correct env): 
	conda uninstall package_name

to list the packages installed in this conda env: conda list

to export the list of packages from current env: conda list --export > package_list.txt

to install packages from an export file: conda install --file package_list.txt

sometimes if a package cannot be found, try to add channel: conda config --append channels conda-forge 
(reference: https://stackoverflow.com/questions/48493505/packagesnotfounderror-the-following-packages-are-not-available-from-current-cha)


install packages using pip in a conda env
-------------------------------------------------

activate the conda env,  
use "whereis pip" to locate the pip for this conda env.

then use the full path of pip to install a package and it will be part of this conda env.


environment variable in conda
-----------------------------------

to add environment variables such that only a particular conda environment knows, need to add a script in the activate.d/ path in the env.
(reference: https://stackoverflow.com/questions/46826497/conda-set-ld-library-path-for-env-only)  

(however, the above approach seems to affect the conda env such that 'source deactivate' no longer works.)

note that in the conda env, you can also see the environment variables set in .bashrc.  
therefore to set env variables for all conda env, then set it is .bashrc, using:  
export ENV_VAR="XXXXXX"

alternatively, we can use the dotenv package to load the env variables from a file.
for example:
```
from dotenv import load_dotenv

load_dotenv('./.env')
```
