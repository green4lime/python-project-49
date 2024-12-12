#!/usr/bin/env python3
from brain_games.welcome import welcome_user
from brain_games.run_game import run_game
from brain_games.games.gcd import game_gcd


def main():
    name = welcome_user()
    game = game_gcd
    run_game(game, name)


if __name__ == '__main__':
    main()
