#!/usr/bin/env python3
from brain_games.games.is_even import generate_question_answer, INSTRUCTION
from brain_games.run_game import run_game


def main():
    run_game(generate_question_answer, INSTRUCTION)


if __name__ == "__main__":
    main()
