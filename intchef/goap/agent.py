import random
from abc import ABC, abstractmethod
from typing import List

from .actions import ALL_ACTIONS, Action, ActionList
from .world import WorldState, WorldStateFrame


class Agent(ABC):

    @abstractmethod
    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> Action:
        """ Policy for action choice given all legal actions at world state """
        pass

    def policy(self, world_state: WorldState, timestamp: int) -> Action:
        """ Main policy wrapper, handles if no legal actions and then runs specific policy """

        # Grab a list of legal Actions if the current WorldState meets its preconditions
        legal_actions = self._get_legal_actions(world_state[timestamp])

        if legal_actions:  # If there are any legal actions

            # Select action according to agent's policy
            action = self.my_policy(world_state, timestamp, legal_actions)
            print(type(self).__name__, "chooses:", action, end="\n\n")

        else:  # If no action in legal_actions, return None

            action = None

        return action

    def _get_legal_actions(self, world_state_frame: WorldStateFrame) -> List[Action]:
        """ Grab a list of legal Actions if the current WorldState meets its preconditions """

        legal_actions = [
            action for action in ALL_ACTIONS
            if world_state_frame.meets_precondition(action.precond)
        ]

        print('All Legal Actions:\n', legal_actions, end="\n\n")

        return legal_actions


class RandomAgent(Agent):

    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> Action:
        """ Randomly select an Action from the list of legal actions """
        return random.choice(tuple(legal_actions))


class ActionAgent(Agent):

    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> Action:
        """ Randomly select an Action from the list of legal actions, preferring not to Do Nothing """

        # if any other action(s) than IDLE, remove IDLE
        if len(legal_actions) > 1 and ActionList.IDLE in legal_actions:
            legal_actions.remove(ActionList.IDLE)

        return random.choice(tuple(legal_actions))


class AgentList:
    """ List of all possible default agents as constants """

    RANDOM_AGENT = RandomAgent()
    ACTION_AGENT = ActionAgent()
