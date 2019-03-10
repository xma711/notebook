#!/bin/bash

# http://www.londatiga.net/it/how-to-sign-apk-zip-files/

# rsa key is a private key based on RSA algorithm;
# this line generates key.pem, the private part
openssl genrsa -out key.pem 1024

# this line generate request.pem;
# how what is request.pem used for?
openssl req -new -key key.pem -out request.pem

# generate certificate.pem, the public part
openssl x509 -req -days 9999 -in request.pem -signkey key.pem -out certificate.pem

# generate key.pk8. don't know what this is used for
openssl pkcs8 -topk8 -outform DER -in key.pem -inform PEM -out key.pk8 -nocrypt
