import sys

import intchef


def run_cooking_session(agent, recipe):
    """Runs a full cooking session

    Returns:
            int: total time elapsed for cooking
    """
    session = intchef.CookingSession(agent, recipe)
    score = session.main()
    return score


def main():
    """Main entry point for the script."""

    agent_list = intchef.AgentList()
    agent = agent_list.ACTION_AGENT

    recipe_book = intchef.RecipeBook()
    recipe = recipe_book.TOAST

    # Run game code n times
    # Init Game
    score = run_cooking_session(agent, recipe)
    print("Time taken:", score)

    # print(ALL_ACTIONS)
    # 	get average score
    print()


if __name__ == '__main__':
    print()
    sys.exit(main())
