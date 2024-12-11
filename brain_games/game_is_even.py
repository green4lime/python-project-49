import random


def game_is_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(4):
        if i == 3:
            print(f"Congratulations, {name}!")
            break
        question = random.randrange(50)
        if question % 2 == 1:
            is_even: str = "no"
        else:
            is_even: str = "yes"
        answer = input(f"Question: {question}\nYour answer: ")
        if is_even == answer:
            print("Correct!")
            continue
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {is_even}.
                    Let's try again, {name}""")
            break
