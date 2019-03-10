#!/usr/bin/python

import socket
import sys
import getopt
import json

'''
format the input file to json and send it to the server.
the input file should contain the docker images list

'''

# define print help function
def print_help () :
	print >>sys.stderr, '%s -f <inputfile> -s <socket path>' % sys.argv[0]	
	return


# parse arguments
argv=sys.argv[1:] # ignore the program name
inputfile=""
server_address=""
try:
	opts, args = getopt.getopt(argv,"hf:s:",["file=","socket="])
except getopt.GetoptError:
	print "the format of options is wrong"
	print_help()
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print_help()
		sys.exit()
	elif opt in ("-f", "--file"):
		inputfile = arg
	elif opt in ("-s", "--socket"):
		server_address = arg

# check if parameters are set
if (not server_address) or (not inputfile) :
	print "please set server socket address and input file"
	print_help()
    	sys.exit(1)

# read file into a list
with open(inputfile) as f:
    	content = f.readlines()

list_images={} # to form a dictionary
for image in content:
	#print image
	image_content = image.split()
	node_id=int(image_content[0])
	image_name=image_content[1]
	list_images[node_id]=image_name

print list_images

# convert dictionary to json
message=json.dumps(list_images)

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
#server_address = './uds_socket'
print >>sys.stderr, 'connecting to %s' % server_address
try:
    sock.connect(server_address)
except socket.error, msg:
    print >>sys.stderr, msg
    sys.exit(1)

try:
    
    # Send data
    #message = '1234567890 abcdefg hijklmn opqrst uvwxyz.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    #while amount_received < amount_expected:
     #   data = sock.recv(16)
      #  amount_received += len(data)
       # print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
