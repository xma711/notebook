Understand tar and gzip
----------------------------

Reference: http://www.crybit.com/difference-between-tar-and-gzip/

tar is just a technology to combine multiple files to one file archive.

Gzip is a compression technology to compress that file.

These 2 steps could be done separately or together (usually together).


Examples
-----------------

Make a tar ball: tar czf programs.tar.gz ./programs/* (note that this is slightly different from "tar czf programs.tar.gz ./programs/", which creates a tarball one less level)  
also, the -z refers to the gzip compression.

Extract a tar ball: tar xf programs.tar.gz

extract with top directory stripped: tar xf programs.tar.gz --strip-components=1 -C new_directory (sometimes have to be --strip-components=2)


bzip
---------------------------------

Bzip is another compression technology.

Example: tar -cjSf folder.tar.bz2 folder (the -j refers to using bzip)


