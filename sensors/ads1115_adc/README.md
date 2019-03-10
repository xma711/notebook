ads1115 (16 bit) / ads1015 (12 bit)
---------------------------

this module has 4 channels. a0 -> channel 0, a1 -> channel 1 and so on.

just connect the analog output to a0/a1/a2/a3 and then treat the whole thing as one single sensor.

however, ads1115 can only samples 860 samples/second. for analog sensor like noise sensor, this sampling rate is too low for high frequency sound. 

the module has configurable 4 i2c addresses.
when addr pin is connected to ground, it is 0x48 (72), 
vdd --> 0x49, 
SDA --> 0x4A, 
SCL --> 0x4B.


Note: NEVER connect a input more than the maximum voltage allowed in to the ads1115!!! Otherwise all readings will be affected!!
e.g. when PGA=1, the maximum allowed voltage is 4.096!

how to calculate the output voltage
-----------------------

ref: https://forums.adafruit.com/viewtopic.php?f=19&t=37355

excerpt:
```
V_in,0 = Input voltage to A0, represented as 2's complement 16-bit
V_in,1 = Input voltage to A1, represented as 2's complement 16-bit
FS = full-scale range, in volts
x = (value of conversion register >> 4) for ADS1015, value of conversion register for ADS1115

For both ADS1015 and ADS1115:
PGA=1, FS = 4.096
PGA=2, FS = 2.048
PGA=4, FS = 1.024
PGA=8, FS = 0.512
PGA=16, FS = 0.256


For ADS1115, when taking a single-ended measurement:
Vin,0 = x / 2^15 * FS

For ADS1115, when taking a differential measurement and MUX[2:0] == 000:
Vin,0 - Vin,1 = x / 2^15 * FS

Questions:
1) Assuming Vdd is within the limits (say 3.3V), the formulas are absolutely independent of Vdd and only depend on FS?
	- ans: yes
2) When taking a single-ended measurement, I can't measure voltages greater than FS (e.g. If FS = 2.048V, measuring anything from 2.049V and greater will always give 32752)?
	- ans: yes
```

from data sheet
----------------------

write to config register:

First byte: 0b10010000 (first 7-bit I 2 C address
followed by a low read/write bit)

Second byte: 0b00000001 (points to Config register)

Third byte: 0b10000100 (MSB of the Config register
to be written)

Fourth byte: 0b10000011 (LSB of the Config register
to be written)

Read Conversion register:

First byte: 0b10010001 (first 7-bit I 2 C address
followed by a high read/write bit)

Second byte: the ADS1113/4/5 response with the
MSB of the Conversion register

Third byte: the ADS1113/4/5 response with the LSB
of the Conversion register


when using PGA setting 1, the FS (Voltage) range is +-4.096V. 
The highest voltage the PGA setting can be selected is +-6.144V,
while the smallest is +-0.256V (more accurate for expected small voltage)  
