# some generic utilities that can be used by other python scripts

import subprocess
import time
import datetime
import os
import threading

# output status choices
INFO=Info=info=0
ERROR=Error=error=1
WARNING=warning=2
timeout_ssh=5 # set a limit on waiting time

# output status to the status file
# need to make this thread-safe
def output_status(folder_dir, status, type_status):
	if not os.path.isdir(folder_dir):
		print "Warning: directory %s does not exist. exit." % (folder_dir)
		print "Not outputing any status."
		return

        type_str=" [INFO]"
        if type_status == INFO or type_status == info:
                type_str = " [INFO]"
        elif type_status == ERROR or type_status == error:
                type_str = " [ERROR]"

        filename=folder_dir+"/status.txt"
	# need to add 8 hours
        timenow=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        text=timenow + type_str +": " +  status + "\n"
        with open(filename, "a") as myfile:
                myfile.write(text)
        myfile.close()


# send a command to a node, which the node will execute
def send_cmd_to_a_node(cmd, ip):
	cmd_linux="ssh -o ConnectTimeout=" + str(timeout_ssh) + " root@"+ip+" "+cmd
	out, err = run_linux_command(cmd_linux)
	num_retries=10 # set the retry numbers
	i=0
	# this part doesn't work. when there is a time out, the ret has nothing. when there is no time out, ret has nothing either.
	while "Connection timed out" in err:
		print "Fail to send command to Node %s. Retry Number %d" % (ip, i+1)
		time.sleep(1)
		out, err = run_linux_command(cmd_linux)
		if i >= num_retries:
			break
		i=i+1
	if "Connection timed out" in err:
		print "Fail to send command to Node %s. Please check the network connection of this node. Return 'timeout'" % (ip)
		return "timeout"
	else:
		return out

# run linux command and return the output
# doesn't seem to be able to run piping commands like ">"
def run_linux_command(cmd):
	print "run linux command: %s" % (cmd)
	output,err = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	if output:
		print "Output from running the command is:\n%s" % (output)
	if err:
		print "Error from running the command is:\n%s" % (err)

	return [output, err]



# for sending commands in its own thread
class sendCommandsThread (threading.Thread):
	def __init__(self, node_id, ip_addr, cmd):
		threading.Thread.__init__(self)
		self.node_id = node_id
		self.ip_addr = ip_addr
		self.cmd = cmd

	# send a command to a node for it to run
	def run(self):
		# print "The command that will be run in node %s is: %s" % (self.ip_addr, self.cmd)
		self._return = send_cmd_to_a_node(self.cmd, self.ip_addr)

	# return the messages from running the commands
	def join(self):
		threading.Thread.join(self)
		return self._return

	# return the node id
	def get_node_id(self):
		return self.node_id
		

# run local linux commands in threads
class runLocalCommandsThread (threading.Thread):
	def __init__(self, node_id, cmd):
		threading.Thread.__init__(self)
		self.node_id = node_id
		self.cmd = cmd

	# send a command to a node for it to run
	def run(self):
		# print "The command that will be run in node %s is: %s" % (self.ip_addr, self.cmd)
		self._out, self._err = run_linux_command(self.cmd)

	# return the messages from running the commands
	def join(self):
		threading.Thread.join(self)
		return [self._out, self._err]

	# return the node id
	def get_node_id(self):
		return self.node_id

# send a list of commands to a list of nodes in sequential
def send_command_list_to_nodes_sequential(cmd_remote_dict, nodes_list, nodes_ip_dict):
	ret_msgs={}
	for node in nodes_list:
		out = send_cmd_to_a_node(cmd_remote_dict[node], nodes_ip_dict[node])
		ret_msgs[node] = out
	# return all output messages
	return ret_msgs

# send an idential command to a list of nodes in sequential
def send_identical_command_to_nodes_sequential(cmd_remote, nodes_list, nodes_ip_dict):
	cmd_remote_dict = {}
	# create a dictionary of identical commands
	for node in nodes_list:
		cmd_remote_dict[node]= cmd_remote
	send_command_list_to_nodes_sequential(cmd_remote_dict, nodes_list, nodes_ip_dict)


