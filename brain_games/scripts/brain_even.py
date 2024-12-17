#!/usr/bin/env python3
from brain_games.games.is_even import game_is_even
from brain_games.run_game import run_game
from brain_games.welcome import welcome_user


def main():
    name = welcome_user()
    game = game_is_even
    run_game(game, name)


if __name__ == '__main__':
    main()
