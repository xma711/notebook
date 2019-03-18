Sftp
------------------------------

Sftp comes with the ssh server.

Nothing needs to do to enable it.

From a client:  
sftp user@ip_address  
then the client can browse the "user" home directory in the server.

To get a file, cd to the right directory and  
get filename  
(this gets the file from remote server to the local computer in the directory where the sftp session is started)

to send a file to remote:  
cd to the right directory in the remote machine and
put localfile

reference: https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server


ftp
-------------------------------

The steps to use ftp:
	- ftp server_ip
	- enter username
	- enter password
	- put/get filename to send or get a filename

