Install
------------------

In Ubuntu, simply sudo apt-get install virtualbox

however, some things need extension package.  
Need to check the virtualbox's version: help->about virtualbox and then check the number at the lower part of the page.

And then download the extension with the correct version from:
http://download.virtualbox.org/virtualbox/

to add a nat, click file (top left panel) -> preference -> network,
then and add a network NAT.

For the mouse pointer integration problem, it may be solved by:
sudo apt-get install virtualbox-guess-(tap tap)

project specific
----------------------

When opening the SEEDAndroid vm, it is stuck at "booting kernel".  
Solution: enable the virtualization support in BIOS!!!

