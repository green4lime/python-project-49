import random


def game_is_even():
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = random.randrange(50)
    is_even = "yes" if num % 2 == 0 else "no"
    return (num, is_even, instruction)
