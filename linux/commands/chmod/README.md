chmod
----------------

besides the usual read write execute permission,
chmod can be used to do this "setuid", 
which means once this "setuid" bit is set, 
when other users run this binary,  
the program (or the system) will set the uid to the owner id first before running the binary.
ultimately, the behaviour is like that the original user is running this binary.

chmod's 1st digit selects the "setuid" when it is 4,
and if the owner is root, then when the program is run, set-root-uid will be activated.  
one example: sudo chmod 4755 retlib

another example is "ping". 
ping command actually needs root access. 
ping is owned by root user.
so when normal user runs ping, the program has to be set root uid first before running.
therefore, when creating this ping program, the root user has to do a chmod 4755 ping.


when applying to a direcotry...
------------------------------

reference: http://unix.stackexchange.com/questions/21251/how-do-directory-permissions-in-linux-work

the execute bit (x) allows the affected user to enter the directory, and access files and directories inside. (NOT about listing!!!)

e.g.  
```
xma@path:~/github/knowledge/linux/commands/chmod$ ls -l
d--x------ 2 xma  xma  4096 Oct 10 10:37 test
xma@path:~/github/knowledge/linux/commands/chmod$ cd test ## this works fine
xma@path:~/github/knowledge/linux/commands/chmod/test$ ls ## this is not working
ls: cannot open directory .: Permission denied

```

the write bit allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes.

e.g.  
```
xma@path:~/github/knowledge/linux/commands/chmod$ ls -l
d--x------ 2 xma  xma  4096 Oct 10 10:56 test

xma@path:~/github/knowledge/linux/commands/chmod$ cd test/
xma@path:~/github/knowledge/linux/commands/chmod/test$ touch hello
touch: cannot touch ‘hello’: Permission denied
xma@path:~/github/knowledge/linux/commands/chmod/test$ cd ..
xma@path:~/github/knowledge/linux/commands/chmod$ chmod +w test
xma@path:~/github/knowledge/linux/commands/chmod$ cd test/
xma@path:~/github/knowledge/linux/commands/chmod/test$ touch hello
```

```
xma@path:~/github/knowledge/linux/commands/chmod$ ls -l
d-w--w---- 2 xma  xma  4096 Oct 10 10:58 test
xma@path:~/github/knowledge/linux/commands/chmod$ echo newfile > test/newfile ## looks like write needs an access too, so it is denied
bash: test/newfile: Permission denied
xma@path:~/github/knowledge/linux/commands/chmod$ touch test/newfile
touch: cannot touch ‘test/newfile’: Permission denied
```

the read bit allows the affected user to list the files within the directory.  
note that this is a totally different thing from the execute bit.  
if i know there is a file and its name in a folder and its name and then i can still execute on it!

e.g.  
```
xma@path:~/github/knowledge/linux/commands/chmod$ ls -l
dr--r--r-- 2 xma  xma  4096 Oct 10 10:58 test
xma@path:~/github/knowledge/linux/commands/chmod$ cd test/ ## cannot enter
bash: cd: test/: Permission denied
xma@path:~/github/knowledge/linux/commands/chmod$ ls test/ ## but can list
ls: cannot access test/hello: Permission denied   ## cannot access because there is no execute set
hello
```

another thing is about subdirectory in a directory without read permission.  
the subdirectory reserves the read permission if it originally has.  
anyway, each directory is a like a file and it has its own permissions.  
changing one directory's permission (don't use -R) doesn't change ther permissions in the subdirectories.

```
xma@path:~/github/knowledge/linux/commands/chmod$ ls -l
d-wx------ 2 xma  xma  4096 Oct 10 11:10 test
xma@path:~/github/knowledge/linux/commands/chmod$ cd test
xma@path:~/github/knowledge/linux/commands/chmod/test$ ls
ls: cannot open directory .: Permission denied
xma@path:~/github/knowledge/linux/commands/chmod/test$ mkdir test2
xma@path:~/github/knowledge/linux/commands/chmod/test$ cd test2
xma@path:~/github/knowledge/linux/commands/chmod/test/test2$ ls ## read in subdirectory is okay!
```

if a directory has w permission only, we cannot list the things in the directory.
but we can still enter the subdirectory if we know the subdirectory's name.  
e.g.  
```
xma@path:~/github/knowledge/linux/commands/chmod$ ls -l
d--x------ 3 xma  xma  4096 Oct 10 11:10 test
xma@path:~/github/knowledge/linux/commands/chmod$ cd test
xma@path:~/github/knowledge/linux/commands/chmod/test$ ls
ls: cannot open directory .: Permission denied
xma@path:~/github/knowledge/linux/commands/chmod/test$ cd test2
xma@path:~/github/knowledge/linux/commands/chmod/test/test2$
```
