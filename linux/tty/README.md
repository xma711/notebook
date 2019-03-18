Explanation
-----------------

Reference: http://superuser.com/questions/449781/why-is-there-so-many-linux-dev-tty

The ttys are not just input/output devices. They also do a special job of acting as the controlling terminal for a session, like sending signals (Ctrl+C). 
/dev/ttyNN are virtual consoles, which are full screen displays on the monitor. 

The terminals start from /dev/tty1. You could switch to these consoles, usually, by pressing Ctrl+Alt+Fn keys.

E.g, Ctrl+Alt+F1 takes you to the first virtual terminal. 
Nowadays, most of the Linux distributions run the X server from the tty1. 
So, pressing Ctrl+Alt+F1 may not have an effect.

Ctrl+Alt+F2 will take you to the second terminal. Usually the distributions run a login program(agetty) on the virtual terminal.

The login programs provide you a login prompt and lets you login with username/password. 
The init scripts decides, where all the login program will be run. 
So depending on that you may or may not see a login prompt on, say tty9. To go back to your GUI interface, press Ctrl+Alt+F1(as in example output above).

/dev/tty0 is a special device, which points to the current terminal. 
So, irrespective of where you run it from(any virtual console), anything read from/written to tty0 goes to your current terminal.

The second column in 'ps ax' also gives the controlling terminal of the program. 
For some programs, like daemons, you may see that the column is '?', which means they are not bound to a terminal.

/dev/pts/0 etc are psuedo-terminal devices, which are not attached to the system display. 
For e.g, terminal you get when you open a gnome-terminal or any other GUI terminal. 
These are client-server based approach where client side will be exported to programs, like bash. 
The data send by the program to the pseudo terminal is sent to the 'server' side (which is usually monitored by another program, like gnome-terminal). 
The controlling process (server side) determines what needs to be sent to the terminal, which is eventually seen by the client. 
These devices help you to open multiple 'GUI terminals' without any limit on your system, 
still providing the same old terminal like controls(ioctl(), colour setting, Sending signals [Ctrl+C] etc. ).

Find out the tty name
---------------------------

Go to a terminal, use command "tty" to find out the terminal name.

Can echo "message" > tty_name to send the message to the terminal.
