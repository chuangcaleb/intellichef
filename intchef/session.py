"""
The CookingSession class that handles each GOAP session.
"""


from .goap.abstract import Recipe
from .goap.agent import Agent
from .goap.colors import green, red
from .goap.world import WorldState


class CookingSession:
    """ An object to handle one entire cooking session. """

    def __init__(self, agent: Agent, recipe: Recipe, timeout: int = 10):
        """Initializes a cooking session"""

        self.time_elapsed: int = 0  # init: no time elapsed
        self.error_msg = None

        self.agent = agent
        self.recipe = recipe
        self.timeout = timeout

        # init: default WorldState
        self.world_state: WorldState = recipe.ingredients

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        should_terminate = False

        # end_condition is when (subset(world state) == goal state)
        if self.world_state.meets_precondition(self.recipe.goal_state):
            should_terminate = True
            print(green(
                f"\n\nSuccessfully made: {self.recipe.display_name}!\n"))

        if self.time_elapsed >= self.timeout:
            should_terminate = True
            print(red("\n\nExceeded time limit!\n"))

        if self.error_msg != None:
            should_terminate = True
            print(red(f"\n\nERROR: {self.error_msg}\n"))

        return should_terminate

    def main(self) -> bool:

        self.recipe.print_details()

        while not self._check_end():
            self.loop()
            self.time_elapsed += 1

        print("Final world state:\n", self.world_state)

        return self.time_elapsed

    def loop(self) -> bool:

        print("\n\n> Time:", green(self.time_elapsed), "--------------------\n")

        # world_state = self._get_world_state(self.world)
        print("Current world state:\n", self.world_state, end="\n\n")

        action = self.agent.policy(self.world_state)

        if action:
            self.world_state.update_condition(action)
        else:
            self.error_msg = "Stuck, no legal actions!"
