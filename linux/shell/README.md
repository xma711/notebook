Shell
-------------

A shell is the generic name for any program that gives you a text-interface to interact with the computer.  
You type a command and the output is shown on screen.

Multiple shells are availabe in linux system: bash, csh, ksh, sh, tcsh, zsh et.  
They differ in the various options they give the user to manipulate the commands and  
in the complexity and capabilities of the scripting language.

Shell script
------------------

Many shells have scripting abilities: put mulitple commands in a script and the shell executes them as if  
they were typed from the keyboard.  
Most shells offer additional programming constructs that extend the scripting feature into a programming language.


Different modes of a shell
------------------------
Interactive: means that the commands are run with user-interaction from keyboard.

Non-interactive: the shell is probably run from an automated process so i can't assume if it can request input  
or that someone will see the output.

Login: means that the shell is run as part of the login of the user to the system.  
Typically used to do any configuration that a user needs/wants to establish his work-environment. 


Non-login: any other shell run by the user after logging on,  
or which is run by any automated process which is not coupled to a logged in user.

Reference: http://unix.stackexchange.com/questions/50665/what-is-the-difference-between-interactive-shells-login-shells-non-login-shell


more on different modes of a shell
-------------------------------------

Login shell: a login shell is the first process that executes under your user id when you log in for an interactive session.

Interactive login shell: when you log in on a text console, or through ssh or with su -, you get an interactive login shell.

Login when computer first boots up: when you log in in a graphical mode, you don't get a login shell, instead you get a session manager or a window manager.

Non-login interaceive shell: when you start a shell in a terminal in an existing session (screen, a shell inside another ..), you get an interactive, non-login shell.

Reference: http://unix.stackexchange.com/questions/38175/difference-between-login-shell-and-non-login-shell

.bashrc and .bash_profile and .profile
--------------------------------------------

.bashrc is only read by a shell that's both interactive and non-login so you'll find most people end up telling their .bash_profile to also read .bashrc with something like:  
[[ -r ~/.bashrc ]] && . ~/.basrc

.bash_profile is the personal initialization file for bash (a particular variant of shell), executed for login shells.

.profile is executed by login sh shell. but bash is backwards-compatible with sh, so it will also read .profile if one exists.

Reference: http://stackoverflow.com/questions/415403/whats-the-difference-between-bashrc-bash-profile-and-environment
