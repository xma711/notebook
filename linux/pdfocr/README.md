notes
------------

to convert a pdf of images (each page is an image) to a pdf of texts, use this pdforc, 
which internally uses tesseract-orc package.

however, as of 20181220, there is no release for ubuntu >= 16.04.  
the way i install it is to use docker image ubuntu:14.04.

inside the ubuntu container, just do:  
```
 add-apt-repository ppa:gezakovacs/pdfocr
 apt-get update
 apt-get install pdfocr
```

if add-apt-repository is not found, then manually edit the source file (/etc/apt/sources.list) to add the repository.  
(reference: https://launchpad.net/~gezakovacs/+archive/ubuntu/pdfocr)

in short, it is to add these lines to the sources.list file:
```
deb http://ppa.launchpad.net/gezakovacs/pdfocr/ubuntu trusty main 
deb-src http://ppa.launchpad.net/gezakovacs/pdfocr/ubuntu trusty main 
```

do an update and install.

to use the software, in terminal, do:  
pdfocr -i input.pdf -o output.pdf



