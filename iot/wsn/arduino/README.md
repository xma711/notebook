Arduino
-----------------

reference: book "Sams Teach Yourself Arduino Programming in 24 hours", 2015

to download popular libraries: https://www.arduino.cc/en/Reference/Libraries

Arduino is an open source microcontroller platform.  
It is a microcontroller, which internally has a CPU, memory and I/O ports all on the same chip.

Arduino developers selected the Atmel Atmega AVR family of microcontroller chips to power the arduino.  
such a microcontroller has several features built in:  
	- flash memory for storing program codes (only);  
	- SRAM for storing program data (it is RAM);  
	- EEPROM for storing long-term data (can be used to store data after power off arduino. max num times of write: 100,000);  
	- digital input and output ports;  
	- ADC

Arduino Uno is the workhorse of the arduino family. 
it uses Atmega328 microcontroller, having 14 digital I/O, 6 analog inputs, 6 PWM, 1 I2C, 1 SPI, 1 UART.
It has 32KB Flash, 2KB SRAM, 1KB EEPROM.

arduino due uses the 32-bit ARM Cortex-M3 cpu (not the usual Atmel Atmega AVR).
it has 54 digital I/O, 12 PWM, 12 analog inputs, and 4 UART..
it has 96KB SRAM, 512KB Flash. no EEPROM.

other notable Arduino: 
Leonardo (similar to uno), Mega (more powerful), Micro (small size), Esplora (game controller), 
Yun (2 processors, one for linux), LilyPad (small round, can put on clothes).

Arduino shields: ethernet shield, LCD shield, Motor shield, prototype shield.


Arduino IDE
-----------------

the usual upload assumes an arduino board has bootloader installed already.
this is the default and recommended way.

to upload a bootloader to a fresh arduino, we need to use the programmer option in the IDE. 
to use this option, we also need a hardware programmer to connect the arduino (spi) to the computer. 
this physical programmer can be created using another arduino uno.. or can be purchased off the shelf.


write data to flash
------------------------

we can't do this when the program is running, but we can do this when the program is uploaded to the flash.  
the way to do it is to declare some special variables, and then they will magically be stored in the flash.
however, we won't be able to change them during runtime.

to use this, need to \#include <avr/pgmspace.h>.  
one example to declare a variable that will be stored in flash: prog_uint16_t maxTries PROGMEM = 10; (note that PROGMEM is a keyword that has to be there)

to access the variables in flash, use some special functions from pgmspace.h.  
one common way is to declare a variable in SPRAM (normal way), and then copy the data from flash to this flash when needed.  
one example: char buffer[50]; strcpy_p (buffer, messsage1); // where strcpy_p is a special function, message1 is stored in flash.  
there are other functions like pgm_read_byte, pgm_read_word, strcmp_p(), strlen_p(). just google to know how to use them.


write data to EEPROM
------------------------

this can be done during the run time.  
but note that EEPROM becomes unreliable after about 100,000 writes.

to do this, \#include <EEPROM.h>

to read: read(address);  
to write: write(address, value);

the address can be 0 to the maximum number. 
in uno, because it has 1KB EEPROM, so the maximum number is 1023.  
note that the address will be wrapped around if the address is bigger than the maximum number, which will cause problems.


standard libraries
------------------

Wire: I2C or TWI   
Wifi: wireless network  
SD: read and write data on an SD card  
GSM: functions for connecting to mobile phone network using the GSM shield.  
Ethernet: functions for accessing networks using Ethernet shield  
SPI: spi port  
LiquidCrystal: write text to and LCD display  
(there are many other libraries. just google whenever we need to use a shield or some special functions.)

btw, each library is a C++ class.  
and the object name that has been declared in the library is exactly the same as the header file name (without the .h). 
--> the library usually already creates an object for users.


contributed libraries
-----------------------

download a wanted library (a zip file) from website, usually http://playground.arduino.cc

click Sketch > Import libraries > Add library. then add the zip file.


creating own libraries
--------------------------

write a .h and a .cpp file ( e.g. MyLib.{h, cpp} ),
then create a folder with the same name as the file (e.g. MyLib).
then create a zip file (e.g. Mylib.zip).

finally, we can add the library to arduino IDE using the normal import way.

