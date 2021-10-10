def tripler(func):
	"""
	Runs a function three times

	This function takes in a function  as a parameter and runs it three times

	parameters
	----------
	func : function
		the function to be run three times

	returns
	-------
	func
		the return of the function three times

	examples
	--------
	lets say function greeter() prints out "Hello"
	>>> tripler(greeter())
	Hello
	Hello	
	Hello
	"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + " \n" + func(*args, **kwargs) + " \n" + func(*args, **kwargs) 
    return wrapper

