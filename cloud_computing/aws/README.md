AWS
-------------------

Reference: http://techgenix.com/three-most-widely-used-amazon-web-services/

the 3 most popular services are Amazon Elastic Compute Cloud (EC2), Amazon Elastic Block Store (EBS), and Amazon Simple Storage Service (S3).

Ref (EC2): https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud  
EC2 allows users to rent virtual computers on which to run their own computer applications.  
A user can boot an Amazon Machine Image (AMI) to configure a virtual machine, which is called an "instance", containing any software desired.
The fee is charged by the hours for active servers.

EBS provides raw block-level storage that can be attached to EC2 instances (virtual machines).
These block devices can then be used like any raw block device.  
In a typical use case, this includes formatting the device with a filesystem (e.g. ext4) and mounting the said filesystem.
EBS also supports a number a advanced features, like snapshotting and cloning.

Ref(S3): https://en.wikipedia.org/wiki/Amazon_S3  
S3 provides highly salable object storage and is suited to both small and large repositories of objects.  
S3 provides storages through web services interfaces (REST, SOAP and BitTorrent).

Differences between S3 and EBS   
(ref: http://www.cloudberrylab.com/blog/amazon-s3-vs-amazon-ebs/)  
S3 stores data as objects in a flat environment (without a hierarchy).
Each object/file in the storage contains a header with associated sequence of bytes from 0byte to 5TB.  
Each object is associated with a unique identifier (key), so access to them can be obtained through web requests from anywhere.  
S3 also allows to host static website content. you can get access to it either from S3 bucket or through content delivery network (CDN) AWS CloudFront..

EBS store data as blocks of the same size and organizes them through the hierarchy similar to a traditional file system.
EBS us bit a standalone storage service like S3 so you can use it only in combination with EC2 instance.  
There are 3 volume types of EBS:   
general purpose (SSD) volumes (good fit for applications that need a lot of read and write operations, like sql, postgreSQL, etc),   
Provisioned IOPS (SSD) volumes (designed for heavy workloads of read/write),   
and Magnetic volumes (low-cost volume that can be used for testing and development).


Testing
----------------

Follow: http://www.brianlinkletter.com/create-a-free-virtual-private-server-on-amazon-web-services/

anyway i created an ec2 instance (a vm) using t2.micro type;
also i added a new key, which can be generated from the amazon web interface (i have to download the pem private-key file).  
Later i can access it using ssh -i ~/.ssh/aws-test1.pem  ubuntu@54.218.142.214  
not sure if this will incur a cost to my account since my account is not new.