# send a list of commands to a list of nodes in parallel
def send_command_list_to_nodes_parallel(cmd_remote_dict, nodes_list, nodes_ip_dict):
	threads = []
	ret_msgs = {}
	for node in nodes_list:
		# create a thread for each node
		thread = sendCommandsThread(node, nodes_ip_dict[node], cmd_remote_dict[node])
		threads.append(thread)

	# start the threads
	for t in threads:
		t.start()
	
	# wait for all threads to completer
	for t in threads:
		out = t.join()
		node_id = t.get_node_id()
		ret_msgs[node_id] = out

	# return all output messages
	return ret_msgs

# send an idential command to a list of nodes in parallel
def send_identical_command_to_nodes_parallel(cmd_remote, nodes_list, nodes_ip_dict):
	cmd_remote_dict = {}
	# create a dictionary of identical commands
	for node in nodes_list:
		cmd_remote_dict[node]= cmd_remote
	return send_command_list_to_nodes_parallel(cmd_remote_dict, nodes_list, nodes_ip_dict)


# send a list of commands to a list of nodes in parallel, n at a time
def send_command_list_to_nodes_parallel_n_at_a_time(cmd_remote_dict, nodes_list, nodes_ip_dict, n):
	ret_msgs={}
	num = len(nodes_list)
	# how to get sublist: list[first:last], last is not included. 
	first = 0
	last = 0
	
	# when last equals to or larger than num, it means all items in the list must have been processed
	while last < num:
		first = last
		last = last + n	
		sublist = nodes_list[first:last]
			
		print "Send command to a sub list of nodes:"
		print sublist
		ret_dict = send_command_list_to_nodes_parallel(cmd_remote_dict, sublist, nodes_ip_dict)
		ret_msgs.update(ret_dict)

	return ret_msgs


# send an identical command to a list of nodes, n nodes at a time in parallel
# this can be used to reduce collision in the channel
def send_identical_command_to_nodes_parallel_n_at_a_time(cmd_remote, nodes_list, nodes_ip_dict, n):
	cmd_remote_dict = {}
	# create a dictionary of identical commands
	for node in nodes_list:
		cmd_remote_dict[node]= cmd_remote
	return send_command_list_to_nodes_parallel_n_at_a_time(cmd_remote_dict, nodes_list, nodes_ip_dict, n)


# run a list of local commands in parallel
def run_local_command_list_parallel(cmd_dict):
	threads = []
	ret_msgs = {}

	nodes_list = cmd_dict.keys()
	nodes_list.sort()

	for node in nodes_list:
		# create a thread for each node
		thread = runLocalCommandsThread(node, cmd_dict[node])
		threads.append(thread)

	# start the threads
	for t in threads:
		t.start()
	
	# wait for all threads to completer
	for t in threads:
		out, err = t.join()
		node_id = t.get_node_id()
		ret_msgs[node_id] = [out, err]

	# return all output messages
	return ret_msgs		


# run a list of commands locally in parallel, n at a time
def run_local_command_list_parallel_n_at_a_time(cmd_dict, n):
	ret_msgs={}
	nodes_list = cmd_dict.keys()
	nodes_list.sort()
	num = len(nodes_list)
	cmd_sub_dict={}
	# how to get sublist: list[first:last], last is not included. 
	first = 0
	last = 0
	
	# when last equals to or larger than num, it means all items in the list must have been processed
	while last < num:
		first = last
		last = last + n	
		sublist = nodes_list[first:last]

		cmd_sub_dict={}
		for node in sublist:
			cmd_sub_dict[node] = cmd_dict[node]
		print "Send command to a sub list of nodes:"
		print sublist
		ret_dict = run_local_command_list_parallel(cmd_sub_dict)
		ret_msgs.update(ret_dict)

	return ret_msgs
