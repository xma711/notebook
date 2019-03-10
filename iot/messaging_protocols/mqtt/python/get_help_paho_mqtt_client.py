#!/usr/bin/python2

# just to output the help manual ;
# to store it to a file, simply pipe it to a file

import paho.mqtt.client as paho

client = paho.Client()

help(client)
