"""Implements Operator class"""
import numbers


class Operator:
    """Auxiliary class for the operators the calculator will support (add, sub, mult, div)"""
    def __init__(self, operator, strength):
        self.operator = operator
        self.strength = strength

    # Need access to an operators strength in the parser-function
    def get_strength(self):
        return self.strength

    def execute(self, element1, element2, debug=True):
        """Returns formatted string for operator we are working with"""
        # Checks type
        if not (isinstance(element1, numbers.Number) and isinstance(element2, numbers.Number)):
            raise TypeError('The elements must be numbers')
        result = self.operator(element1, element2)

        # Report
        if debug is True:
            print('Operator: ' + self.operator.__name__ +
                  '({v1}, {v2}) = {res}'.format(v1=element1, v2=element2, res=result))

        return result
