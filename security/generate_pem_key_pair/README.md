Some explanation
-------------------

Reference: http://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file

.pem and .key (and .csr) are all generated by ssl.  

One implementation of ssl is openssl.

.key file: this is a PEM formatted file containing just the private-key of a specific certificate
and is merely a conventional name and not a standardized one.  
In Apache installs, this frequently resides in /etc/ssl/private

.pem file: this is a container format that may include just the public certificate (e.g. in Apache installs, this is in /etc/ssl/certs)
or may include an entire certificate chain including public key, private key and root certificates.
(more details are in the reference)

.cert  .cer  .crt file: a .pem formatted file with a different extension,
one that is recognized by windows explorer as a certificate, which .pem is not.

.pem .key and .cert are all PEM files.  
PEM on its own is not a certificate. it is just a way of encoding data.  
There are other encoding methods like PKCS#7.


