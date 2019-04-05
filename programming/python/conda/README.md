How to use
-------------------

Create a conda environment named test: conda create -n test

The folder for this particular env can be found in ~/anaconda2/envs/test  
(this means conda is very similar to virtualenv. the later creates a folder somewhere else)


To create an env with python3: conda create -n py3conda python=3.5

To see a list of conda env: conda info --envs ,  
and the currently active env is the one with an asterisk (*)

To activate a conda env: source activate test  
(the env name with a bracket will appear)

Example to activate a conda env not in the default path (e.g. in anaconda's folder):  
	source activate ${HOME}/anaconda3/envs/py3updatePandas

Note that by default, when we use 'conda', we are already inside the default env, which is the base 'anaconda' folder!
Therefore conda is always in an environment.
So be careful when using conda to install anything.

To deactivate a conda env: source deactivate

To install a package, firstly make sure you are in the right env, and then install it.
E.g.

```
source activate test
conda info --envs  # double check
conda install numpy
```

Similarly, to uninstall a package from a conda env (make sure you are in the correct env): 
	conda uninstall package_name

To list the packages installed in this conda env: conda list

To export the list of packages from current env: conda list --export > package_list.txt

To install packages from an export file: conda install --file package_list.txt

Sometimes if a package cannot be found, try to add channel: conda config --append channels conda-forge 
(reference: https://stackoverflow.com/questions/48493505/packagesnotfounderror-the-following-packages-are-not-available-from-current-cha)


Install packages using pip in a conda env
-------------------------------------------------

Activate the conda env,  
use "whereis pip" to locate the pip for this conda env.

Then use the full path of pip to install a package and it will be part of this conda env.


Environment variable in conda
-----------------------------------

To add environment variables such that only a particular conda environment knows, need to add a script in the activate.d/ path in the env.
(reference: https://stackoverflow.com/questions/46826497/conda-set-ld-library-path-for-env-only)  

(However, the above approach seems to affect the conda env such that 'source deactivate' no longer works.)

Note that in the conda env, you can also see the environment variables set in .bashrc.  
Therefore to set env variables for all conda env, then set it is .bashrc, using:  
export ENV_VAR="XXXXXX"

Alternatively, we can use the dotenv package to load the env variables from a file.
For example:

```
from dotenv import load_dotenv
load_dotenv('./.env')
```
