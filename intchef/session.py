"""
The CookingSession class definition that handles each GOAP session.
"""


from intchef.goap.abstract import Recipe
from intchef.goap.agent import Agent
from colours import Colour, colour
from intchef.goap.world import WorldState
import operator


class CookingSession:
    """ An object to handle one entire cooking session. """

    def __init__(self, agent: Agent, recipe: Recipe, timeout: int = 15):
        """Initializes a cooking session"""

        self.timestamp: int = 0  # init: no time elapsed
        self.debug_msg = None

        self.agent: Agent = agent
        self.recipe: Recipe = recipe
        self.timeout: int = timeout

        # init: default WorldState
        self.world_state: WorldState = WorldState({0: recipe.ingredients})

        # Precompute agent plan
        self.agent.precompute(recipe, timeout)

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        if self.debug_msg != None:
            print(colour(Colour.RED, f"\n\nERROR: {self.debug_msg}\n"))
            return True

        if self.timestamp > self.timeout:
            print(colour(Colour.RED,
                         f"\n\nTimed out, exceeded time limit of {self.timeout}!\n"))
            self.debug_msg = "Timed out"
            return True

        # end_condition is when (subset(world state) == goal state @ timestamp)
        if self.world_state.meets_precondition(
                self.recipe.goal_state, self.timestamp):
            print(colour(Colour.GREEN,
                         f"\n\nSuccessfully made: {self.recipe.name}!\n"))
            return True

        # Else, return False
        return False

    def main(self) -> bool:
        """ Main entry method that loops, returns timestamp at termination """

        self.recipe.print_details()

        while not self._check_end():
            self.loop()
            self.timestamp += 1

        print("Final world state history:")
        print(self.world_state.get_repr(
            self.timestamp, operator.le, action_h=True))
        print()

        return self.timestamp, self.debug_msg, self.agent.opened_nodes

    def loop(self) -> bool:
        """ Loop method, makes choices every tick """

        print("\n\n> Time:", colour(Colour.GREEN, self.timestamp),
              "-------------------------------------------------------------\n")

        print("Current world state:")
        print(self.world_state.get_repr(self.timestamp, operator.ge), end="\n\n")

        action = self.agent.policy(self.world_state, self.timestamp)
        print(type(self.agent).__name__, "chooses:", action, end="\n\n")
        self.world_state.update_world(action, self.timestamp)
