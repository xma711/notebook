To sync google drive
---------------------------

It is better to use the command line tool "drive".

Follow the guide here: https://github.com/odeke-em/drive

to install platform-specific binary, follow: https://github.com/odeke-em/drive/blob/master/platform_packages.md 


usage
-------------

Create a folder, e.g. drive, and cd to the folder and do a 'drive init'.  
The instruction will tell me how to set the credentials in this folder to point to one particular google drive account.

Subsequently in this folder, we can do 'drive pull -hidden folder_name' to pull exactly one particular folder.

To see the listing: drive list

to push a folder: drive push folder_name

to pull a folder: drive pull folder_name

to compared folder difference between local and remote: drive diff folder_name


after some time, the credential may fail.  
To reset it, (no need to delete any files or folders), do a 'drive deinit',  
and then do a 'drive init' again.


Notes
-----------------------

For shared folder, you have to add the folder to your own drive before you can use 'drive pull folder_name'.  
(Not sure if there is a way to pull a shared folder directly.)

The folder will still be 'shared' mode.
I.e. whatever changes done in your drive will be reflected in the shared folder.

E.g. create a subfolder in a shared folder first,
then right click this subfolder and choose to add to `my drive'.

Then in the local machine in the appropriate folder, we can do a 'drive pull -hidden subfolder'.  
Note that the option -hidden allows me to pull the files and folders with names starting with '.'.

