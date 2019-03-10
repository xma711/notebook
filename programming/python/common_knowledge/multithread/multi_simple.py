from time import sleep
import threading

lock = threading.Lock()

def foo(arg, bar):  
  lock.acquire()
  try:
    for i in range(arg):
      print "{}: running".format(bar)
      sleep(1)
    print 'hello {0}'.format(bar)
  finally:
    lock.release()
  return 'foo-' + bar

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)

async_result1 = pool.apply_async(foo, (5, 'hello')) # tuple of args for foo

async_result2 = pool.apply_async(foo, (10, 'world')) # tuple of args for foo

# do some other stuff in the main process

print "test1"

# ready() is not blocking
#for i in range(10):
#	sleep(1)
#	print "async_result1.ready() = {}".format(async_result1.ready())

# this get() seem is a blocking function.
# it will wait the respective thead to finish and then proceed
ret1 = async_result1.get()  # get the return value from your function.
print ("return vals = {}".format( (async_result1.get(), async_result2.get())))

print "test2"

