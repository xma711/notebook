Design by contract
------------------------

Reference: https://en.wikipedia.org/wiki/Design_by_contract

DbC prescribes that software designers should define formal, 
precise and verifiable interface specifications for software components, 
which extend the ordinary definition of abstract data types 
with preconditions, postconditions and invariants.

These specifications are referred to as "contracts", 
in accordance with a conceptual metaphor with 
the conditions and obligations of business contracts.


My own example: double_1_to_10.py
-------------------------------------
This is my own understanding.
May not be correct.

The function inside double_1_to_10.py makes sure 
it only accepts int and number 1 to 10.

Run this test by:
python3 -m unittest double_unittest (don't put .py at the end)

Question: should we also add checking before return?
Making sure the returned value won't be less than 2 and more than 20?
Maybe yes.
