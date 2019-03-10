endianness
-----------------------

endianness refers to the order of the bytes in computer memory,
or the order of byte transmission over a digital link.

with big-endian, the most significant byte of a word is stored at a particular memory address 
and the subsequent bytes are stored in the following higher memeory addresses, 
the least significant byte thus being stored at the highese memory address.

little-endian format reservers the order and stores the least significant byte at the lower memory address 
with the most significant byte being stored at the highest memory address.

note that endianness is NOT about the order of bits inside a byte!!!

also big-endian format is the most common format in data networking.  
big-endian order is also referred to as network byte order.

little-endian storage is popular for microprocessors, in part due to significant influence on microprocessor designs by Intel.


example
--------------

take nodejs buffer as example.

if buf = new Buffer(2),  
and buf[0] = 0, buf[1] = 1.

using big endian, buf.readInt16BE(0) will give 0*256 + 1*1 = 1;  
in this case, the byte at the lower position buf[0] represent the bigger 8 bits.

on the other hand, when using little endian, buf.readInt16LE(0) will give 1*256 + 0 = 256.

