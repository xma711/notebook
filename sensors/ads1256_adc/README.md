from data sheet
-----------------

When using ADS1255/6 for single-ended measurements,
it is important to note that common input AINCOM does not
need to be tied to ground. For example, AINCOM can be
tied to a midpoint reference such as +2.5V or even AVDD.

when adc value is 0x000001, the corresponding voltage is 1 * (+2 * Vref)/(PGA (2^23-1)).  
When adc value is 0x7fffff, the voltage is (maximum) (+2 * Vref)/PGA.  
when adc value is 0xffffff (maximum adc value), the voltage is (the maximum negative value, ie the minimum absolute value of the negative voltage) 1 * (-2 * Vref)/(PGA (2^23-1)).  
when adc value is 0x800000 (mid point), the voltage is (most negative voltage) (-2 * Vref)/PGA  .
Just derive other voltages from these boundaries points.
