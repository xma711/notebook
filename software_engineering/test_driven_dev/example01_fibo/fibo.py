# the main class
class FIBO():
	def get_fibo_list(self, num_items_to_return):

		# this method returns a list of fibonacci numbers with total number = num_items_to_return
		if (num_items_to_return <= 0):
			raise InputError("Input number cannot be smaller than 1.");

		# the first 2 fibo numbers
		start1 = 1;
		start2 = 1;

		if num_items_to_return == 1:
			return [start1];
		elif num_items_to_return == 2:
			return [start1, start2];
		else:
			# handle the case that the num_items required is more than 2
			list_num = [start1, start2];
			num_iter = num_items_to_return - 2;
			assert (num_iter > 0);	

			# new number is the sum of last 2 numbers,
			# then add the new number to the list
			i = 0;
			while (i < num_iter):
				len_list = len(list_num)
				assert(len_list >= 2);
				new_num = list_num[len_list - 1] + list_num[len_list - 2];
				list_num.append(new_num)
				i += 1
			return list_num;

# exception to be raised/thrown
class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg
