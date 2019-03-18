AzCopy
-------------------------

Reference:  
	- For Linux: https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-linux?toc=%2fazure%2fstorage%2ffiles%2ftoc.json  
	- For Windows: https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy

The reference has a good explanation on how to use AzCopy.

In the particular scenario of copying files from a file storage to a blob storage,
it can be done by:  
```
azcopy \ 
    --source https://myaccount1.file.core.windows.net/myfileshare/ \
    --destination https://myaccount2.blob.core.windows.net/mycontainer/ \
    --source-key <key1> \
    --dest-key <key2> \
    --recursive
```

when copying a file from file share to blob, a server-side copy operation is carried out.

