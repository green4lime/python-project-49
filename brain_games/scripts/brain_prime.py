#!/usr/bin/env python3
from brain_games.games.prime import generate_question_answer, instruction
from brain_games.run_game import run_game


def main():
    run_game(generate_question_answer, instruction)


if __name__ == "__main__":
    main()
