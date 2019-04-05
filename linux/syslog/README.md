Using shell
------------------
Simply use the "logger" command:  
	logger "message"

In /var/log/syslog, we can see the message. e.g.  
	sudo tail -f /var/log/syslog  
	sudo grep "xma" /var/log/syslog

