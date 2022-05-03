from abc import ABC, abstractmethod
import random
from typing import List


from .actions import ALL_ACTIONS, Action


class Agent(ABC):

    @abstractmethod
    def policy(world_state):
        pass

    def get_legal_actions(self, world_state) -> List[Action]:

        legal_actions = [
            action for action in ALL_ACTIONS
            if self._meets_precondition(action.precond, world_state)
        ]

        print(world_state)
        # print(legal_actions[0].precond)
        # print()

        # toast_precond = legal_actions[0].precond
        # print(self._meets_precondition(toast_precond, world_state))

        # print(legal_actions[0].precond in dict(world_state.keys()))

        return legal_actions

    def _meets_precondition(self, preconditions, world_state) -> bool:

        # for precondition in precondition
        for condition, value in preconditions.items():

            if (
                # if world state has item
                (condition in world_state.keys()) and
                # and also in enough quantity
                (value >= world_state[condition])
            ):
                # print(condition)
                pass

            else:
                return False  # If it fails at all, instantly return False

        return True  # If it never fails, return True

        # check = True
        # return check


class RandomAgent(Agent):

    def policy(self, world_state) -> Action:

        legal_actions = self.get_legal_actions(world_state)
        print('All Legal Actions:\n', legal_actions, end="\n\n")

        if len(legal_actions) > 0:

            action = random.choice(tuple(legal_actions))
            print(type(self).__name__, "chooses:", action, end="\n\n")

        else:

            action = []

        return action
