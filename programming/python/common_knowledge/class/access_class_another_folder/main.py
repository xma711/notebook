# import hello_world.hello_world.HelloWorld as HelloWorld # this line has an error:  ImportError: No module named HelloWorld
# this is a stupid error; it has nothing to do with importing class from another folder..
# solution: from hello_world.hello_world import HelloWorld !! (as shown below)

import hello_world.hello_world as hw # this line is okay

h = hw.HelloWorld()
h.print_hello()

# this is the right way to import class from a file
from hello_world.hello_world import HelloWorld as HW
hh = HW()
hh.print_hello()


import deeper.hi.hi as hi
h2 = hi.Hi()
h2.print_hi()
