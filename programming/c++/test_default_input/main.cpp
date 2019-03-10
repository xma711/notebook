#include "hello_world.h"

// test a default argument in the function header 
// in this case, one of hello_world's arguments to constructor has a default value


int main(){
	hello_world hw (1); // the parameter 2 will gives a default value as -1
	// hello_world hw(1, 2); // this is to specify both arguments
	hw.get_para1();
	hw.get_para2();
	return 0;
}
