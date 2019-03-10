to sync google drive
---------------------------

it is better to use the command line tool "drive".

follow the guide here: https://github.com/odeke-em/drive

to install platform-specific binary, follow: https://github.com/odeke-em/drive/blob/master/platform_packages.md 


usage
-------------

create a folder, e.g. drive, and cd to the folder and do a 'drive init'.  
the instruction will tell me how to set the credentials in this folder to point to one particular google drive account.

subsequently in this folder, i can do 'drive pull -hidden folder_name' to pull exactly one particular folder.

to see the listing: drive list

to push a folder: drive push folder_name

to pull a folder: drive pull folder_name

to compared folder difference between local and remote: drive diff folder_name


after some time, the credential may fail.  
to reset it, (no need to delete any files or folders), do a 'drive deinit',  
and then do a 'drive init' again.


notes
-----------------------

for shared folder, you have to add the folder to your own drive before you can use 'drive pull folder_name'.  
(i cannot find a way to pull a shared folder directly.)

the folder will still be 'shared' mode.
i.e. whatever changes done in your drive will be reflected in the shared folder.

e.g. i create a subfolder in a shared folder,
then i right click this subfolder and add to my drive.

then in my local machine in the appropriate folder, i can do a 'drive pull -hidden subfolder'.  
note that the option -hidden allows me to pull the files and folders with names starting with '.'.

