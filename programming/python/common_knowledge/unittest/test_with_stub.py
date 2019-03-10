#!/usr/bin/python2

# reference: http://stackoverflow.com/questions/3909942/how-to-stub-python-methods-without-mock

### try unit tests with stub (not mock, because mock is about asserting something, stub is to make the function work)

# the class for test
class HELLOWORLD ():
	def getData(self):
		print "Production getData() called."
		return "Production codes that gets data from server"

	def getDataLength(self):
		return len( self.getData() )

	def getDataLen2(self):
		return len( self.getData() )

# now test the class HELLOWORLD
import unittest

class TestHELLOWORLDclass (unittest.TestCase):

	# first test: using stub
	def testGetDataLength(self):

		print "\nin testGetDataLength()"
		# create a stub for getData() method
		def mockGetData(self):
			print "Stubbed getData called."
			#logger.info("BB")
			# this  string length is 20
			return "stub_data_length_20."

		# we need to keep this original method,
		# because at the end we need to change the method back to this original one
		originalGetData = HELLOWORLD.getData ### can use the internal method directly???

		# testing the method GetDataLength()
		try:
			# replace the method by the mockGetData.. 
			# this doesn't seem to be global; in the next test the helloworld method is still the original one
			# so the methods inside a class are public??
			HELLOWORLD.getData = mockGetData
			
			helloworld_obj = HELLOWORLD()

			self.assertEqual( 20, helloworld_obj.getDataLength() ) # this test will pass
		finally:
			# change the method in the class back to the original GetData() method
			HELLOWORLD.getData = originalGetData 

	# second test: not using stub --> which is not the right way to do btw
	def testGetDataLen2(self):
		print "\nin testGetDataLen2()"

		# no need try_except if i want the unittest framework to capture the failed test
		helloworld_obj = HELLOWORLD()
		self.assertEqual( 20, helloworld_obj.getDataLength() )	# this test will fail because it will use the original getData() function
	

if __name__ == "__main__":
	unittest.main()
