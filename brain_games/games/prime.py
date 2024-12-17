from random import randrange as rd

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    question = rd(300)
    result = "yes" if is_prime(question) else "no"
    return (question, result)


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
