def multiply_list(list):
    """
    Multiply the list
    
    this function multiplies the contents in the list if they are all values that can be multiplied.
    
    Parameters
    ----------
    list : list
        list to be multiplied

    Returns
    -------
    int
       product of all the values in the lsit
    
    examples
    --------
    >>> multiply_list([1, 2, 3, 4])
    24
    >>> multiply_list([ 2, 5, 2])
    20
    """
    try:
        sum = int(list[0])
        for x in list[1:]:
           sum *= int(x)
        return sum
    except ValueError:
        return False


