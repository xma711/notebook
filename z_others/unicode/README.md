Unicode
------------------

Reference: http://stackoverflow.com/questions/2241348/what-is-unicode-utf-8-utf-16

previously, there was only ASCII, which is mostly for english language.  
However, today we need an encoding scheme to represent characters in all languages. 
Thus came unicode.
It assigns every character a unique number called a code point.

The first 256 code points are identical to ASCII.  
Majority of the commonly used characters are representable by only two bytes, in a region called the Basic Multilingual Plane (BMP).

Utf-8:  
	- 1 byte: standard ASCII  
	- 2 bytes: Arabic, Hebrew, most European scripts  
	- 3 bytes: BMP  
	- 4 bytes: all unicode characters


utf-16:  
	- 2 bytes: BMP  
	- 4 bytes: all unicode characters


exmaple
----------------------

Using nodejs,  
buf = new Buffer("hello world!", 'utf16le');
buf2 = new Buffer("hello world!", 'utf8');

buf.toString() makes sense only when the option is set to 'utf16le': buf.toString('utf16le');  
buf.toString('utf8') will lead to some random string output.

Similarly, only buf2.toString('utf8') will give correct output.


Chinese character encoding
---------------------------

Unicode is one way.

But mainland chinese use GuoBiao as the encoding scheme and 
TW, HK and Macau use Big5.  
For more details, check wikipedia page https://en.wikipedia.org/wiki/Chinese_character_encoding
