"""
The CookingSession class definition that handles each GOAP session.
"""


from intchef.goap.abstract import Recipe
from intchef.goap.actions import ActionList
from intchef.goap.agent import Agent
from colours import Colour, colour
from intchef.goap.world import WorldState
import operator


class CookingSession:
    """ An object to handle one entire cooking session. """

    def __init__(self, agent: Agent, recipe: Recipe, timeout: int = 10):
        """Initializes a cooking session"""

        self.timestamp: int = 0  # init: no time elapsed
        self.error_msg = None

        self.agent = agent
        self.recipe = recipe
        self.timeout = timeout

        # init: default WorldState
        self.world_state = WorldState(recipe.ingredients)

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        if self.timestamp > self.timeout:
            print(colour(Colour.RED,
                         f"\n\nTimed out, exceeded time limit of {self.timeout}!\n"))
            return True

        if self.error_msg != None:
            print(colour(Colour.RED, f"\n\nERROR: {self.error_msg}\n"))
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
        print(self.world_state.get_repr(self.timestamp, operator.le))
        print()

        return self.timestamp

    def loop(self) -> bool:
        """ Loop method, makes choices every tick """

        print("\n\n> Time:", colour(Colour.GREEN, self.timestamp),
              "-------------------------------------------------------------\n")

        # Let agent make actions until agent chooses to IDLE
        action_list = self.agent.policy(self.world_state, self.timestamp)
        for action in action_list:
            self.world_state.update_world(action, self.timestamp)
        # while action != ActionList.IDLE:
        #     print(self.world_state)
        #     action = self.agent.policy(self.world_state, self.timestamp)
        #     break

        print("New world state from current timestamp:")
        print(self.world_state.get_repr(self.timestamp, operator.ge), end="\n\n")
