
# this program cannot be killed by ctrl-c... which may not be a good thing
# this because except catches too much exceptions, including SIGINT (which is ctrl-c)
# in fact, all signals except SIGKILL can be handled by the program

import time

def to_sleep():	
	try:
		while True:
			print "sleep 100"
			time.sleep(100)
	except Exception:
		print "some normal exception occurred"
	except: 
		# this will make this program hard to kill -- which may not be desirable
		# e.g. if a gunicorn worker is hard to kill, gunicorn master will not be able to terminate the worker after it time out
		print "system exception occurred"

while True:
	to_sleep()
