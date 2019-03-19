#!/usr/bin/python2

# reference: http://mosquitto.org/documentation/python/
# install: sudo pip install paho-mqtt

# this is a publisher that publish a message to the server: localhost

import paho.mqtt.client as paho
import time
import sys

server="localhost"
message = "hello world"
topic = "hello"

print "Going to publish a message '%s' to Server %s under topic '%s'" % (message, server, topic)

# create the client
client = paho.Client()

# for checking if the broker ever responds to connect_async()
status = -1 

# define a callback function to print a msg when the client connects to the broker

# The value of rc determines success or not:
# 0: Connection successful
# 1: Connection refused - incorrect protocol version
# 2: Connection refused - invalid client identifier
# 3: Connection refused - server unavailable
# 4: Connection refused - bad username or password
# 5: Connection refused - not authorised
def on_connect(client, userdata, flags, rc):
	print("Connection returned " + str(rc))
	if rc != 0:
		print ("Fail to connect to the server.");
		exit(1);

	global status
	status = rc

# set the callback function
client.on_connect = on_connect


def on_disconnect(client, userdata, rc):
	print "broker disconnected"

client.on_disconnect = on_disconnect	

# Connect to a remote broker asynchronously. 
# This is a non-blocking connect call that can be used with loop_start() 
# to provide very quick start.
client.connect_async(server, port=1883, keepalive=60)

# question: how to know if the server doesn't have a broker?
# one way to solve is to see if the on_connect is ever called

# This is part of the threaded client interface. Call this once to
# start a new thread to process network traffic. This provides an
# alternative to repeatedly calling loop() yourself.
client.loop_start()

# need some time to let the client connect to the broker
i = 0
while status == -1:
	i += 1;
	# if status is not updated for some time, probably the server doesn't have a MQTT broker at all
	if i >= 5:
		print "The server %s doesn't seem to have a MQTT broker running. please check." % (server)
		exit(1)	
	time.sleep(1)
	

print "Now publish the message"

# publish(self, topic, payload=None, qos=0, retain=False)
client.publish("hello", message)

client.loop_stop()
