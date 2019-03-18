Sort -t, --key=1,1 file
	- -t means field-separator, or delimiter. in this case the delimiter is ','
	- --key= is to indicate which field (column) to sort. in this case it is the first field

what does --key=1,4 mean? 
	- it means the sorting is to done on the basis of the first 4 fields. (what does this mean instead?)

Sort -k 2,2 -n file : sort 2nd column using numeric.. -n refers to using numeric

to randomize the lines in a file: sort --random-sort filename
