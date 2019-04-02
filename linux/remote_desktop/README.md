Server side
------------------

Reference: https://www.linode.com/docs/applications/remote-desktop/using-vnc-to-operate-a-desktop-on-ubuntu-12-04  
http://askubuntu.com/questions/304017/how-to-set-up-remote-desktop-sharing-through-ssh

just run command: "vino-preferences"

configure the remote server setting. it is quite straightforward.

If i want to do this to a remote server,
then "ssh -Y username@serverip " first, then
in the same terminal run the vino-preferences command.


Client side
-----------------
Run "remmina".

Create a new profile, with protocol "VNC-Virtual Network Computing"!!! (important!!)  
Then enter server ip address.  
And that's it!  
Just click "connect" will do
