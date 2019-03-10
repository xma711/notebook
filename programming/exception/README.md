if a certain block of codes may lead to some errors, a programmer could have a few choices:  
	1. let the errors occur and crash the programs  
	2. handle the errors so that the program can go on

1 is simple. and sometimes 1 can be used if there is a systemd to restart the program.

2 can be achieved by try...except...  
'try' the codes, if there are some errors, the errors won't crash the program.
the errors will be passed to the 'except' part. 
the except part can choose to handle the errors in whatever ways it sees fit.
if the except decides to ignore the errors, the program will go on as normal.  
one easy way is for except part to log the errors and then go on..
