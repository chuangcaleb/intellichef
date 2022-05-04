"""
The CookingSession class that handles each GOAP session.
"""


from .goap.abstract import Recipe
from .goap.agent import Agent
from .goap.colors import green, red
from .goap.world import WorldState
import pprint as pp


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
            print(red(f"\n\nExceeded time limit of {self.timeout}!\n"))
            return True

        if self.error_msg != None:
            print(red(f"\n\nERROR: {self.error_msg}\n"))
            return True

        # end_condition is when (subset(world state) == goal state @ timestamp)
        if self.world_state.meets_precondition(
                self.recipe.goal_state, self.timestamp):
            print(green(
                f"\n\nSuccessfully made: {self.recipe.display_name}!\n"))
            return True

        # Else, return False
        return False

    def main(self) -> bool:
        """ Main entry method that loops, returns timestamp at termination """

        self.recipe.print_details()

        while not self._check_end():
            self.loop()
            self.timestamp += 1

        world_history = self.world_state.get_history(self.timestamp)

        print("Final world state history:\n")
        print("\n".join([f"{k}: {v}" for k, v in world_history.items()]))
        print()

        return self.timestamp

    def loop(self) -> bool:
        """ Loop method, makes choices every tick """

        print("\n\n> Time:", green(self.timestamp), "--------------------\n")

        # world_state = self._get_world_state(self.world)
        print("Current world state:\n", self.get_future_states(), end="\n\n")

        action = self.agent.policy(self.world_state, self.timestamp)

        if action:
            self.world_state.update_world(action, self.timestamp)
        else:
            self.error_msg = "Stuck, no legal actions!"

    def get_future_states(self):
        return {time: frame
                for time, frame in self.world_state.items()
                if time >= self.timestamp}
