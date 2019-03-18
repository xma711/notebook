Use storage account
-------------------------

In Dashboard, follow the steps to create a storage account.

Apparently i can create multiple storage account. just imagine each is one dropbox account.

Inside one storage account, there are different 'services': blobs, files, tables, queues..

Assume we want to create a storage to store files, then click 'Files'.

Follow the steps to create a storage for files. minimally 1 GB.

After creating one named 'files1', we want to access the whole directory in a local computer, just like Dropbox.
Luckily azure does support linux machine's access.

To mount the folder in the local linux computer, click the '...' beside the folder 'files1' in browser,
then click 'connect'.
In the 'connecting from linux', there is a full command line to mount the file in the local computer.  
Before that, note that i have to install this cifs-utils first, using: sudo apt-get install cifs-utils (ref: https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-linux)

also need to create the mount point first: sudo mkdir /mnt/azure_files1

in my case, the command is: sudo mount -t cifs //xma1.file.core.windows.net/files1 /mnt/azure_files1 -o vers=3.0,username=xma1,password=longlonglongpasswordgivenbyazure,dir_mode=0777,file_mode=0777,sec=ntlmssp

after this, i can access the folder as if it is a dropbox folder.  
E.g. if i 'touch hello.txt' in the folder, the file will be auto-synced to the remote folder.


Access azure storage account using 'Microsoft Azure Storage Explorer'
-----------------------------------------------------------------------

Firstly, need to install .net packages. 
Instructions can be found here: https://dotnet.microsoft.com/download/linux-package-manager/ubuntu18-04/sdk-current
(assume ubuntu 18.04)

in short, register product repository for once per machine:

```
wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

then install .net sdk:

```
sudo add-apt-repository universe
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install dotnet-sdk-2.2
```

then download the Azure storage explorer here: https://azure.microsoft.com/en-us/features/storage-explorer/

extract the linux tar file.  
In the extracted folder, run ./StorageExplorer

To add an storage account using SAS in the storage explorer, click view -> account management -> add an account,
-> use a sas URI -> fill in the fields, esp the URI (example: https://xmatest.blob.core.windows.net/?sv=SAS_KEY). 


Different storage types
------------------------------

In a storage account, different storage types can be defined.

'File' storage is easier to be understood. it is just a storage specially for files.

'Block Blob' storage is used for streaming and storing documents, videos pictures, backups,
and other unstructured text or binary data.

The word 'blob' stands for 'Binary Large OBject', which is a collection of binary data stored as a single entity in a database management system.
(reference: https://en.wikipedia.org/wiki/Binary_large_object)

Even for 'Block Blob', there are 4 choices: general purpose v2, premium blobs, blob storage, general purpose v1.  
Https://azure.microsoft.com/en-us/pricing/details/storage/blobs/ says that blob storage accounts provide access to the latest features, but not to page blobs, files, queues or tables.


Pricing
-----------------------------

Reference: https://azure.microsoft.com/en-us/pricing/details/storage/page-blobs/

for Redundancy, LRS seems the cheapeast.

Standard storage is cheaper than the premium storage.

For 'Files' storage type, as on 4th Dec 2018, with choices of LRS, Japan West, General Purpose v2, 
the standard data storage price is $0.06 (USD) per GB per month, and $0.015 per 10,000 common operations.

For 'Block Blob' storage (general purpose v2), with the same setting, the price is about $0.02 per GB per month,
$0.05 per 10,000 write and list operations, and $0.004 per 10,000 read operations.  
Also, 'HOT' type is actually cheaper than 'COOL' type on the data taransfer cost. but COOl should be cheaper for the storage pricing than HOT type.  
(reference for block blob pricing: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/ )

also, pricing for 'Blob Storage' and 'General Purpose v2' are identical for Block Blob storage, 
except for data write and early deletion charges in the Cool tier.


Recommended choice for the storage account
-----------------------------

After all the reading, the recommended choice for the storage account i think is:
Standard, LRS, General purpose v2, HOT.

Note that this is the account only. further, i need to choose the 'container', which can have multiple types to choose, such as blob, files... (ok.. this is confusing..)
I think the pricing refers to the types of storages used inside the storage account.


Account key
-----------------------------

In the storage account, click 'Access Keys', there will be 2 account keys.
Any one of them can be used.

Account key is like the root password to this account so it has to be protected safely.  
I think there is no read/write access control when using the account key.


Shared access signatures (SAS)
---------------------------------

A shared access signature (SAS) provides you with a way to grant limited access to objects in your storage account to other clients, without exposing your account key.

A SAS gives you granular control over the type of access you grant to clients who have the SAS, e.g. validity period, read/write permission, etc.  
(reference: https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1)

To create a SAS, go to the storage account, click 'Shared access signature', choose the permissions accordingly, and click generate the keys.


Importantly, when using the SAS key in the BlockBlobService(), cannot copy the '?' in the first character in the SAS key string provided by the Azure interface.  
(reference: https://github.com/Azure/azure-storage-python/issues/301)

