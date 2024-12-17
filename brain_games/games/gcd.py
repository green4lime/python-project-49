import random
from math import gcd

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    a = random.randrange(50)
    b = random.randrange(50)
    expression = (f"{a} {b}")
    result = gcd(a, b)
    return (expression, result)
