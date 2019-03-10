explain arduino bootloader
----------------------------

reference: https://www.arduino.cc/en/hacking/programmer

"If you have an external programmer (e.g. an AVR-ISP, STK500, or parallel programmer), 
you can burn sketches to the Arduino board without using the bootloader. 
This allows you to use the full program space (flash) of the chip on the Arduino board. 
So with an ATmega168, you'll get 16 KB instead of 14 (on an ATmega8 you'll get 8 KB instead of 7). 
It also avoids the bootloader delay when you power or reset your board.

This can be easily done in this way:
Tools->Boards->Your Board
Tools->Programmer->Your Programmer
Sketch->Upload Using a Programmer
"

This means this programmer is a hardware device that allows a computer to burn skedule to the arduino using the full flash.  
Also, the programmer is needed when we try to upload a bootloader to the arduino.

as explained by reference https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader/all,
"The bootloader is basically a .hex file that runs when you turn on the board. 
It is very similar to the BIOS that runs on your PC. 
It does two things. 
First, it looks around to see if the computer is trying to program it. 
If it is, it grabs the program from the computer and 
uploads it into the ICs memory (in a specific location so as not to overwrite the bootloader). 
That is why when you try to upload code, the Arduino IDE resets the chip. 
This basically turns the IC off and back on again so the bootloader can start running again. 
If the computer isn’t trying to upload code, 
it tells the chip to run the code that’s already stored in memory. 
Once it locates and runs your program, 
the Arduino continuously loops through the program and does so as long as the board has power."



install bootloader to an arduino
------------------------

reference: https://learn.sparkfun.com/tutorials/installing-an-arduino-bootloader/all

the programmer actually uses SPI interface to upload the file to the flash at a particular location.
