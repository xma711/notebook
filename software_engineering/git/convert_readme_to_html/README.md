Convert README.md to html
------------------------------

Reference: http://stackoverflow.com/questions/7694887/is-there-a-command-line-utility-for-rendering-github-flavored-markdown

using this python tool 'grip'.  
Install: sudo pip install grip.

And go to the folder with the README.md, run grip.  
It will print out the localhost:PORT_NUMBER ..  
Then in another terminal, simply do a "wget localhost:PORT_NUMBER"

disadvantage of this method: have to do it in 2 steps, and cannot be easily automated..


Another way is "grip --export" which will simply export a README.html file locally, but it has too many extra things that i don't want.

