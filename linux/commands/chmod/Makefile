## the result from this is that the badfile generated is root:xma;
## setuid set the owner's uid, but group id is still determined by whoever (xma) runs this
run:  
	sudo gcc createFile.c
	sudo chmod 4755 a.out
	./a.out
clean:
	rm a.out ./outputfile.bk

## the result from nosetuid is that the badfile generated is xma:xma;
## both the user id and group id of files genreated are determined by who runs the program, not who owns the program
nosetuid:
	sudo gcc createFile.c
	./a.out
