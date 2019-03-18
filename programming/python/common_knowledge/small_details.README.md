Difference between "#!/usr/bin/python" and "#!/usr/bin/env python" in shell script
---------------------------------------------------------

#!/usr/bin/python is hardcoded to run /usr/bin/python 
while #!/usr/bin/env python is to run whatever python in the $PATH.

2nd case may be preferred because it runs well inside virtualenv.

Reference: https://stackoverflow.com/questions/5709616/whats-the-difference-between-these-two-python-shebangs


difference between float and decimal
--------------------------------------------

Float is like float in C.
If you do 0.1 + 0.1 + 0.1 - 0.3 in C, the result is not 0 but 5.55e-17.  

If we want exact computation, we need to use decimal in python, because it has the concept of significant numbers in the decimal class.

Reference: https://docs.python.org/2/library/decimal.html


Example:
```
Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17

>>> from decimal import Decimal

>>> Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
Decimal('0.0')

>>> Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
Decimal('2.775557561565156540423631668E-17')

```

from the example above, we need to know that it is when we convert a string to decimal, it maintains the original number;
but if we convert a float to decimal, it behaves still like a float.  
This has to be careful if we want to convert a float to decimal. one way is to convert it to string first and then to decimal (not sure if it is the best solution)


range()
-----------------------

By default range(10) means [0 to 9].

If we want to create a list from 2 to 9, then we do it this way: range(2, 10)
