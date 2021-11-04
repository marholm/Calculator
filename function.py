"""Implements Function class"""
import numbers


class Function:
    """Auxiliary classes for the functions the calculator will support"""
    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """Returns formatted string of function we are working with"""
        # Check type
        if not isinstance(element, numbers.Number):
            raise TypeError('The element must be a number')
        result = self.func(element)

        # Report
        if debug is True:
            print('Function: ' + self.func.__name__ + '({:f}) = {:f}'.format(element, result))

        return result
