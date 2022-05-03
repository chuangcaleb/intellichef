"""
The CookingSession class that handles each GOAP session.
"""

from typing import Dict, List

from .goap.abstract import Recipe
from .goap.actions import Action
from .goap.agent import Agent
from .goap.colors import green, red
from .goap.components import Components

WorldState: List[Components]


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
        self.world_state = recipe.ingredients

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        should_terminate = False

        # end_condition is when (subset(world state) == goal state)
        if self.world_state == self.recipe.goal_state:
            should_terminate = True
            print(green("\n\nSuccessfully made", self.recipe.display_name, "!"))

        if self.time_elapsed >= self.timeout:
            should_terminate = True
            print(red("\n\nExceeded time limit!"))

        if self.error_msg != None:
            should_terminate = True
            print(red("\n\nERROR:", self.error_msg))

        return should_terminate

    def main(self) -> bool:

        self.recipe.print_details()

        while not self._check_end():
            self.loop()
            self.time_elapsed += 1

        return self.time_elapsed

    def loop(self) -> bool:

        print("\n\n> Time:", green(self.time_elapsed), "--------------------\n")

        # world_state = self._get_world_state(self.world)
        print("Current world state:\n", self.world_state, end="\n\n")

        action = self.agent.policy(self.world_state)
        self.world_state.update_condition(action)


class WorldState(Dict):

    # def __init__(self, initial_state: Dict[Components, int]):
    #     self.world_state = initial_state

    def __init__(self, initial_state: Dict[Components, int], *args, **kw):
        super(WorldState, self).__init__(initial_state, *args, **kw)
        self.itemlist = super(WorldState, self).keys()

    # def __repr__(self):
    #     return str(self.world_state)

    # def __get__(self):
    #     return self.world_state

    def meets_precondition(self, preconditions) -> bool:

        # for precondition in precondition
        for condition, value in preconditions.items():

            if (
                # if world state has item
                (condition in self.keys()) and
                # and also in enough quantity
                (value >= self[condition])
            ):
                # print(condition)
                pass

            else:
                return False  # If it fails at all, instantly return False

        return True  # If it never fails, return True

    def update_condition(self, action: Action):

        updated_world_state = {}

        for cond in action.precond:
            # print(cond)
            # print(self)
            # print(self[cond])

            # Pop conditions from world state
            updated_world_state[cond] = (
                self[cond] - action.precond[cond]
            )

        for cond in action.effect:
            # print(cond)
            # print(old_world_state)

            # Push new condition into world state
            if cond in self.keys():  # Add to current count
                updated_world_state[cond] = (
                    self[cond] + action.effect[cond]
                )
            else:  # Or add a new component
                updated_world_state.update({cond: action.effect[cond]})

        self.update(updated_world_state)
