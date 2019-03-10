# git tutorial
For teaching how to use git and git server


Advantages of using git and git server
-----------------------------------

Git is a version-control software for source codes and text files,  
and a git server (e.g. Gitlab or Github) is a web-based Git repository hosting service.

Git can be used locally without a git server. It allows one to keep track of a full history of a repository locally.

A git server allows one to host the repository in their website and link it to your local repository.

There are many advantages of using git and a git server:

 - If you are doing a project alone, you can use git and a git server to log your progress neatly and you can jump to any past history when needed.

 - For a team project, you can collaborate each other using a git server easily.  The team can incrementally add changes to a remote a git server repo without stepping on each other' toes. 

 - It allows you to access the remote repo in any computer and you can clone the full history in any computer. 

 - It enhances accountability and reduces confusion in a collaboration. 

 - It provides a single interface for team mates to access each other's works, which increases work efficiency.

 - Good for trial and error in your own branch without affecting anyone else.

 - Good for organizing development work ('dirty' state) and well-tested work (master branch).

 - A git server usually comes with extra features like wiki, issue tracker.

 - A git server has a lot of extensibilities. E.g. You can link your remote repo in a git server with extra tools to do CI (continuous integration) and CD (continuous development).

Set up necessary tools
------------------------

If you use ubuntu, then add git by  
*sudo apt-get install git*

If you use windows, then download git shell from https://windows.github.com/ and install it

This tutorial will purely make use of command line, which gives users more controls.

Note that all commands in this tutorial are done in a Git Shell or a Linux terminal. Some basic linux commands you may need to know include:

Go to a directory   
*cd [path_to_a_folder/directory]*  

List the files and folders in a folder/directory:  
*ls* or *ls -lh*

Make a directory/folder:  
mkdir [directory_name]

For more linux commands, you can refer to: http://www.thegeekstuff.com/2010/11/50-linux-commands

Note that all the git commands are in *italic*.


Understand some basics
------------------------

Check url of the remote repository:   
*git remote -v*

Note that 'origin' is a label for this remote url.  

Check all local branches in your local repo:  
*git branch*

You will see things like "master" and whatever branches you have created.

To view both local branches and remote branches, use:  
"git branch -a"  
Note that the remote branch looks something like "remotes/origin/master". 

Branches are like parallel worlds in a repo. You can only go to one branch at a time. 
This means there won't be multiple copies of the project folders in your computer. 
There is always one folder, but it represents one particular branch at any time.

Branch names like "master" are labels of the local branches you have. Some branches can exist in your local repo but not in remote repo.


Clone a remote repository
--------------------------

You can find the url of the remote repo from the git server. Then clone it by:  
*git clone remote_url*

e.g. to clone a repo, you use:  
*git clone https://github.com/.....git*   
OR *git clone git@github.com:.....git* (if you added your ssh key of your computer to github)

After you clone the repository, you have a local copy of the remote repository. You can do anything to your local repo. As long as you don't push it to the remote repo, any local changes won't affect the remote repo.


branch
-----------------------

When you are working on a repo, it is good to create your own branch and work on it first. 
Only until you are sure your works are okay, then you do a merge request to merge your branch to the "master" branch.

Create a branch:  
*git branch [branch_name]*  
e.g. *git branch xma_branch*

Go to a branch (i.e. checkout a branch):  
*git checkout [branch_name]*   
e.g. *git checkout xma_branch*

The 'git checkout' command allows you to go to a 'parallel world' you choose.  
In fact, if you want to do anything to a branch, always checkout the branch first.

To merge branch B to Branch A, go to branch A first, and do a 'git merge branch_B':  
*git checkout branch_A*  
*git merge branch_B*  
e.g. *git checkout xma_branch & git merge master* (merge master branch to xma_branch)  

To delete a local branch, use:  
*git branch -d [branch_name]*

To delete a remote branch (use with care!):  
*git push origin :[branchName]*


commit
---------------------

