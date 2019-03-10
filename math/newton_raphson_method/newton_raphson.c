#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double get_y (const double n) {
	return 2.0*pow(10,-4) + 16.0 *n*n/(10.0 * pow(10,9)) + n*n*n *( -3.0/ (800.0 * pow(10,9)));	
};

double get_dy_dn (const double n) {
	return 32*n/(10.0 * pow(10,9)) +n*n*(-9.0/(800*pow(10,9)));
};


int main (){

	int i = 0;
	double n=1.1;
	//double y;
	while (i<40) {
		n = n - get_y(n)/get_dy_dn(n); // newton-raphson method
		printf ("%f\n", n);	
		i++;
	}

	return 0;
}
