
def run_game(game, name):
    ROUNDS_COUNT = 3
    print(game()[2])

    for round in range(ROUNDS_COUNT):
        (expression, result, _) = game()
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
