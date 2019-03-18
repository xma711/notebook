Systemd is the software to auto start programs in some linux system, like archlinux.


- commands:

systemctl enable simple_example.service		# enable the service unit

systemctl start simple_example.servie		# start the unit

systemctl status simple_example.service		# check the status

time units
---------------

Time units: https://www.freedesktop.org/software/systemd/man/systemd.time.html#

usec, us

msec, ms

seconds, second, sec, s

minutes, minute, min, m

hours, hour, hr, h

days, day, d

weeks, week, w

months, month, M (defined as 30.44 days)

years, year, y (define as 365.25 days)


journalctl
--------------------

- read the print messages:

journalctl -fu simple_example.service		# 'f'ollow the 'u'nit to see the messages

# see the messages since a date indicated

journalctl --since="yy-mm-dd HH:MM:SS" -u simple_example.service	


to read a particular journal file, use   
journalctl --file=file_name -u unit_name


examples
--------------------

A standalone service file in service/

a target file with its component service file in target/

a timer file with its service file in timer/


timer
--------------------------

See http://www.freedesktop.org/software/systemd/man/systemd.time.html for more details

Note that the timer is not precise by default. it can happen within 1min!  
To set it more precise, use AccuracySec =  

see: https://www.freedesktop.org/software/systemd/man/systemd.timer.html

