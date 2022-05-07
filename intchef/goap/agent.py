
import random
from abc import ABC, abstractmethod
import sys
from typing import List, Tuple

from colours import Colour, colour
from intchef.goap import world
from intchef.goap.abstract import Recipe

from intchef.goap.actions import ALL_ACTIONS, Action, ActionList
from intchef.goap.world import WorldState, WorldStateFrame


class Agent(ABC):

    def __repr__(self):
        return colour(Colour.PURPLE, self.__class__.__name__)

    @abstractmethod
    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> Action:
        """ Policy for action choice given all legal actions at world state """
        pass

    def policy(self, world_state: WorldState, timestamp: int) -> Action:
        """ Main policy wrapper, passes legal actions to specific policy """

        # Grab a list of legal Actions if the current WorldState meets its preconditions
        legal_actions = self._get_legal_actions(world_state[timestamp])

        print('All Legal Actions:\n', legal_actions, end="\n\n")

        # Select action according to agent's policy
        action = self.my_policy(world_state, timestamp, legal_actions)
        # print(type(self).__name__, "chooses:", action, end="\n\n")

        return action

    def _get_legal_actions(self, world_state_frame: WorldStateFrame) -> List[Action]:
        """ Grab a list of legal Actions if the current WorldState meets its preconditions """

        legal_actions = [
            action for action in ALL_ACTIONS
            if world_state_frame.meets_precondition(action.precond)
        ]

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


class BruteForceAgent(Agent):
    """Brute Force Uninformed Search """

    def __init__(self, recipe: Recipe, timeout: int):
        # self.iter = 0
        # self.solved = False

        self.goal_state = recipe.goal_state
        self.dummy_world = WorldState({0: recipe.ingredients})
        # adjust for starting count at 0
        self.timeout = self.best_depth = timeout - 1

        self.success, best_depth, self.best_policy = \
            self.DFS_recursion(self.dummy_world, 0)

        if self.success:
            print("BEST:", best_depth, self.best_policy)
        else:
            print(type(self).__name__ +
                  " did not find a solution within the timeout limit. Consider increasing the timeout?")
            sys.exit()

    def DFS_recursion(self, world_state: WorldState,
                      depth: int) -> Tuple[bool, int, str]:

        # If goal state, return action history
        if world_state[depth].meets_precondition(self.goal_state):

            # print("success state")
            return True, depth, world_state.action_hist

        # If reached timeout, return back
        elif depth > self.timeout:
            # print("TIMEDOUT")
            return False, depth, world_state.action_hist

        # Else, recurse
        else:
            # Generate duplicate world state and actions
            legal_actions = self._get_legal_actions(world_state[depth])
            best_depth_subtree = 9999999
            best_action_hist = None
            subtree_has_success = False

            # Over all legal actions
            while legal_actions:

                # New parallel world timeline
                sub_world = world_state.dupe()

                # Apply top action
                current_action = legal_actions.pop(0)
                sub_world.update_world(current_action, depth)

                # Recurse
                (success, new_depth, new_action_hist) = \
                    self.DFS_recursion(sub_world, depth+1)

                # If subtree has new high score
                if success and (new_depth < best_depth_subtree):
                    # Update new best stats
                    subtree_has_success = True
                    best_depth_subtree = new_depth
                    best_action_hist = new_action_hist

            return subtree_has_success, best_depth_subtree, best_action_hist

    def my_policy(self,
                  world_state: WorldState,
                  timestamp: int,
                  legal_actions: List[Action]) -> Action:
        return self.best_policy[timestamp]
