# iterable vs generator
# reference: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

# this is an iterable
print "iterable:"
iter1 = [ x*2 for x in range(10) ]
print iter1
for i in iter1:
	print i

# we can do it again and again, because iterable exists in memory before the program ends or they are actively freed
for j in iter1:
	print j

# now, let's try generator
# it looks the same as an iterable, except it uses a () instead of []
print "\ngenerator:"
g1 = ( x*2 for x in range(10) )
print g1
# this ends when there is no more value generated from the generator;
for i in g1:
	print i
	# print g1 # interestingly, g1's address does not change.. i don't know how the system keeps track of this. anyway not so important to know this.

# when we iterate thru a generator a second time, there won't be anything inside!!
print "\t2nd time:"
for j in g1:
	print j

# explanation:
# a generator generates the values on the fly!!
# the x*2 is a bit like "yield x*2" in the create_generator() function below..
#
# imagine that i write it in this way: for i in (x for x in range(10)), then obviously nothing is stored in the memory...
# with this way of imagination, then just assume that the code can only be pasted once; the next time it will be nothing..
# not sure if this is the right way of thinking...

# also note that the keyword "yield" is a bit like "return" but it returns a generator!
print "\ntry yield:"
def create_generator():
	r = range(5)
	for i in r:
		yield i*2

ret = create_generator()
print ret
# this ends when there is no more value generated from the generator
for i in ret:
	print i

print "\t2nd time:"
for j in ret:
	print j

# explain: the function create_generator is not run when we call it;
#	then, when we do "for i in ret", it starts to execute the function, until it hits yield and returns the first value;
#	and, when the next round starts, it continues function until it hits yield again, and so on...


print "\nfibo generator"
def fibo_generator():
	a=1;
	b=1;
	while True:
		yield a
		tmp = a
		a = a + b
		b = tmp

fibo = fibo_generator()
num=1
# this can run forever, because there is always a next number in the generator fibo
# in this case, it is stopped by an external counter "num"
for i in fibo:
	print i
	num = num + 1
	if num > 10:
		break

print "reset counter. another 10 numbers:"
num = 1
for i in fibo:
	print i
	num = num + 1
	if num > 10:
		break
