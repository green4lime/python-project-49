#!/usr/bin/env python3
from brain_games.welcome import welcome_user
from brain_games.game_is_even import game_is_even


def main():
    name = welcome_user()
    game_is_even(name)


if __name__ == '__main__':
    main()
