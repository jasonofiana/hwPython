def calculator(number1, number2, operator):
	"""
	Calculates an equation
	
	This function takes in an operation in the form of the parameters, calculates it, and returns the output
	
	Parameters
	----------
	number1 : float
		the number on the left side of the operator
	number2 : float
		the number on the right side of the operator
	operator : string
	the operator to be used to calculation

    returns
    -------
    float
         depending on the operator, the  result from calculating with number1 and number2

    Examples
    --------
    >>> calculator(2, 7, '*')
    14
    >>> calculator(4, 3, '-')
    1
    """
	try:
		numb1 = float(number1)
		numb2 = float(number2)
		if operator  == "+":
			return numb1 + numb2
		elif operator ==  '-':
			return numb1 - numb2
		elif operator == '*':
			return numb1 * numb2
		elif operator == '/':
			if numb2 == 0:
				return 0
			return numb1 / numb2
		elif operator == '//':
			return numb1 // numb2
		elif operator == '**':
			return numb1 ** numb2
		else:
			return False
	except ValueError:
			return False
def parse_input():
	"""
	Parses and passes user input into function calculator

	This function prompts the user for an equation, parses the string into an array, and passes the content
	of the array into the calculaotr function to be calculated. The output of the calculator function is printed

	parameters
	----------

	Returns
	-------
	Doesn't return anything, but prints out the return of the calculaotr function

	Examples
	--------
	>>> parse_input
	Enter equation: (user input)10 + 11
	21.0
	>>> parse_input
	Enter equation: (user input)12 * 4.2
	50.400000000000006
	"""
	try:
		inp = input("Enter equation: ")
		arr = inp.split()
		print(calculator(arr[0], arr[2], arr[1]))
	except:
		pass
parse_input()
