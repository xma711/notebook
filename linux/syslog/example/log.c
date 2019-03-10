#include <syslog.h>

int main() {

setlogmask (LOG_UPTO (LOG_DEBUG));

openlog ("exampleprog", LOG_PERROR | LOG_CONS | LOG_PID | LOG_NDELAY, LOG_LOCAL1);

syslog (LOG_NOTICE, "Program started by User %d", getuid ());
syslog (LOG_INFO, "A tree falls in a forest");

closelog ();

return 1;

}
