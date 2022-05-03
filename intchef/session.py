"""
The CookingSession class that handles each GOAP session.
"""

from collections import Counter
from typing import List

from .goap.colors import green, red

from .goap.abstract import Recipe
from .goap.agent import Agent
from .goap.components import Components

World: List[Components]


class CookingSession:
    """ An object to handle one entire cooking session. """

    def __init__(self, agent: Agent, recipe: Recipe, timeout: int = 10):
        """Initializes a cooking session
        """

        self.time_elapsed: int = 0  # init: no time elapsed

        self.agent = agent
        self.recipe = recipe
        self.timeout = timeout

        # init: empty world
        self.world: World = recipe.get_ingredients()

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        should_terminate = False

        # end_condition is when (subset(world state) == goal state)
        if self.world == self.recipe.goal_state:
            should_terminate = True
            print(green("\n\nSuccessfully made", self.recipe.display_name, "!"))

        if self.time_elapsed >= self.timeout:
            should_terminate = True
            print(red("\n\nExceeded time limit!"))

        return should_terminate

    def run(self) -> bool:

        print("\n\n> Time:", green(self.time_elapsed), "--------------------\n")

        world_state = self._get_world_state(self.world)
        print("Current world state:\n", world_state, end="\n\n")

        action = self.agent.policy(world_state)
        print(action.precond)

    def loop(self) -> bool:

        self.recipe.print_details()

        # Handle termination
        while not self._check_end():
            self.run()
            self.time_elapsed += 1

        return self.time_elapsed

    def _get_world_state(self, world: 'World') -> Counter:
        return Counter(world)

    # def _process_action(action, world):

        # Step cycle

        # def step(self):
        #     """Step through one

        #     Returns:
        #     bool: If the game has ended
        #     """

        #     # Increment num_cycles
        #     self.time_elapsed += 1

        #     return self._check_end()
