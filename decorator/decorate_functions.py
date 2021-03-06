
def stringify(function):
	""" 
	:param function: any function 
	:rtype: int
	:return: modified function wrapper

	method stringify takes a function as an argument and changes it's return type to string.
	"""
    def wrapper(*args):
    	"""
    	method, that changes return type of function given as stringify argument 
    	to string.
		:param *args: functions
		:return type: return value of function translated to string
    	"""
        

   
@stringify
def add_numbers(first_number, second_number):
	"""
	method, that returns the sum of two numbers
	:param first_number second_number: 2 numbers(integer or float), accordingly
	:return type: integer
	"""

@stringify
def multiply_numbers(first_number, second_number):
	"""
	method, that returns the multiplication of two numbers
	:param first_number second_number: 2 numbers(integer or float), accordingly
	:return type: integer
	"""
