import sys

import intcivil


def main():
    """Main entry point for the script."""

    # Run game code n times
    # 	Init Game
    # 	get average score
    game = intcivil.CivilGame(max_cycles=80)
    end = False
    while not end:
        end = game.step()

    print(game.num_cycles)


if __name__ == '__main__':
    sys.exit(main())
