from brain_games.welcome import welcome_user


def run_game(generate_question_answer, instruction):
    ROUNDS_COUNT = 3
    name = welcome_user()
    print(instruction)

    for round in range(ROUNDS_COUNT):
        (expression, result) = generate_question_answer()
        print(f"Question: {expression}")
        answer = input("Your answer:  ")
        if str(answer) == str(result):
            print("Correct!")
            if round == ROUNDS_COUNT - 1:
                print(f"Congratulations, {name}!")
                break
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            break
