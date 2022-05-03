from abc import ABC, abstractmethod
import random

from .actions import ALL_ACTIONS


class Agent(ABC):

    @abstractmethod
    def policy(world_state):
        pass


class RandomAgent(Agent):

    def policy(self, world_state):
        print('All Actions:', ALL_ACTIONS)
        action = random.choice(tuple(ALL_ACTIONS))
        print(type(self).__name__, "has chosen:", action, end="\n\n")
        return action
