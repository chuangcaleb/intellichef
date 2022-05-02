import sys

import intchef


def play_game():
    """Plays a CivilGame

    Returns:
            CivilGame: a finished game
    """
    game = intchef.CivilGame(max_cycles=80)
    end = False
    while not end:
        end = game.step()
    return game


def main():
    """Main entry point for the script."""

    # Run game code n times
    # Init Game
    game = play_game()

    # 	get average score
    print(game.num_cycles)


if __name__ == '__main__':
    sys.exit(main())
