import random
from abc import ABC, abstractmethod
from typing import List

from .actions import ALL_ACTIONS, Action

# from intchef.session import WorldState


class Agent(ABC):

    @abstractmethod
    def policy(world_state):
        pass

    def _get_legal_actions(self, world_state_frame) -> List[Action]:

        legal_actions = [
            action for action in ALL_ACTIONS
            if world_state_frame.meets_precondition(action.precond)
        ]

        return legal_actions


class RandomAgent(Agent):

    def policy(self, world_state, timestamp) -> Action:

        legal_actions = self._get_legal_actions(world_state[timestamp])
        print('All Legal Actions:\n', legal_actions, end="\n\n")

        if len(legal_actions) > 0:

            action = random.choice(tuple(legal_actions))
            print(type(self).__name__, "chooses:", action, end="\n\n")

        else:  # If stuck, return None
            action = None

        return action


class ActionAgent(Agent):

    def policy(self, world_state, timestamp) -> Action:

        legal_actions = self._get_legal_actions(world_state[timestamp])
        print('All Legal Actions:\n', legal_actions, end="\n\n")

        if len(legal_actions) > 0:

            # if "Do Nothing" in

            action = random.choice(tuple(legal_actions))
            print(type(self).__name__, "chooses:", action, end="\n\n")

        else:  # If stuck, return None
            action = None

        return action


class AgentList:

    RANDOM_AGENT = RandomAgent()
    ACTION_AGENT = ActionAgent()
