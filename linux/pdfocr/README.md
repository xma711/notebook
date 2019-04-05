Notes
------------

To convert a pdf of images (each page is an image) to a pdf of texts, use this pdforc, 
which internally uses tesseract-orc package.

However, as of 20181220, there is no release for Ubuntu >= 16.04.  
One solution is to install it inside a docker image Ubuntu:14.04.

Inside the Ubuntu container, just do:  
```
 add-apt-repository ppa:gezakovacs/pdfocr
 apt-get update
 apt-get install pdfocr
```

If add-apt-repository is not found, then manually edit the source file (/etc/apt/sources.list) to add the repository.  
(reference: https://launchpad.net/~gezakovacs/+archive/ubuntu/pdfocr)

In short, it is to add these lines to the sources.list file:
```
deb http://ppa.launchpad.net/gezakovacs/pdfocr/ubuntu trusty main 
deb-src http://ppa.launchpad.net/gezakovacs/pdfocr/ubuntu trusty main 
```

Do an update and install.

To use the software, in terminal, do:  
pdfocr -i input.pdf -o output.pdf



