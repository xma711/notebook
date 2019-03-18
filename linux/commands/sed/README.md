Sed
------------------

Sed (stream editor) is a Unix utility that parses and transforms text, using a simple, compact programming language. sed was developed from 1973 to 1974 by Lee E. McMahon of Bell Labs, and is available today for most operating systems.

Reference: en.wikipedia.org/wiki/Sed

- usage

    sed -i "s/original/new/g" file.txt
(use "" instead of '' when there are parameters passed in in a shell script)

Explanation:

    sed = Stream EDitor
    -i = in-place (i.e. save back to the original file)

    The command string:
        s = the substitute command
        original = a regular expression describing the word to replace (or just the word itself)
        new = the text to replace it with
        g = global (i.e. replace all and not just the first occurrence)

    file.txt = the file name

reference: askubuntu.com/questions/20414/find-and-replace-text-within-a-file-using-commands


to change a parameter:

sed -i.bak "s/^\(generic.node-id \).*/\1${node_id}/" file


rename
-------------------
Rename is similar, but it is used for renaming files:

rename 's/ACDC/AC-DC/' files  
where 'AC-DC' will replace any 'ACDC' in the file names
