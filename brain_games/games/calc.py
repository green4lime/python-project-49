import random

INSTRUCTION = "What is the result of the expression?"


def generate_question_answer():
    operators_list = ["+", "-", "*"]

    a = random.randrange(10)
    b = random.randrange(10)
    operator = random.choice(operators_list)

    expression = f"{a} {operator} {b}"
    result = calculate(a, b, operator)
    return (expression, result)


def calculate(a, b, operation) -> int:
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    raise Exception(f"unknown operation {operation}")
