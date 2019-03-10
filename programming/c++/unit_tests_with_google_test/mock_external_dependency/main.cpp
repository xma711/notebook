#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "count_num_char.h"
#include "helloworld.h"

int main() {
	HELLOWORLD hw;

	COUNT_NUM_CHAR cnc(&hw);

	int num = cnc.count_after_call_hello_world();

	printf("num after calling count_after_call_hello_world() = %d\n", num);

	return 0;
}
