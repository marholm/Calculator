"""Main calculator class"""
import numpy
import function as f
import ops as o
import container as c
import re


class Calculator:
    """Class for implementing main calculator functionality"""

    def __init__(self):
        # Define funcs supported by linking them to numpy functions
        self.functions = {'EXP': f.Function(numpy.exp), 'LOG': f.Function(numpy.log),
                          'SIN': f.Function(numpy.sin), 'COS': f.Function(numpy.sin),
                          'SQRT': f.Function(numpy.sqrt)}

        # Define ops supported by linking to numpy funcs
        self.operators = {'ADD': o.Operator(numpy.add, 0), 'MULTIPLY': o.Operator(numpy.multiply, 1),
                          'DIVIDE': o.Operator(numpy.divide, 1), 'SUBTRACT': o.Operator(numpy.subtract, 0)}

        # Define output-queue; gets filled with RPN
        self.output_queue = c.Queue()

    def rpn_calculation(self):
        """Implement RPN calculation"""
        # We need a stack for intermediate storage (when performing calculation)
        calculation_stack = c.Stack()

        # Iterate through queue until its empty
        while not self.output_queue.is_empty():
            # Pop each item from the queue
            item = self.output_queue.pop()

            # If item is a number -> push it on the stack
            if isinstance(item, (float, int)):
                calculation_stack.push(item)

            # If item is a function -> pop an element from the stack
            # and evaluate the function with that element (which will be a number)
            # Push the result on the  stack
            elif isinstance(item, f.Function):
                element = calculation_stack.pop()  # pop element from stack
                result = item.execute(element=element)  # item: a function, element: a number
                calculation_stack.push(result)  # push result to stack

            # If item is an operator -> pop two elements from stack
            # Perform operation with the two elements
            # Push the result back on the stack
            # PS! Watch the order of items
            elif isinstance(item, o.Operator):
                # Pop two elements from the stack
                element1 = calculation_stack.pop()
                element2 = calculation_stack.pop()
                # perform operation on them
                result = item.execute(element1=element1, element2=element2)
                # Push result back on stack
                calculation_stack.push(result)

        # Return last element on stack - the final result of the calculations
        return calculation_stack.peek()

    def nnq_to_rpn(self, input_queue):
        """Converts NNQ-ip_queue(txt) to RPN-op_queue"""
        operator_stack = c.Stack()  # temporary storage for the operators/ functions/ parenthesis from the ipq

        # 1. Review each item in input queue
        while not input_queue.is_empty():
            elem = input_queue.pop()

            # a) elem==number -> push directly on output queue
            if isinstance(elem, (float, int)):
                # print('elem num: ', elem)
                self.output_queue.push(elem)

            # b) elem==func -> push on operator stack
            elif isinstance(elem, f.Function):
                # print('elem func: ', elem)
                operator_stack.push(elem)

            # c) elem==left_parenthesis -> push on operator stack
            elif elem == '(':
                # print('elem (: ', elem)
                operator_stack.push(elem)

            # d) elem==right_parenthesis -> *, **, ***
            elif elem == ')':
                # print('elem ): ', elem)
                # *) pop items from operator_stack one by one
                # and push them to output queue until top element on operator_stack
                # is a left parenthesis '('
                while operator_stack.peek() != '(':
                    # Never right parentheses ')' on the operator_stack
                    # Never parentheses at all on the output_queue
                    if isinstance(operator_stack.peek(), (f.Function, o.Operator)):
                        # ***) If top of operator_stack is a function
                        # pop function from operator stack onto output queue
                        item = operator_stack.pop()
                        self.output_queue.push(item)
                # **) If top of operator_stack is a left parenthesis
                # pop parenthesis and discard it
                operator_stack.pop()

            # e) elem==operator -> sort it into correct location
            elif isinstance(elem, o.Operator):
                # print('elem oper: ', elem)
                # Move items one by one from operator_stack to output_queue until either:
                # *) operator_stack is empty
                # **) top elem on operator stack is a weaker operator
                # ***) top elem on operator stack is left parenthesis
                while not operator_stack.is_empty() and isinstance(operator_stack.peek(), (f.Function, o.Operator)) and operator_stack.peek().get_strength() >= elem.get_strength():
                    # Move items one by one from operator stack to output queue
                    # print('IN WHILE FOR OPERATOR')
                    try:
                        item = operator_stack.pop()
                        self.output_queue.push(item)
                    except:
                        print('Operator stack is empty')
                        break

                # After moving, push elem on operator stack
                operator_stack.push(elem)

        # 2. Pop each item on operator stack and push it on output queue
        while not operator_stack.is_empty():
            item = operator_stack.pop()
            self.output_queue.push(item)

        # We return the now accurate RPN queue
        return self.output_queue

    def text_parser(self, txt):
        """Method receives a txt string and produces element list for shunting
        -yard algorithm"""

        # Remove whitespace and make txt uppercase
        txt = txt.replace(' ', '').upper()
        str_input_queue = c.Queue()  # Build list of all elements contained in the string input text

        # re.search lets us look for several substrings simultaneously
        target_functions = "|".join(["^" + func for func in self.functions.keys()])
        target_operators = "|".join(["^" + op for op in self.operators.keys()])

        # When using search - if there is no match -> value None is returned
        # Iterate text
        while len(txt) != 0:

            # numbers
            # re.search() lets us look for several substrings simultaneously
            # num_match = re.search("^[-0123456789.]+", txt)
            if re.search("^[-0123456789.]+", txt) is not None:
                print('NUM FOUND')
                match = re.search("^[-0123456789.]+", txt)
                print('num match found: ', match)
                # re.group() returns the part of the string where there was a match
                # set group(0) so it doesnt default to None if no match is found
                # match.group(0) is the text that matches search
                str_input_queue.push(float(match.group(0)))  # Type should be float

            # functions
            # func_match = re.search(target_functions, txt)

            elif re.search(target_functions, txt) is not None:
                print('FUNC FOUND')
                match = re.search(target_functions, txt)
                print('func match found: ', match)
                str_input_queue.push(self.functions[match.group(0)])

            # operators
            # op_match = re.search(target_operators, txt)
            elif re.search(target_operators, txt) is not None:
                print('OPERATOR FOUND')
                match = re.search(target_operators, txt)
                print('op match found: ', match)
                str_input_queue.push(self.operators[match.group(0)])

            # parentheses
            elif re.search('\(', txt) is not None:
                print('LEFT PARENTHESES FOUND')
                match = re.search('\(', txt)
                print('left parentheses match found: ', match)
                str_input_queue.push('(')

            elif re.search('\)', txt) is not None:
                print('RIGHT PARENTHESES FOUND')
                match = re.search('\)', txt)
                print('right parentheses match found: ', match)
                str_input_queue.push(')')
            else:
                print('Unrecognizable input in txt string')

            # Slicer txt med slice[start_fra_der_match_endte: ut_lista]:
            # Need this to avoid infinite loop
            # match.end(0) gives end of match, so where we wish to continue from
            txt = txt[match.end(0):]

        return str_input_queue

    def calculate_expression(self, txt):
        """Master routine, puts program together"""
        self.text_parser(txt)
        self.nnq_to_rpn(self.text_parser(txt))
        res = self.rpn_calculation()
        print('Result: ', res)
