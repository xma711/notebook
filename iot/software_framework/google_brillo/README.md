Brillo
--------------

brillo is stripped down version of android.

an OS for IoT --> ambitious goal!

for now it is still targeting slightly more powerful devices.
(maybe devices with 32MB or 64MB of RAM; lighting products or thermostat usually are not so powerful)

Brillo has 3 elements: android-based embedded OS, core platform services, and a developer kit.

core services include Weave, which helps devices to securely connect to the network.
weave-enabled devices can seamlessly talk to each other.

weave is a protocol for device discovery, provisioning, authentication and interaction,
which is shipped as a client library, mobile SDK and a cloud-based web service.  
brillo will have weave already embbed in it.  
other devices can achieve the functionality through the client libraries.  
(this actually means that manufacturers do not necessarily have to use brillo, if brillo's requirement on hardware is too high.)

there is also this Libuweave: a tiny weave implementation:
a communication stack intended to be portable to MCU based devices.

references: 
Brillo: http://www.theverge.com/2015/5/28/8683147/google-brillo-weave-internet-of-things-solution  
Brillo vs Apple HomeKit vs AllJoyn vs IoTivity: http://www.techradar.com/news/world-of-tech/which-is-the-best-internet-of-things-platform-1302416  
Brillo: http://www.forbes.com/sites/janakirammsv/2015/10/29/google-brillo-vs-apple-homekit-the-battleground-shifts-to-iot/#347395e84cac

slide: http://events.linuxfoundation.org/sites/events/files/slides/Brillo%20and%20Weave%20-%20Introduction_v3_1.pdf

more reference:
http://nextmarket.co/blogs/smarthomeweekly/29995073-google-brillo-and-weave-an-explainer-and-analysis  

