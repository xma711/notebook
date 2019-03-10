#include <stdio.h>
#include <stdlib.h>

float f1 = 0.01234567890123456789;
float f2 = 123456789.01234567890123456789;
double d1 = 0.01234567890123456789;
double d2 = 123456789.01234567890123456789;

int main(){
	printf ("float1\t0.01234567890123456789\n");
	printf("%s\t%f\n", "%f", f1);
	printf("%s\t%.10f\n", "%10f", f1);
	printf("%s\t%.20f\n", "%20f", f1);
	printf("\n");

	printf ("float2\t123456789.01234567890123456789\n");
	printf("%s\t%f\n", "%f", f2);
	printf("%s\t%.10f\n", "%10f", f2);
	printf("%s\t%.20f\n", "%20f", f2);
	printf("\n");

	printf ("double1\t0.01234567890123456789\n");
	printf("%s\t%f\n", "%f", d1);
	printf("%s\t%.10f\n", "%10f", d1);
	printf("%s\t%.20f\n", "%20f", d1);
	printf("\n");

	printf ("double2\t123456789.01234567890123456789\n");
	printf("%s\t%f\n", "%f", d2);
	printf("%s\t%.10f\n", "%10f", d2);
	printf("%s\t%.20f\n", "%20f", d2);
	printf("\n");

	printf("it seems that float has 8 significant numbers while double has 17 signifiant numbers\n");

	return 0;
}
