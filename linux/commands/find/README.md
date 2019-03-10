- usage
find files with certain pattern in filenames

- example

	find ./ -name "hello*"
	# files with names lik "helloworld" "hello kitty" will be found.

to execute a command one each file found:  
	find ./testin -name "*.csv" -exec COMMAND_AND_OPTIONS '{}' \;  
	e.g. find ./testin -name "*.csv" -exec ls -lh '{}' \;
