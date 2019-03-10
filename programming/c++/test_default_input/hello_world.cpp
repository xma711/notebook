#include "hello_world.h"
#include <stdio.h>
#include <stdlib.h>

int p1=0;
int p2=0;

hello_world::hello_world(int para1, int para2) {
	p1= para1;
	p2 = para2;
};

void hello_world::get_para1(){
	printf ("para1 = %d\n", p1);
};

void hello_world::get_para2(){ 
        printf ("para2 = %d\n", p2);
};
