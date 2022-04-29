import sys

from int_civil.game import CivilGame


def main():
    """Main entry point for the script."""

    # Run game code n times
    # 	Init Game
    # 	get average score
    game = CivilGame()
    end = False
    while not end:
        num_cycles, end = game.step()

    # asd
    print(num_cycles)


if __name__ == '__main__':
    sys.exit(main())
