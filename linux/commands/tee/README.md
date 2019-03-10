reference: http://stackoverflow.com/questions/764463/unix-confusing-use-of-the-tee-command

tee is used to split a command pipeline, allowing you to save the output of a command to a file and send it along down the pipeline. In the first example you gave::

echo "foo bar" | sudo tee -a /path/to/some/file

./print_hello.sh  | tee tmpfile

in short, tee allows the program print_hello.sh or command echo to output messages to standout but also pipe them to a file.