(this is a bit troublesome though, when multiple peoples are updating the same source files using version control)  
(--> solution: we can manually crate the library folder in the local Arduino library folder and copy the files manually.)

btw, in the .cpp file, we can create an object: MyLibClass MyLib;  
and in .h file, extern MyLibClass Mylib;  
this is to create an existing object for users to use directly.


digital I/O
------------------

set pin modes: pinmode(pinNum, MODE);  
MODE can be INPUT, OUTPUT, INPUT_PULLUP.
(the purpose of INPUT_PULLUP can be found below.)

when mode is OUTPUT, to write a pin, use: digitalWrite(pinNum, LOW/HIGH); // output 0 V or 5 V  

when the mode is INPUT, to read a pin, use: int result = digitalRead(pinNum); 
where the result returned is HIGH (1) or LOW (0).  

one possible issue: input flapping, when the digital input doesn't connect to anything while we try to read the value.  
this can happen when there involves a button to make the digital input HIGH or LOW.
we cannot simply connect one end of the button to ground and the other end of button to the digital input. 
because when the button is release, the digital input is connected to nothing.  
the solution to this is either the pullup circuit or pulldown circuit.  
e.g. +5v --- resistor --- digital input -- push button --- resistor --- ground.  
in such a circuit, when the button is released, input is connected to 5v. 
when button is pushed, input will take gnd as the preference.  
pull down circuit is a similar concept.

another way is to use the internal pullup. 
when using pinMode(pinNum, INPUT_PULLUP);  
it will activate the internal pullup resistor so that the digital input by default will be HIGH.  
this is much easier compared to creating an external pullup circuit!

be careful when using pin 13 as an input, because it connects to an internal resistor and a led.
need to provide a full +5v when using this as input.

to detect if an input changes value, one way is to use interrupt (will be discussed later).


input and output analog signal
-------------------------------------

to read analog input: input = analogRead(A0); // for uno, there are A0 to A5.

uno's ADC's resolution is 10 bit, so the reading will be from 0 to 1023.
when it is 1023, it corresponds to +5v at the input.

