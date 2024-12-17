from random import randrange as rd

INSTRUCTION = "What number is missing in the progression?"


def generate_question_answer():
    start, step, length = rd(30), rd(1, 5), 10
    position = rd(length - 1)
    progression = [
        str(elem) for elem in range(start, start + step * length, step)
    ]
    result = progression[position]
    progression[position] = ".."
    question = " ".join(progression)
    return (question, result)
