unit tests
-----------------

reference: https://docs.python.org/2/library/unittest.html

The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:

(I can also run the files directly, just like any other python files.)

python -m unittest test_module1 test_module2  
python -m unittest test_module.TestClass  
python -m unittest test_module.TestClass.test_method

e.g. python -m unittest hello_world_unittest  (cannot have ./ in front!!! and cannot have .py at the end!!!)

You can run tests with more detail (higher verbosity) by passing in the -v flag:

python -m unittest -v test_module


xml outputs
----------------

to get xml outputs (for jenkins e.g.), follow this guide http://stackoverflow.com/questions/11241781/python-unittests-in-jenkins  
anyway "py.test --junitxml results.xml tests.py" OR "nosetests --with-xunit" should work.  


use stub
------------

reference: http://stackoverflow.com/questions/3909942/how-to-stub-python-methods-without-mock

see test_with_stub.py.

a class's method can be easily replaced by a stub in a test.
