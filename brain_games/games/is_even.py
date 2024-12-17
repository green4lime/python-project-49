import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    num = random.randrange(50)
    is_even = "yes" if num % 2 == 0 else "no"
    return (num, is_even)
