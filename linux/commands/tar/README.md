understand tar and gzip
----------------------------

reference: http://www.crybit.com/difference-between-tar-and-gzip/

tar is just a technology to combine multiple files to one file archive.

gzip is a compression technology to compress that file.

these 2 steps could be done separately or together (usually together).


examples
-----------------

make a tar ball: tar czf programs.tar.gz ./programs/* (note that this is slightly different from "tar czf programs.tar.gz ./programs/", which creates a tarball one less level)  
also, the -z refers to the gzip compression.

extract a tar ball: tar xf programs.tar.gz

extract with top directory stripped: tar xf programs.tar.gz --strip-components=1 -C new_directory (sometimes have to be --strip-components=2)


bzip
---------------------------------

bzip is another compression technology.

example: tar -cjSf folder.tar.bz2 folder (the -j refers to using bzip)