After you edit files, add files or do other changes, you will save these changes to a local branch. The tools you will use are "git add" and "git commit".

For example, if you create a new file named "hello_world.txt" with some texts inside or edit the file if "hello_world.txt" has been commited to the repo before, then you can add it to the current branch by:  
*git add hello_world.txt*

To check the current status of the repo, use:  
*git status*

To see what exactly have been changed, use:  
*git diff*

If you are okay with the changes and want to save it, then use:  
*git commit -m "add hello world file"*  
the "-m" allows you to add a logging message so that you know what this commit is about in the future.

Note that we normally don't commit any binary files or images or videos to a git server. These files are usually big and do not often subject to changes. Adding them to the a git server repo will slow down the "git pull" (obtaining the latest changes) by everyone else and make the repo untidy. Therefore, please check your changes carefully before you do a "git commit".

One tip: if you edit an existing file that has been committed before, you can skip the "git add" by using "git commit -am", where "a" means 'all'.  
e.g. *git commit -am "edit hello world file"*

Note that each commit is a snapshot of the repo at a particular time. you can check the past commits by:  
*git log*

You can go to a particular commit by:  
*git checkout [the_commit_hash_id]*

To come back to the master branch, you can do a:  
*git checkout master*


push to remote
------------------
When you are happy with the commits you have done, you can push your branch to the remote repo (or push the commits if the branch already exists in the remote repo). The command is:  
*git push origin [branch_name]*

E.g. if your changes are committed in the local "feature_branch", you can push it by:  
*git checkout feature_branch; git push origin feature_branch*

Usually, you will have to do a "git pull origin master" before a git push. "git pull" allows you to obtain the latest changes in the remote repo. "git pull" can lead to conflicts sometimes, when two people edit on the same thing from the same commit. how to resolve conflicts will be talked about later.

Usually feature branches should be temporary and you should remove them when they have been merged to the master branch.
 
My personal habit is to create a new branch for a new feature i want to create. Most of the time i will keep the branch to my local repo only. When i finished the feature, i will merge the branch to the an intermediate branch under my name and delete the temporary branch. And i will repeat the cycle again for a new feature.

After you do a git push, you can check the latest changes in git server too.


Resolve conflicts
--------------------

Conflicts can happen when you do a "git pull" or "git merge". When the changes coming from pull or merge affects something you have already edited in the destination branch, git will prompt you that there is a conflict. 

To resolve the conflicts, open the file affected and decide what to keep and what to remove. After you are happy with it, then you can do a new commit with the new changes.


.gitignore
----------------------

To ignore some files (which you never want to commit), add the filename to the .gitignore files.  
Then when you do a "git status", they won't appear as untracked files.


README.md
------------------
It is always good to add a README.md in as many folders as possible.

People can view the details about this repo or this folder directly in the git server in a browser.


The recommended workflow
-----------------------

1. Clone a remote repo to the local computer

2. Make a new branch from the master branch in your local repo and working on it (*git checkout master && git branch feature_branch && git checkout feature_branch*)

3. (Recommended) In any major folder you created, it is good to write a README.md to explain what it is about and how to use the materials you committed

4. Carefully select the files to be added and commit the changes time after time (never commit binary files and static files like big documents or videos) (git add files_list; git commit -am "comment on this commit" )

5. When you completed and tested the feature, update your master branch and merge the master branch to your feature branch. (in case there is any change to the master branch during your development) (git checkout master; git pull origin master; git checkout feature_branch; git merge master.  
Or equivalently, git fetch origin; git checkout feature_branch; git merge origin/master;)

6. Push your feature branch to the remote repo (*git push origin feature_branch*)

7. When you are confident to contribute your feature to the master branch, go to the git server through browser and do a merge request to merge your branch to the master branch

8. After merging to master, delete the new_branch.

9. Repeat steps 2 to 8 for new features


git cheat sheets
--------------------

For more git commands, you can refer to  
https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf  
or http://www.git-tower.com/blog/git-cheat-sheet/

