Representation
------------------

X + iy

r * e^(i * angle)

r * (sin(angle) + i cos(angle))

btw, electrical engineers like to use j instead of i


multiply a real number
-------------------------

When a complex number multiplies a real number, the effect on the real part and img part are independent. 
E.g. (x +iy)*2 = 2x+i2y, or (cos(x) + isin(x))*2 = 2cos(x) + i2sin(x)

this means we can convert a sin(x) or cos(x) to a complex number, and do all the multiplication with the complex number, and then extract the real part or the img part for the results.

E.g.to calculate sin(2x).  
Sin(2x) = img(e^(i2x)), where  
e^(i2x) = e^(ix) * e^(ix) = (cos(x) + isin(x))^2 = cos(x)^2 + i2cos(x)sin(x) - sin(x)^2  
therefore, sin(2x) = img(e^(2ix)) = 2cos(x)sin(x)

what about dsin(x)/dx?  
As de^(ix)/dx = ie^(ix) = i (cos(x) + isin(x)) = icos(x) - sin(x),  
dsin(x)/dx = img( de^(ix)/dx ) = cos(x)

then what about integrate_from_0_to_pi sin(x) dx?  
The direct answer is 2.  
If using complex number, integrate_from_0_to_pi(e^(ix))dx = (e(ix)/i) | (0, pi) = 2j.  
Therefore, integrate_from_0_to_pi sin(x) dx = img(2j) = 2.

Multiply an imaginary number
----------------------------

The real part becomes the img part while the img part becomes a real part.

In the e^() form, it is a rotation of 90* with some scaling.


Multiply a complex number
---------------------------

It involves rotation of an angle and scaling on the magnitude.

E.g. r1 e^(xi) * r2 e^(yi) = r1*r2 e^((x+y)i)

phasor notation
-------------------------

Phasor notation is the process of constructing a single complex number that has the amplitude and the phase angle of the given sinusoidal waveform.

It transforms the sinusoidal function A(t) = Am sin(wt +- phi) from time domain into the frequency domain.

V(t) = Vm sin(wt + phi) = Vm * img (cos(wt+phi) + j sin(wt+phi)) = Vm * img{ e^((wt+phi)j) } = Vm * img{ e^(wt j) * e^(phi j) } =  
sqrt(2) * img{ ( Vm/sqrt(2) * e^(phi j) ) * e^(wt j) } = sqrt(2) * img{ Vrms * e^(wt j) }  
(Vrms is the more important part in this whole thing.)  

Then with a 'leap of faith', V(t) can be transformed to Vrms = Vm/sqrt(2) * e^(phi j) = Vm/sqrt(2) /_phi ( where e^(phi j) = /_phi )    
e.g. V(t) = 20 sin(wt + 30) ==> Vrms = 20/sqrt(2) /_30 = 14.14 /_30 

note that in this  case, 'wt' is hidden (which is the time domain i guess).

Why hide wt?  
Reference: http://www.dummies.com/how-to/content/how-to-use-phasors-for-circuit-analysis.html 

because the radian frequency w remains the same in a linear circuit, a phasor just needs the amplitude Vm and the phase phi to get into the polar form.


Circuit analysis (AC circuit)
----------------------------

"For circuit analysis, think of the real part as tying in with resistors that get rid of energy as heat and the imaginary part as relating to stored energy, 
like the kind found in inductors and capacitors."

Transform voltage source, inductor, capacitor, resistor to complex number (or phasors), and do the calculation as if it is a dc circuit.

Resistor: just a real number

inductor: v(t) = L * di(t)/dt, using complex numbers: V*e^(jwt) = L * d(Ie^(jwt))/dt = L (jw)I e^(jwt) ==> V = jwL * I

... to be continued...
