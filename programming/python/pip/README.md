Notes
-------------

If bbb doesn't have pip, it can be installed by 
	pacman -S python-pip

if there is any problem, just remove python-pip (pacman -Rns python-pip)
and upgrade the system: pacman -Syu (read the readme for archlinux for more details and possible issues about upgrading the system)


pip vs apt-get
--------------------

Reference: http://askubuntu.com/questions/431780/apt-get-install-vs-pip-install

apt-get installs packages from ubuntu repository. 
Usually the programs are installed to /usr/bin

pip install packages from PyPI, a repo managed by python software foundation.
It has more packages and the same package with different versions.
Usually packages installed by pip are stored to /usr/local/bin.

Due to the $PATH value in which /usr/local/bin is usally in front of /usr/bin,
the packages installed by apt-get will not be chosen if a same package is installed both by apt-get and pip.

In fact, when using pip, it is not a good idea to use "sudo pip install" because the packages may not be as secured as packages in apt-get.

A better way is to use virtualenv to create an env and use pip to install the packages without danger of hurting the system.
