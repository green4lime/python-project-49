import random


def game_is_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = random.randrange(50)
    if num % 2 == 1:
        is_even: str = "no"
    else:
        is_even: str = "yes"
    return (num, is_even, description)
