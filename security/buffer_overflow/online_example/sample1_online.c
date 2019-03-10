// from: https://turkeyland.net/projects/overflow/intro.php
// this is just to let us see what memeory it uses using pmap pid_value;
// and by comparing with another process's memory, 
// it shows that 2 processes can use the same addresses

#include <stdio.h>

int main() {
  char c;

  printf("I am a running instance, or process, of program 1.\n");
  printf("My PID is %d\n", getpid());
  printf("Press enter to exit...\n");
  c = getchar();

  return 0;
}
