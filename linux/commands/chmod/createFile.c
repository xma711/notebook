// try using setuid (chmod 4755 a.out) to check the permisson of the resultant files

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
	char buf[52];
	FILE *badfile;

	memset(buf, 1, sizeof(buf));
	badfile = fopen("./outputfile.bk", "w");

	fwrite(buf, sizeof(buf), 1, badfile);
	fclose(badfile);
}
