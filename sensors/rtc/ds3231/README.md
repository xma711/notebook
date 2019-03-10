
if /dev/rtc1 is not found, need to actively load the module by:  
echo ds3231 0x68 > /sys/class/i2c-adapter/i2c-1/new_device

reference: https://learn.adafruit.com/adding-a-real-time-clock-to-beaglebone-black/set-rtc-time


