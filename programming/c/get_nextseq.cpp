#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

static uint16_t getNextSeqnum()
{
    static uint16_t seqnum = -1;
    return ++seqnum;
};


int main() {
	int i;
	for (i=0; i< 65550; i++) {
		printf ("%d: next seq number = %u\n", i,  getNextSeqnum());
	}
	return 0;
}
