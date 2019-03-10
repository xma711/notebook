git
-------------------

a source-code versioning software, similar to subversion.

unlike svn, git is a distributed versioning software, meaning everyone can have different commits at their local repo.

with git, one is commiting changes to the local repo.

but if the local repo has linked to a remote repo such as github, then one can push the changes to the remote repo.

what is doing i believe is alway merging. 

when one pull a brancn from a remote repo to a local branch, there is a merge.

when one push a local branch to a remote branch, there is a merge. 

e.g. git pull origin master , which is to pull the master branch from the 'origin' repo to the local master branch.

e.g. git push origin master, which is to push the master branch from the local repo to the master branch at the remote repo.  
this line actually means git push origin master:master.
technically we can do "git push origin dev:master" too.

when git push origin branchxxx, and if branchxxx does not exit in origin, then origin repo will create a branch with the same name.

'origin' is just a tag of the remote repo from the local perspective, which is default for local repo that clones from a remote repo.

one can create many tags of whatever remote repo they want to consider in the same local repo.

e.g. 'git remote add upstream git@github.com:xxxx.git' is to add an 'upstream' tag for certain upstream repo.

one can update the upstream branches and merge a branch from upstream to a local branch.

e.g. git fetch upstream; git checkout localbranch; git merge upstream/whatever_branch 

git rebase: similar to git merge, but it creates a new commit for every single commit in the feature branch (current branch) at the end of the upstream branch, so that the history is linear 