(seems that it cannot read negative voltage. how?)  
(is this the reason that most of the time we use an external ADC thru i2c?)  
(one solution is to use an external circuits made of 3 resistors to map the +xV and -xV to 0V and 5V. 
one example: http://electronics.stackexchange.com/questions/108320/read-positive-and-negative-voltage-in-arduino)

to map the input reading to another range, we can use a built-in function 'map'.  
e.g. to map the reading from "0 to 1023" to "0 to 255", we can use:
input = map(analogRead(A0), 0, 1023, 0, 255); // obviously internally it uses a linear mapping

by default the reference voltage is +5v.  
to change this, there are 2 ways: internal and external.

internally, we can change the reference voltage to +1.1 v: analogReference(INTERNAL); 
// in uno, INTERNAL is a constant that will make the reference to be 1.1V  
// in Anduino Mega, it has 2 choices: INTERNAL1V1 (1.1 V) and INTERNAL2V56 (2.56 V)

to change the reference voltage externally, we can apply a reference voltage to AREF pin,
and in the codes we need to set: analogReference(EXTERNAL); // and that's it!

to simulate an analog output, we can use the PWM at some digital pins with a '~' before the number on the silkscreen.  
usage: analogwrite(pin, dutycycle); 
where dutycycle ranges from 0 to 255; 255 means 100% duty cycle, generating +5v all the time.

note that Arduino Leonardo does have a DAC to generate a real analog output.  
most of other arduino need to use PWM to simulate an analog output.


interrupts
------------------

there are 3 types of interrupts supported: external (built-in to cpu), pin change interrupts (software based), and timer interrupts.

for external interrupts, arduino usually has only 2 digital interfaces supported.
e.g. uno has pin 2 (INT0) and pin 3 (INT1) that can be attached a interrupt service routine (ISR).  
the usage is: attachInterrupt(interrupt, isr, mode);
where 'interrupt' is the number (0 or 1), isr is the callback function, mode can be RISING, FALLING, CHANGE, LOW (don't use LOW normally).

note that inside the ISR, it can still access to global variables.
just declare a void function() {} and attach it to the external interrupts.  

(it seems that when using mode=FALLING, the digital pin is use INPUT_PULLUP by default (so that it is HIGH by default).)

one potential problem is switch bouncing if we use a mechanical switch to trigger to external interrupt.
when we press it, there could be multiple interrupts occurred. 
to solve this, use a capacitor across the two pins of the switch.

regarding pin change interrupt, the advantage is that we can use any digital pin.  
the disadvantage is that our code needs to decode which interface generated the pin change interrupt, and based on what type of signal change (RISING, FALLING, etc).

luckily, the PinChangeInt Library comes to our rescue.  
once we include this library (we need to download and install this library manually), 
using pin change interrupt is as easy as using the external interrupts.  
the usage is (an example):  
 \#include <PinChangeInt.h>  
pinMode(7, INPUT);  
PCintPort::attachInterrupt(7, callbackFunction, FALLING);

that is it! almost exactly the same as the external interrupt case.

regarding the timer interrupts, there is (at least) one built-in timer that comes with Arduino.  
we can set the repeating duration and then attach a routine to it.  
we need to download and install the TimerOne library manually.  
the usage:  
```
 \#include <TimerOne.h>  
Timer1.initialize(1000000); // the unit is microseconds; so here it is 1 second  
Timer1.attachInterrupt(callbackFunction); // just put these codes in setup{}
```

the timer interrupt could be very useful when we try to sample sensor data periodically.

btw to temporarily ignore all interrupts, use: nointerrupts();  
to resume all interrupts: interrupts();

to disable one external interrupt, use: detachInterrupt(0/1);  


serial communication: serial
-----------------------

there are 3 different communication protocols: standard serial interface (UART), the serial peripheral interface (SPI) and inter-integrated circuit (I2C) protocol.

for uno, the serial port is at pin 0 and 1 (it uses 2 interfaces), and one is RX and the other is TX.

in fact, arduino comes with a built-in serial-to-USB adapter so that we can plug the arduino to workstation directly.

question: when i use the serial port to communicate with a device like XBEE, can i still connect it to a workstation?

we can use the Serial library to send and receive data. 
some notable functions (need to add "Serial." in front of the functions when using):  
available(): returns the number of bytes available for reading from the serial port  
begin(rate ): set data rate, e.g. 9600, 56000.  
print(text) / println(text): sedn data to interface as ASCII text   
write(val): send val string as a series of bytes.  
read(): return the first byte of incoming data; -1 if no data  
readBytes(buffer, length): read length bytes of incoming data into buffer array  
parseInt(): return the first valid integer value


serial communication: SPI
-----------------------------------

SPI: 3 interfaces:  
	- MISO: for slave sending data to master  
	- MOSI: for master sending data to slave  
	- SCK: clock signal to synchronize the data transfer  
there is also the SS pin. the master must set the slave SS pin to LOW when it communicates with that specific slave device.

for uno, it can only connects to one slave device because it has only one SPI.  
(question: cannot connect to multiple devices like i2c? because of the single SS interface on uno?)

the spi interfaces are provided in the ICSP headers.  
the same pins are also at pin 10, 11, 12 and 13.
once spi is used, there digital pins cannot be used for other purposes.

arduino comes with a spi library.  
notable functions:  
begin(): init the spi interface pins  
end(): done  
setBitOrder(mode): set how arduino sends data out the spi inteface  
setClockDivider(divider): set the timing clock speed on the sck interface  
setDataMode(mode): sets the spi data mode on the interface  
transfer(val): sends 1 byte of data out the SPI bus, and retrieves 1 byte of data from the bus.


serial communication: I2C
---------------------------------

to eliminate the extra slave select line, the I2C protocol uses addresses to determine which data is intended for which device.  
each slave device has a unique address assigned to it.  
there are 2 interfaces:  SDA for data sending and SCL for synchronizing data transfer.

slave devices can only send data when prompted by the master device.

different arduino models provide i2c interfaces at different pins.  
e.g. uno's i2c is at A4 and A5, due's is at pin 20 and 21, Leonardo's is at pin 2 and 3.  
due actually has one more i2c interface.

to use i2c in arduino, we need to use this library: Wire, which is installed by default.  
the notable functions:  
begin( [address if want to be a slave] ): init the i2c interface. when there is no address, it will be the master device.  
beginTransmission(address): start a transmission session to the slave device; it is a bit like tcp, session to a slave will be started and ended explicitly.  
write( data [, length] ): send data in the transmission session with a slave device. data can be a single byte or a C-style string. can be an array too but have to specify the length.  
endTransmission(address): terminate the session.  
onReceive(callbackFunction): for slave to call a function when it receives data from master device.  
onRequest(callbackFunction): for master to call a function when it receives data from a slave device.  
read(): read a byte of data from a master device.

one application: we can use i2c to let multiple arduino units communicate.  
we can let one arduino as the master and connect the others as slaves on the i2c bus.  
the master can request sensor data from each of the slaves to combine readings.


analog sensors
------------------------

there are 3 types of analog sensors (at least) that output different electrical properties: voltage, resistance, and capacitance.  

if the voltage output is within +5v and 0v, then it is very simply.
just connect the voltage output to one of the analog inputs on arduino (e.g. A0).  
if the voltage output is larger than +5v (when the minimum is still positive), we need a voltage divider to do the job:  
power supply --- sensor_positive_pin --- sensor output pin --- R1 ---- (this point connects to A0) --- R2 --- GND.  
it is not hard to see that the voltage to A0 is ( R2/(R1+R2) * Sensor output voltage ).  
we can adjust R1 and R2 to have the intended range we want.

when the output can have negative voltage, we need to convert it to the proper range. 
one example to do this is shown here: http://electronics.stackexchange.com/questions/108320/read-positive-and-negative-voltage-in-arduino

if we want to reduce the sensitivity, we can do this in software using the map() function.
we can just map the output range to a smaller range so that the value changes become smaller (one extreme case is to map it to 0 or 1..) 

to convert the voltage to something meaningful (e.g. temperature), we need to consult the datasheet of the sensor.

when the output from the sensor is resistance change, it is quite easy to convert it to voltage, by using a voltage divider again.  
the connection is: +5v --- sensor --- (this point connects to A0) --- R1 --- GND.  
when the sensor's output resistance changes, the voltage to A0 changes so that we can determine the resistance output from the sensor.

when the output from the (touch) sensor is capacitance, we need to measure the time taken for the capacitance to discharge in order to determine when there is a change in capacitance.  
one connection is: digital pin 7 --- R1 --- (the sensor wire connects to this point) --- digital pin 5.  (pin 7 and 5 are just examples)  
we can download an library CapacitiveSensor to do the job for us.  
the usage is something like:  
```
 \#include <CapacitiveSensor.h>  
CapacitiveSensor Sensor = CapacitiveSensor(7, 5);  
long sensorValue = Sensor.capacitiveSensor(30); // when this value changes, it means the sensor wire is touched.
```

LCD display
--------------------

two types of LCD: alphanumeric LCD device and Graphical LCD device.

the most common alphanumeric LCD is the 16x2 LCD device, which can display 2 lines of 16 characters.

LCD device usually has a chip to control the dots. 
one common controller chip is HD44780.  
the interfaces for LCD with this chip is:  
pin 1: VSS, GND connection  
pin 2: VDD, +5V  
pin 3: V0, contrast adjustment  
pin 4: RS, Register selection  
pin 5: RW, Read/Write  
pin 6: EN, enable  
pin 7 to pin 14: D0 to D7, the data lines  
pin 15: A, Backlight anode  
pin 16: K, backlight cathod

HD44780 has 2 modes: 8-bit mode and 4-bit mode

when using 4-bit mode, we only have to connect 6 main pins to arduino (and another 6 pins for power and controlling):  
arduino    lcd  
2          4 (RS)  
3          6 (EN)  
4          11 (D4)  
5          12 (D5)  
6          13 (D6)  
7          14 (D7)

Other 6 pins: pin1 (VSS) to GND, pin2 (VDD) to +5v, pin3 (V0) to +5v through a potentiometer, pin 5 (RW) to GND, pin 15 (Backlight anode) to +5v through a resistor, and pin 16 (backlight cathod) to GND

Then we can use the LiquidCrystal library to control the LCD, which comes by default.

the functions:  
LiquidCrystal(rs, en, d4, d5, d6, d7): the constructor; just input the corresponding arduino pins. e.g. LiquidCrystal lcd(2,3,4,5,6,7);  
begin(num_cols, num_rows): define the number of rows and columns in the LCD.  
print (data, BASE): print the text to the LCD device.  
setCursor(col, row): place the cursor at a specific row and column location.

another version of LCD with the same chip is the LCD shield created by Adafruit.  
it uses another layer to control the chip, thru the i2c interface.  
so the only data connection between the LCD shield and arduino is the 2 i2c interfaces: SDA and SCL.

To use this shield, need to download and install the Adafruit_RGBLCDShield library.  
link: https://learn.adafruit.com/rgb-lcd-shield/using-the-rgb-lcd-shield

the function names are all the same as the LiquidCrystal library, except the constructor.  
usages:  
Adafruit_RGBLCDShield lcd = Adafruit_RGBLCDShield();  
lcd.begin(16,2);  
lcd.setCursor(0,1);  
lcd.print("This is a test");

there are 2 more functions:  
setBacklightColor: set the background color of RGB LCD  
readButton: retrieve the status of all the buttons on the LCD shield.


Ethernet shield
------------------------

there are ethernet shield and wifi shield.  
both have their own libraries.

the ethernet shield allows an arduino to connect to an ethernet network.  
it can act as a client or as a server.  
normally it runs TCP, but there is a library for it to use UDP.

ethernet shield use SPI for communication with arduino.

one example:  
```
 \#include <Ethernet.h>  
 \#include <SPI.h>  
byte mac[] = {0x90, 0xa2 ... (6 numbers here)};  
EthernetClient client; // create a client  
// in setup() function  
Ethernet.begin(mac); // not specify ip this time; to rely on router's DHCP to allocate an ip address  
if (client.connect("server_address.com", 21) ) {  
  // connected  
}  
// in loop()  
if (client.connected() ) {  
 // connected  
}  
```

the EthernetServer class allows the arduino to behave as a TCP server.  
The EthernetUDP classprovides methods for interacting on the network as a UDP device.

with the network capability, we can let the arduino device behave as a web server,
which is able to reply to HTTP request.  
one example:  
```
EthernetServer server(80); // use port 80  
// in loop():  
if (client.connected()) {  
  int temp = getTemperature(); // get temperature reading  
  client.println("HTTP/1.1 200 OK"); // send status  
  client.println("Content-Type: text/html"); // sender headers  
  client.println("Connection: close");  
  client.println(); // done with headers  
  client.println("<!DOCTYPE HTML>"); // now start with html  
  ... (other html) ...  
  client.println("<h2>The current temperature is ");  
  client.print(temp); // print temperature value  
  client.println("&deg; F</h2>"); // close <h2> tag  
  ... (other html)...  
  client.stop();  
}
```

other more advanced usage includes creating a link in the html, 
once the user click the link, the http server will do something like turning a led on.


SD card reader
-----------------

there is a library for SD card reader.

the ethernet shield has a SD card reader inside.  
there is a standalone SD card shield: Micro-SD breakout board, Adafruit Data logging shield, the wave shield..

example:  
SD.begin(4); // 4 is the pin number that acts as SS pin to control SD card  
File myfile;  
myfile = SD.open("test.txt", FILE_WRITE); // the file object is very similar to the file functions in C


do a project: steps
---------------------

1. determine project requirements ..  
	- what type of data does the project need to monitor?  
	- what type of equipment does the project need to control?  
	- does the data need to be saved?  
	- does the project need to connect to a network?

2. determine interface requirements:  
	- what analog and digital interfaces are needed?  
	- do they cause any conflicts? (if yes, what other boards are suitable?)  

3. list down components: component and quantity

4. create a schematic, maybe in a google word document

5. create the breadboard circuit

6. design the sketch (software program):  
	- which arduino libraries are needed?  
	- what codes will be in setup()?  
	- what codes will be in loop()?  
	- whether any extra functions are needed? 

7. write the sketch (programming!):  

8. test the sketch:  
	- the easiest way (not the best) is to use a serial monitor  
	- should use unit testing during coding

9. create a prototype board, probably using a prototype board

10 create a circuit board using software like Eagle, which then can be made to PCBs.
