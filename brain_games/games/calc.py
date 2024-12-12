import random


def calculate(a, b, operation) -> int:
    if operation == 0:
        result = sum(a, b)
    elif operation == 1:
        result = different(a, b)
    else:
        result = multiply(a, b)
    return result


def sum(a, b):
    return a + b


def different(a, b):
    return a - b


def multiply(a, b):
    return a * b


def game_calc():
    description = "What is the result of the expression?"
    first_num = random.randrange(10)
    second_num = random.randrange(10)
    operator = random.randrange(3)
    operator_char = (' + ', ' - ', ' * ')[operator]
    expression = (f"{first_num}{operator_char}{second_num}")
    result = calculate(first_num, second_num, operator)
    return (expression, result, description)
