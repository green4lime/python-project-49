from random import randrange as rd


def game_progression():
    instruction = 'What number is missing in the progression?'
    start, step, length = rd(30), rd(1, 5), 10
    # progression = list(range(start, start + step * length, step))
    position = rd(length - 1)
    progression = [str(elem) for elem
                   in range(start, start + step * length, step)]
    result = progression[position]
    progression[position] = '..'
    question = ' '.join(progression)
    return (question, result, instruction)
