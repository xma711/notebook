Chmod
----------------

Besides the usual read write execute permission,
chmod can be used to do this "setuid", 
which means once this "setuid" bit is set, 
when other users run this binary,  
the program (or the system) will set the uid to the owner id first before running the binary.
Ultimately, the behavior is like that the original user is running this binary.

Chmod's 1st digit selects the "setuid" when it is 4,
and if the owner is root, then when the program is run, set-root-uid will be activated.  
One example: sudo chmod 4755 retlib

another example is "ping". 
Ping command actually needs root access. 
Ping is owned by root user.
So when normal user runs ping, the program has to be set root uid first before running.
Therefore, when creating this ping program, the root user has to do a chmod 4755 ping.


When applying to a directory...
------------------------------

Reference: http://unix.stackexchange.com/questions/21251/how-do-directory-permissions-in-linux-work

the execute bit (x) allows the affected user to enter the directory, and access files and directories inside. (NOT about listing!!!)

E.g.  
```
$:~/github/notebook/linux/commands/chmod$ ls -l
d--x------ 2 xma  xma  4096 Oct 10 10:37 test
$:~/github/notebook/linux/commands/chmod$ cd test ## this works fine
$:~/github/notebook/linux/commands/chmod/test$ ls ## this is not working
ls: cannot open directory .: Permission denied

```

the write bit allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes.

E.g.  
```
$:~/github/notebook/linux/commands/chmod$ ls -l
d--x------ 2 xma  xma  4096 Oct 10 10:56 test

$:~/github/notebook/linux/commands/chmod$ cd test/
$:~/github/notebook/linux/commands/chmod/test$ touch hello
touch: cannot touch ‘hello’: Permission denied
$:~/github/notebook/linux/commands/chmod/test$ cd ..
Xma@path:~/github/notebook/linux/commands/chmod$ chmod +w test
$:~/github/notebook/linux/commands/chmod$ cd test/
$:~/github/notebook/linux/commands/chmod/test$ touch hello
```

```
$:~/github/notebook/linux/commands/chmod$ ls -l
d-w--w---- 2 xma  xma  4096 Oct 10 10:58 test
$:~/github/notebook/linux/commands/chmod$ echo newfile > test/newfile ## looks like write needs an access too, so it is denied
bash: test/newfile: Permission denied
$:~/github/notebook/linux/commands/chmod$ touch test/newfile
touch: cannot touch ‘test/newfile’: Permission denied
```

the read bit allows the affected user to list the files within the directory.  
Note that this is a totally different thing from the execute bit.  
If i know there is a file and its name in a folder and its name and then i can still execute on it!

E.g.  
```
$:~/github/notebook/linux/commands/chmod$ ls -l
dr--r--r-- 2 xma  xma  4096 Oct 10 10:58 test
$:~/github/notebook/linux/commands/chmod$ cd test/ ## cannot enter
bash: cd: test/: Permission denied
$:~/github/notebook/linux/commands/chmod$ ls test/ ## but can list
ls: cannot access test/hello: Permission denied   ## cannot access because there is no execute set
hello
```

another thing is about subdirectory in a directory without read permission.  
The subdirectory reserves the read permission if it originally has.  
Anyway, each directory is a like a file and it has its own permissions.  
Changing one directory's permission (don't use -R) doesn't change the permissions in the subdirectories.

```
$:~/github/notebook/linux/commands/chmod$ ls -l
d-wx------ 2 xma  xma  4096 Oct 10 11:10 test
$:~/github/notebook/linux/commands/chmod$ cd test
$:~/github/notebook/linux/commands/chmod/test$ ls
ls: cannot open directory .: Permission denied
$:~/github/notebook/linux/commands/chmod/test$ mkdir test2
$:~/github/notebook/linux/commands/chmod/test$ cd test2
$:~/github/notebook/linux/commands/chmod/test/test2$ ls ## read in subdirectory is okay!
```

if a directory has w permission only, we cannot list the things in the directory.
But we can still enter the subdirectory if we know the subdirectory's name.  
E.g.  
```
$:~/github/notebook/linux/commands/chmod$ ls -l
d--x------ 3 xma  xma  4096 Oct 10 11:10 test
$:~/github/notebook/linux/commands/chmod$ cd test
$:~/github/notebook/linux/commands/chmod/test$ ls
ls: cannot open directory .: Permission denied
$:~/github/notebook/linux/commands/chmod/test$ cd test2
$:~/github/notebook/linux/commands/chmod/test/test2$
```
