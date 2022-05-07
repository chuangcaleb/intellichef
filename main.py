import statistics
import sys

import intchef


def run_cooking_session(agent, recipe):
    """Runs a full cooking session

    Returns:
            int: total time elapsed for cooking
    """
    session = intchef.CookingSession(agent, recipe)
    score = session.main()
    print(f"Time taken: {score}\n\n")
    return score


def run_n_sessions(agent, recipe, n_iter: int):

    all_scores = []

    for _ in range(1, n_iter):
        score = run_cooking_session(agent, recipe)
        all_scores.append(score)

    avg_score = statistics.mean(all_scores)

    print(f"{recipe} with {agent} over {n_iter} iterations:")
    print(f"Avg Score: {avg_score:.3f}")


def main():
    """Main entry point for the script."""

    agent_list = intchef.AgentList()
    agent = agent_list.RANDOM_AGENT

    recipe_book = intchef.RecipeBook()
    recipe = recipe_book.CHICKEN_FILLET_RICE

    run_n_sessions(agent, recipe, n_iter=100)
    # run_cooking_session(agent, recipe)


if __name__ == '__main__':
    print()
    sys.exit(main())
