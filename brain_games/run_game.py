
def run_game(game, name):
    rounds_count = 3
    print(game()[2])

    for round in range(rounds_count):
        (expression, result, description) = game()
        print(f"Question: {expression}")
        answer = input("Your answer:  ")
        if str(answer) == str(result):
            print("Correct!")
            if round == rounds_count - 1:
                print(f"Congratulations, {name}")
                break
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.")
            print(f"Let's try again, {name}!")
            break
