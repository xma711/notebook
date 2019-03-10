#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// the implementation of the callback function
// note that a callback function is just a normal function -- nothing special
void callback( char* str) {
	printf("in callback 1\n");
	printf("%s\n\n", str);
};

// another callback function implementation
void callback2( char* str) {
	printf("in callback 2\n"); 
	printf("The length of '%s' = %lu\n\n", str, strlen(str));
};

// the caller function that has to be used with a callback function.
// to indicate a callback function in the argument, the argument has to be very precise.
// there have to be the return type (void in this case), the input arguments to the callback function: char *str. 
// also note that there has to be a * in front of the generic function name.
// this is quite different from nodejs, inwhich only a callback function is indicated in the argument without having to indicate the return type and the arguments
int caller_function(void (*func)(char *str), char* string) {
	func(string); // use the callback function on string input
};

int main (){
	caller_function(callback, "hello world!");
	caller_function(callback2, "hello world!");
	return 0;
}
