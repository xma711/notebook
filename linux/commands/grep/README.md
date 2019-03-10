grep "^string" file_name
	- meaning it will find will lines start with 'string'


To search a string in files with a certain extension only (in this example it is .py)
grep -r -i --include \*.py 'hello' .  
another example: grep -r --include \*.py "sys.path.insert" .
