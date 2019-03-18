# tryGithub
For teaching how to use git and github


Advantages of using git and github
-----------------------------------

Git is a version-control software for source codes and text files  
and github is a web-based Git repository hosting service.

Git can be used locally without github. It allows one to keep track of a full history of a repository locally.

Github allows one to host the repository in their website and link it to your local repository.

There are many advantages of using git and github:

 - If you are doing a project alone, you can use git and github to log your progress neatly and you can jump to any past history when needed.

 - For a team project, you can collaborate each other using github easily.  The team can incrementally add changes to a remote github repo without stepping on each other' toes. 

 - It allows you to access the remote repo in any computer and you can clone the full history in any computer. 

 - It enhances accountability and reduces confusion in a collaboration. 

 - It provides a single interface for team mates to access each other's works, which increases work efficiency.


The recommended workflow for people contributing to master branch (much simpler compared to the front-end team)
-----------------------

(see details of the git commands in the later sections)

1. clone a remote repo to the local computer

2. make a new branch from the master branch in your local repo and working on it (*git checkout master && git branch new_branch && git checkout new_branch*)

3. (recommended) in any major folder you created, it is good to write a README.md to explain what it is about and how to use the materials you committed

4. carefully select the files to be added and commit the changes time after time (never commit binary files and static files like big documents or videos)

5. when you completed and tested the feature, merge the branch to the master branch. (if you are not sure, never merger your branch back to master.)

6. in master branch, do a git pull to see if everything is okay. resolve conflicts if needed (*git checkout master && git pull origin master*)

7. in master branch, do a git push to add the changes to the remote repo (*git checkout master && git push origin master*)

8. delete the your local branch

9. repeat steps 2 to 8 for future works


The recommended workflow for people working on his/her own branch
----------------------------------------------

(see details of the git commands in the later sections)

1. clone a remote repo to the local computer

2. make a new branch from the desired branch in your local repo

3. (recommended) in any major folder you created, it is good to write a README.md to explain what it is about and how to use the materials you committed

4. carefully select the files to be added and commit the changes time after time (never commit binary files and static files like big documents or videos)

5. do a git pull to see if everything is okay. resolve conflicts if needed (*git pull origin branch_name*)

6. do a git push to add the changes to the remote repo (*git push origin branch_name*)

7. repeat steps 3 to 6 for future works

set up necessary tools
------------------------

If you use ubuntu, then add git by  
*sudo apt-get install git*

if you use windows, then download git shell from https://windows.github.com/ and install it

this tutorial will purely make use of command line, which gives users more controls.

Note that all commands in this tutorial are done in a Git Shell or a Linux terminal. Some basic linux commands you may need to know include:

go to a directory   
*cd [path_to_a_folder/directory]*  
e.g. *cd ./github/tryGithub*

list the files and folders in a folder/directory:  
*ls* or *ls -lh*

make a directory/folder:  
mkdir [directory_name]

for more linux commands, you can refer to: http://www.thegeekstuff.com/2010/11/50-linux-commands

note that all the git commands are in *italic*.


Clone a remote repository
--------------------------

You can find the url of the remote repo from github.com. Then clone it by:  
*git clone remote_url*

e.g. to clone this repo, you can use:  
*git clone https://github.com/xma711/tryGithub.git*   
OR *git clone git@github.com:xma711/tryGithub.git* (if you added your ssh key of your computer to github)

After you clone the repository, you have a local copy of the remote repository. You can do anything to your local repo. As long as you don't push it to the remote repo, any local changes won't affect the remote repo.

Understand some basics
------------------------

Check url of the remote repository:   
*git remote -v*

Note that 'origin' is a label for this remote url.  

Check all branches in your local repo:  
*git branch*

you will see things like "master" and whatever branches you have created.

Branches are like parallel worlds in a repo. you can only go to one branch at a time. 

Branch names like "master" are labels of the local branches you have. some branches can exist in your local repo but not in remote repo.


Branch
-----------------------

When you are working on a repo, it is good to create your own branch and work on it first. only until you are sure your works are okay, then you merge the branch to the "master" branch.

Create a branch:  
*git branch [branch_name]*  
e.g. *git branch xma_branch*

go to a branch:  
*git checkout [branch_name]*   
e.g. *git checkout xma_branch*

The 'git checkout' command allows you to go to a 'parallel world' you choose.

To merge branch B to Branch A, go to branch A first, and do a 'git merge branch_B':  
*git checkout branch_A*  
*git merge branch_B*  
e.g. *git checkout master & git merge xma_branch*  

to delete a local branch, use:  
*git branch -d [branch_name]*

to delete a remote branch (use with care!):  
*git push origin :[branchName]*

commit
---------------------

After you edit files, add files or do other changes, you will save these changes to a particular branch. the tools you will use are "git add" and "git commit".

For example, if you create a new file named "hello_world.txt" with some texts inside or edit the file if "hello_world.txt" has been commited to the repo before, then you can add it to the current branch by:  
*git add hello_world.txt*

to check the current status of the repo, use:  
*git status*

to see what exactly have been changed, use:  
*git diff*

if you are okay with the changes and want to save it, then use:  
*git commit -m "add hello world file"*  
the "-m" allows you to add a logging message so that you know what you have done in the future.

Note that we normally don't commit any binary files or images or videos to github. these files are usually big and do not often subject to changes. adding them to the github repo will slow down the "git pull" (obtaining the latest changes) by everyone else and make the repo untidy. Therefore, please check your changes carefully before you do a "git commit".

One tip. if you edit an existing file that has been committed before, you can skip the "git add" by using "git commit -am", where "a" means 'all'.  
E.g. *git commit -am "edit hello world file"*

note that each commit is a snapshot of the repo at a particular time. you can check the past commits by:  
*git log*

you can go to a particular commit by:  
*git checkout [the_commit_hash_id]*

to come back to the master branch, you can do a:  
*git checkout master*

push to remote
------------------
When you are happy with the commits you have done, you can push the right branch to a branch of the remote repo (e.g. "master" branch). The command is:  
*git push origin [branch_name]*

e.g. if your changes are committed in the local master branch, you can push it by:  
*git push origin master*

usually, you will have to do a "git pull" before a git push. "git pull" allows you to obtain the latest changes in the remote repo. "git pull" can lead to conflicts sometimes, when two people edit on the same thing from the same commit. how to resolve conflicts will be talked about later.

If you have a local branch and you want the remote repo to keep a copy of it, then you can do a:  
*git push origin [the_new_branch]*  
e.g. *git push origin xma_branch*

but usually extra branches should be temporary and you should remove them when they have been merged to the master branch.
 
My personal habit is to create a new branch for a new feature i want to create. most of the time i will keep the branch to my local repo only. when i finished the feature, i will merger the branch to the master branch and delete the temporary branch. and i will repeat the cycle again for a new feature.

After you do a git push, you can check the latest changes in github.com too.

Resolve conflicts
--------------------

Conflicts can happen when you do a "git pull" or "git merge". when the changes coming from pull or merge affects something you have already edited in the destination branch, git will prompt you that there is a conflict. 

To resolve the conflicts, open the file affected and decide what to keep and what to remove. After you are happy with it, then you can do a new commit with the new changes.

README.md
------------------
It is always good to add a README.md in as many folders as possible.

People can view the details about this repo or this folder directly in github.

For example, what you are reading is the README for this repo.

Git cheat sheets
--------------------

For more git commands, you can refer to  
https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf  
or http://www.git-tower.com/blog/git-cheat-sheet/


some other points
-----------------------

To monitor github on your phone, you can install the github app from the apps market.
