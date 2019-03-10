#!/usr/bin/python2

# reference: http://mosquitto.org/documentation/python/
# install: sudo pip install paho-mqtt

# more details: https://eclipse.org/paho/clients/python/docs/#constructor-reinitialise

# this is a subscriber that subscribes to all the topics at local host

import paho.mqtt.client as paho
import time
import sys

server="localhost"
topic = "#"

# create the client
client = paho.Client()

# for checking if the broker ever responds to connect_async()
status = -1 

# define a callback function to print a msg when the client connects to the broker

# The value of rc determines success or not:
# 0: Connection successful
# else: connection failed
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

# question: how to know if the server doesn't have a broker???
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
	

print "Now subscribe to the broker"

# when a message has been received on a
# topic that the client subscribes to. The message variable is a
# MQTTMessage that describes all of the message parameters.
# message: an instance of MQTTMessage. This is a class with members topic, payload, qos, retain.
def on_message(client, userdata, message):
	print "on_message: Received a message "
	print "Message = '%s'" % (message)
	print "Userdata = %s" % (userdata)
	print "Message payload = '%s'" % (message.payload)
	print "Message topic = '%s'" % (message.topic)
	

client.on_message = on_message

# callback function for subscribe
def on_subscribe(client, userdata, mid, granted_qos):
	print "client subscribes to the topic successfully"

client.on_subscribe = on_subscribe

# if want to handle different topic differently, create a handler and add it to the client
#def topic_callback(client, userdata, message):
#	print "topic_callback: receive a message: %s" % (message)

# add the handler to a particular topic
# client.message_callback_add(topic, topic_callback);


# subscribe(self, topic, qos=0)
client.subscribe(topic);

# keep the subscriber alive
while True:
	time.sleep(10)

client.loop_stop()
