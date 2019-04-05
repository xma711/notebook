Modulation
--------------

Modulate -> means change.

Modulate a carrier wave -> change a carrier wave.

Things that can be changed/modulated: phase, amplitude, frequency or a combination of these.

Simple phase shift-keying (PSK) modulates the phase of the carrier. 
	- e.g. BPSK shifts the carrier wave 180 degrees when info change between 0 and 1. -> receiver has to detect if there is a 180 degrees shift in the wave, and each change, a symbol, represent a 1 or 0 in this case.

QPSK
---------------

Stands for Quadrature Phase Shift Keying.

Why stop at 180 degree shift? QPSK extends the idea by modulating the carrier wave by 4 distinct values (e.g. 45, 135, 225, 315) then each change in the wave (each symbol) then represents a 2 bits.
	- the intuition is that the receiver has a "look-up table", and receiver maps each symbol to the bit representation.

Of course there is a limit due to noise in the signal. otherwise it can just go to infinity.

Another limitation is that the value added by each newly added pattern decreases exponentially, as the total pattern number can be used only in 2 to power of something.  
To represent 1 bit we need 1 pattern, to represent 2 bits we need 4 patterns (4 = 2^2), to represent 4 bits we need 16 patterns, to represent 6 bits we need 64 patterns and so on.   

QAM
---------------------

Stands for Quadrature amplitude modulation.

It mixes phase shift together with amplitude change, giving more patterns (choices of symbols.)
	- e.g. QAM16 has 16 patterns, each representing a 4 bit 
	- e.g. QAM64 has 64 patterns, each representing a 6 bit. This can be used only when the channel condition is good

Baud rate
-----------------------

Baud rate is the number of times we modulate a carrier per second.

When a carrier wave is modulated at a baud rate B, it will occupy a spectrum range of B centered around the carrier frequency.

Maximum date rate = baud rate x number of bits per symbol
	- e.g. 20Mhz baud rate with QAM16 give 200MHz x 4 bits = 80Mbps
