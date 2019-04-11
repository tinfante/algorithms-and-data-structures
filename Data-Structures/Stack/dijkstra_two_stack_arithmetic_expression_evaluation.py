# -*- coding: utf-8 -*-

import re


def evaluate(expression):
    """
    Evaluates a fully parenthesized arithmetic expression, recursively defined
    as either an integer, or an opening parenthesis followed by another
    expression, an operator (+, -, *, /), an expression and then a closing
    parenthesis.

    E.g.        3
                (4 / 2)
                (2 + (5 - 3))
                (1 + ((2 * 3) * (4 * 5)))

    Accepts a string with the expression as input. It doesn't check if the
    expression is valid. Outputs an integer or a float if the division
    operator was used.
    """
    tokens = re.findall(r'\d+|\(|\)|\+|-|\*|/', expression)
    operand_stack = []
    operator_stack = []
    operator_dict = {'+': lambda n1, n2: n2 + n1,
                     '-': lambda n1, n2: n2 - n1,
                     '*': lambda n1, n2: n2 * n1,
                     '/': lambda n1, n2: n2 / n1}
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            operator_stack.append(token)
        elif token == '(':
            continue
        elif token == ')':
            n1 = operand_stack.pop()
            n2 = operand_stack.pop()
            op = operator_stack.pop()
            operand_stack.append(operator_dict[op](n1, n2))
        else:  # must be digit
            operand_stack.append(int(token))
    return operand_stack[0]
