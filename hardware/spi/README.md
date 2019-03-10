spi
--------------
The Serial Peripheral Interface (SPI) bus is a synchronous serial communication interface specification used for short distance communication, primarily in embedded systems.

SPI devices communicate in full duplex mode using a master-slave architecture with a single master. 
The master device originates the frame for reading and writing. 
Multiple slave devices are supported through selection with individual slave select (SS) lines.

```
                SCLK ----> SCLK
SPI Master      MOSI ----> MOSI    SPI Slave
                MISO <---- MISO
                SS   ----> SS
```
Meaning:
    - SCLK : Serial Clock (output from master).
    - MOSI or DI, DIN: Master Output, Slave Input (output from master).
    - MISO or DO, DOUT: Master Input, Slave Output (output from slave).
    - SS or CS: Slave Select (active low, output from master).


spi on beaglebone
----------------------

reference: http://www.mathworks.com/help/supportpkg/beagleboneio/ug/use-the-beaglebone-black-spi-interface-to-connect-to-a-device.html

    P9_22 (SPI0_SCLK => SCLK) outputs a serial clock signal to synchronize communications.

    P9_18 (SPI0_D1 => MOSI) outputs data to the SPI peripheral device.

    P9_21 (SPIO_DO => MISO) receives data from the SPI peripheral device.

    P9_17 (SPI0_CSO => CE0) enables one SPI peripheral device.

OR

    P9_31 (SPI1_SCLK => SCLK) outputs a serial clock signal to synchronize communications.

    P9_30 (SPI1_D1 => MOSI) outputs data to the SPI peripheral device.

    P9_29 (SPI1_DO => MISO) receives data from the SPI peripheral device.

    P9_28 (SPI1_CSO => CE0) enables one SPI peripheral device.

By default, D1 is MOSI and D0 is MISO (ref: https://groups.google.com/forum/#!topic/beagleboard/R2Gvkjy_QFk)

however, it can be configured to be the other way: http://elinux.org/BeagleBone_Black_Enable_SPIDEV

enable spi
---------------------
reference: http://hipstercircuits.com/enable-spi-with-device-tree-on-beaglebone-black-copy-paste/ (there is a python module to use spi)  
reference: http://elinux.org/BeagleBone_Black_Enable_SPIDEV

enable spi1 at pin p9_28,29,30,31:  
echo BB-SPIDEV1 > /sys/devices/bone_capemgr.*/slots


how to use spi
-------------------

in python2, there is spi; in python3, there is spidev. (pip install spi or spidev)

reference: https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/spi

    #import the library
    from Adafruit_BBIO.SPI import SPI
     
    #Only need to execute one of the following lines:
    #spi = SPI(bus, device) #/dev/spidev<bus>.<device>
    spi = SPI(0,0)	#/dev/spidev1.0
    spi = SPI(0,1)	#/dev/spidev1.1
    spi = SPI(1,0)	#/dev/spidev2.0
    spi = SPI(1,1)	#/dev/spidev2.1

c codes: https://www.kernel.org/doc/Documentation/spi/spidev_test.c

python codes for spi: https://github.com/raspberrypi-aa/raspberrypi-aa/ 
and some explanation on these codes: http://raspberrypi-aa.github.io/session3/spi.html


exmaple on github
----------------------

https://github.com/roice/gdm3d-uav

seems that this one can be used to run the ads1256 in bbb.

there are other github repos that use ads1256. just search it in codes.
