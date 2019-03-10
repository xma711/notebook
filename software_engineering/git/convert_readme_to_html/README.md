convert README.md to html
------------------------------

reference: http://stackoverflow.com/questions/7694887/is-there-a-command-line-utility-for-rendering-github-flavored-markdown

using this python tool 'grip'.  
install: sudo pip install grip.

and go to the folder with the README.md, run grip.  
it will print out the localhost:PORT_NUMBER ..  
then in another terminal, simply do a "wget localhost:PORT_NUMBER"

disadvantage of this method: have to do it in 2 steps, and cannot be easily automated..


another way is "grip --export" which will simply export a README.html file locally, but it has too many extra things that i don't want.

