"""
The CookingSession class that handles each GOAP session.
"""

from collections import Counter
from typing import List

from .goap.abstract import Recipe
from .goap.agent import Agent
from .goap.components import Components

World: List[Components]


class CookingSession:
    """ An object to handle one entire cooking session. """

    def __init__(self, agent: Agent, recipe: Recipe):
        """Initializes a cooking session
        """

        self.time_elapsed: int = 0  # init: no time elapsed

        self.agent = agent

        # init: empty world
        self.world: World = recipe.get_ingredients()

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        # end_condition is when (subset(world state) == goal state)
        end_condition = (
            False
        )

        return True if end_condition else False

    def run(self) -> bool:

        world_state = self._get_world_state(self.world)
        print("Current world state:", world_state)
        world = self.agent.policy(world_state)

        return self._check_end()

    def _get_world_state(self, world: 'World') -> Counter:
        return Counter(world)

        # Step cycle

        # def step(self):
        #     """Step through one

        #     Returns:
        #     bool: If the game has ended
        #     """

        #     # Increment num_cycles
        #     self.time_elapsed += 1

        #     return self._check_end()
