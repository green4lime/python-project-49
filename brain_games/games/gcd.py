import random
from math import gcd


def game_gcd():
    instruction = 'Find the greatest common divisor of given numbers.'
    f_num = random.randrange(50)
    s_num = random.randrange(50)
    exception = (f"{f_num} {s_num}")
    result = gcd(f_num, s_num)
    return (exception, result, instruction)
