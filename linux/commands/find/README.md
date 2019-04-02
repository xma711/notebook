- usage
find files with certain pattern in filenames

- example

	find ./ -name "hello*"
	# files with names like "helloworld" "hello kitty" will be found.

To execute a command one each file found:  
	find ./testing -name "*.csv" -exec COMMAND_AND_OPTIONS '{}' \;  
	e.g. find ./testing -name "*.csv" -exec ls -lh '{}' \;
