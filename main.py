"""TDT4113_Assignment_4: Calculator"""

__author__ = 'Marianne Hernholm'
__project__ = 'TDT4113_Assignment_4'

# import numpy
# import container
# import function
# import ops
import calculator as calc


def main():
    """Generic main function to run program"""

    # Test that container-classes behave as expected
    # TEST QUEUE class
    # queue1 = container.Queue()
    # queue1.push('element a')
    # queue1.push('element b')
    # print(queue1.peek())
    # queue1.pop()
    # print(queue1.peek())
    # queue1.is_empty()
    # size = queue1.size()
    # print(size)

    # TEST STACK class
    # stack1 = container.Stack()
    # stack1.push('element a')
    # stack1.push('element b')
    # print(stack1.peek())
    # size = stack1.size()
    # print(size)
    # stack1.pop()
    # print(stack1.peek())

    # Test FUNCTION class
    # exponential_func = function.Function(numpy.exp)
    # sin_func = function.Function(numpy.sin)
    # print(exponential_func.execute(0))
    # print(sin_func.execute(0))

    # TEST OPERATOR class
    # add_op = ops.Operator(operator=numpy.add, strength=0)
    # mult_op = ops.Operator(operator=numpy.multiply, strength=1)
    # mult_try = mult_op.execute(element1=2, element2=6)
    # print(mult_try, '\n')
    # add_try = add_op.execute(2, mult_op.execute(element1=2, element2=6))
    # print(add_try, '\n')
    # mult_try2 = mult_op.execute(2, add_op.execute(element1=5, element2=7))
    # print(mult_try2)

    # TEST CALCULATOR class
    # calc1 = calculator.Calculator()
    # compute = calc1.functions['EXP'].execute(calc1.operators['ADD'].
    # execute(1, calc1.operators['MULTIPLY'].execute(2,3)))
    # print(compute)

    # TEST RPN IMPLEMENTATION method
    # calc_obj = calc.Calculator()    # Build calculator object
    # opq = calc_obj.output_queue     # Build an output queue
    # Start by filling output_queue with some values
    # opq.push(1)
    # opq.push(2)
    # opq.push(3)
    # opq.push(calc_obj.operators['MULTIPLY'])
    # opq.push(calc_obj.operators['ADD'])
    # opq.push(calc_obj.functions['EXP'])
    # print('Final calculation result: ', calc_obj.rpn_calculation())

    # TEST NNQ_TO_RPN IMPLEMENTATION method
    # calc_obj = calc.Calculator()    # Make calculator object
    # ipq = container.Queue()         # Build input_queue
    # TEST1
    # ipq.push(2)
    # ipq.push(calc_obj.operators['MULTIPLY'])
    # ipq.push(3)
    # ipq.push(calc_obj.operators['ADD'])
    # ipq.push(1)
    # TEST2
    # ipq.push(calc_obj.functions['EXP'])
    # ipq.push('(')
    # ipq.push(1)
    # ipq.push(calc_obj.operators['ADD'])
    # ipq.push(2)
    # ipq.push(calc_obj.operators['MULTIPLY'])
    # ipq.push(3)
    # ipq.push(')')
    # calc_obj.nnq_to_rpn(ipq)
    # result = calc_obj.rpn_calculation()
    # print('FINAL RESULT:',  result)

    # TEST TEXT_PARSER IMPLEMENTATION function
    # calc_obj = calc.Calculator()
    # s_ipq1 = calc_obj.text_parser('((15 DIVIDE (7 subtract (1 add 1)))
    # MULTIPLY 3) subtract (2 add (1 add 1))')
    # s_ipq2 = calc_obj.text_parser('2 multiply 5)')
    # s_ipq3 = calc_obj.text_parser('exp(1 add 2 multiply 3)')
    # test_parse = calc_obj.nnq_to_rpn(s_ipq3)
    # res = calc_obj.rpn_calculation()
    # print('FINAL RESULT TXT PARSER TEST CALCULATION: ', res)

    # TEST CALCULATE_EXPRESSION MASTER METHOD
    calc_obj = calc.Calculator()
    calc_obj.calculate_expression('exp (1 add 2 multiply 3)')
    # calc_obj.calculate_expression('(27 add 213) multiply 5')
    # calc_obj.calculate_expression('((27 DIVIDE (8 SUBTRACT(2 ADD 2))) DIVIDE 2) SUBTRACT (EXP (4 DIVIDE 2))')
    # calc_obj.calculate_expression('3 multiply sin(3) add cos(5)')

    return 0


RUN_MAIN = main()
