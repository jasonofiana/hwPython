from time import time

def calculate_time(func):
    """
    Calculates the time a function takes to run

    This function takes a function as a paramter, runs the parameter function, and prints the runtime of the
    parameter function. Also returns the result of the parameter function

    Parameters
    ----------
    func : function
        the function to run

    returns
    -------
    func
         This function returns whatever the parameter function should return

    Examples
    --------
    lets say function greeter() has one line and it is print("hello")
    >>> calculate_time(greeter())
    hello
    Total time (whatever small value end - time would be)
    """
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Total time {(end-start)}')
        return result
    return wrapper

