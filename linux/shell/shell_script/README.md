Shell script
-------------------------

Refer to the example for how to write a function, how to check if a file or directory is there, etc


arithmetic in shell script
-----------------------------

A=`expr "$a" + "$num"` or a=`expr $a + $num`

where  
a is the variable, 
expr is a command line Unix utility which evaluates an expression and outputs the corresponding value,
`command arguments` is similar to $(command arguments), which allows a command to be executed inside,
and $a and $num are the numbers to be added 

note that there must be a space between $a and +, as well as + and $num. 

The operations available:
	- for integers: addition, subtraction, multiplication, division and modulus
	- for strings: find regular expression, find a set of characters in a string; in some versions: find substring, length of string
	- for either: comparison (equal, not equal, less than, etc.)

Backticks `` notation is older than $() so backticks are more portable in unix machine.  
But $() is easier to read.

Reference: https://en.wikipedia.org/wiki/Expr

other ways of doing arithmetic (less portable):
	- a=$(($a+$num))
	- ((a=a+num))
	- let a=a+num
	- ((a+=num))
