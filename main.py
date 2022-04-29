import sys

import intcivil


def main():
    """Main entry point for the script."""

    # Run game code n times
    # 	Init Game
    # 	get average score
    game = intcivil.CivilGame()
    end = False
    while not end:
        num_cycles, end = game.step()

    # asd
    print(num_cycles)


if __name__ == '__main__':
    sys.exit(main())
