import operator
import random
from abc import ABC, abstractmethod
from itertools import permutations
from typing import List

from regex import P

from intchef.goap.actions import ACTIVE_ACTIONS, Action, ActionList
from intchef.goap.world import WorldState, WorldStateFrame


class Agent(ABC):

    IDLE_SEQ = (ActionList.IDLE,)

    @abstractmethod
    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> List[Action]:
        """ Policy for action choice given all legal actions at world state """
        pass

    def policy(self, world_state: WorldState, timestamp: int) -> Action:
        """ Main policy wrapper, passes legal actions to specific policy """

        frame = world_state.get_last_frame

        # Grab a list of legal Actions if the current WorldState meets its preconditions
        legal_actns_seq_set = self._get_legal_actns_seq(frame)

        if legal_actns_seq_set:

            # Select action according to agent's policy
            action_list = self.my_policy(frame, timestamp, legal_actns_seq_set)

        # action_list.append(ActionList.IDLE)

        print(type(self).__name__, "chooses:", action_list, end="\n\n")

        return action_list

    def _get_legal_actns_seq(self, world_state_frame: WorldStateFrame) -> List[Action]:
        """ Grab a list of legal Actions if the current WorldState meets its preconditions """

        def recursive_legal_check(action_list, frame):
            return [(a1, recursive_legal_check(a2))
                    for a1 in action_list
                    for a2 in action_list
                    # if a1 meets criteria
                    # else #FIXME
                    ]

        precond = [
            action for action in ACTIVE_ACTIONS
            if world_state_frame.meets_precondition(action.precond)
        ]

        legal_actions_set = [

        ]

        legal_actions_set = set(permutations(precond))
        # legal_actions_set.add(self.IDLE_SEQ)

        print('All Legal Actions:\n', legal_actions_set, end="\n\n")

        return legal_actions_set


class RandomAgent(Agent):

    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> List[Action]:
        """ Randomly select a sequence of Actions from the list of legal Action sequences, including only Doing Nothing """
        return random.choice(tuple(legal_actions))


class ActionAgent(Agent):

    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> List[Action]:
        """ Randomly select a sequence of Actions from the list of legal Action sequences, preferring not to only Do Nothing """

        active_actions = legal_actions

        # # if any other action(s) than IDLE, remove IDLE
        # if len(legal_actions) > 1 and self.IDLE_SEQ in legal_actions:
        if len(legal_actions) > 1:
            active_actions.remove(self.IDLE_SEQ)

        return random.choice(tuple(active_actions))


class AgentList:
    """ List of all possible default agents as constants """

    RANDOM_AGENT = RandomAgent()
    ACTION_AGENT = ActionAgent()
