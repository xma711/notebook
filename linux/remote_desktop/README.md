server side
------------------

reference: https://www.linode.com/docs/applications/remote-desktop/using-vnc-to-operate-a-desktop-on-ubuntu-12-04  
http://askubuntu.com/questions/304017/how-to-set-up-remote-desktop-sharing-through-ssh

just run command: "vino-preferences"

configure the remote server setting. it is quite straigtforward.

if i want to do this to a remote server,
then "ssh -Y username@serverip " first, then
in the same terminal run the vino-preferences commmand.


client side
-----------------
run "remmina".

create a new profile, with protocol "VNC-Virtual Network Computing"!!! (important!!)  
then enter server ip address.  
and that's it!  
just click "connect" will do
