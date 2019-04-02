Endianness
-----------------------

Endianness refers to the order of the bytes in computer memory,
or the order of byte transmission over a digital link.

With big-endian, the most significant byte of a word is stored at a particular memory address 
and the subsequent bytes are stored in the following higher memory addresses, 
the least significant byte thus being stored at the highest memory address.

Little-endian format reserves the order and stores the least significant byte at the lower memory address 
with the most significant byte being stored at the highest memory address.

Note that endianness is NOT about the order of bits inside a byte!!!

Also big-endian format is the most common format in data networking.  
Big-endian order is also referred to as network byte order.

Little-endian storage is popular for microprocessors, in part due to significant influence on microprocessor designs by Intel.


Example
--------------

Take nodejs buffer as example.

If buf = new Buffer(2),  
and buf[0] = 0, buf[1] = 1.

Using big endian, buf.readInt16BE(0) will give 0*256 + 1*1 = 1;  
in this case, the byte at the lower position buf[0] represent the bigger 8 bits.

On the other hand, when using little endian, buf.readInt16LE(0) will give 1*256 + 0 = 256.

