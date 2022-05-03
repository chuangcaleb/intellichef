import sys

import intchef


def run_cooking_session():
    """Runs a full cooking session

    Returns:
            int: total time elapsed for cooking
    """
    session = intchef.CookingSession()
    score = session.run()
    return score


def main():
    """Main entry point for the script."""

    recipe_book = intchef.RecipeBook()
    recipe_toast = recipe_book.TOAST
    recipe_toast.print_details()

    # Run game code n times
    # Init Game
    # score = run_cooking_session()

    # print(score)
    # 	get average score


if __name__ == '__main__':
    sys.exit(main())
