from collections import Counter
import statistics
import sys
from colours import Colour, colour

import intchef


def run_cooking_session(agent, recipe, timeout):
    """Runs a full cooking session

    Returns:
            int: total time elapsed for cooking
    """

    session = intchef.CookingSession(agent, recipe, timeout)
    score, debug_msg, opened_nodes = session.main()

    if debug_msg:
        print(colour(Colour.RED, f"Failed: {debug_msg}\n"))

    print(f"Agent: {agent}")
    print(f"Recipe: {recipe}")
    print(f"Time taken: {score}")
    print(f"Nodes opened: {opened_nodes}")

    return score, debug_msg


def run_n_sessions(agent, recipe, timeout, n_iter: int):

    all_scores = []
    debug_list = []

    for _ in range(1, n_iter):
        score, debug_msg = \
            run_cooking_session(agent, recipe, timeout)
        if debug_msg:
            debug_list.append(debug_msg)
        else:
            all_scores.append(score)

    print(Counter(all_scores))

    avg_score = statistics.mean(all_scores)
    debug_stats = Counter(debug_list)

    print(f"{recipe} with {agent} over {n_iter} iterations:")
    print(f"Fails: {dict(debug_stats)}")
    print(f"Avg success score: {avg_score:.3f}")


def main():
    """Main entry point for the script."""

    recipe_book = intchef.RecipeBook()
    recipe = recipe_book.CHICKEN_FILLET_MEAL
    timeout = 13

    agent = intchef.agent.ActionAgent()
    # agent = intchef.agent.BruteForceAgent(avoid_idling=True)

    # run_n_sessions(agent, recipe, n_iter=100, timeout=20)
    run_cooking_session(agent, recipe, timeout)


if __name__ == '__main__':
    print()
    sys.exit(main())
