
import random
from abc import ABC, abstractmethod
import sys
from typing import List, Tuple

from colours import Colour, colour
from intchef.goap.abstract import Recipe

from intchef.goap.actions import ALL_ACTIONS, Action, ActionList, Condition
from intchef.goap.world import World, WorldStateFrame


class Agent(ABC):

    def __init__(self) -> None:
        self.opened_nodes = 0
        self.success_nodes_found = 0
        self.timedout_nodes = 0

    def __repr__(self):
        return colour(Colour.PURPLE, self.__class__.__name__)

    def precompute(self, recipe: Recipe, timeout: int) -> int:
        return 0

    @abstractmethod
    def policy(self):
        pass

    def _get_legal_actions(self, world_state_frame: WorldStateFrame, verbose=False) -> List[Action]:
        """ Grab a list a legal Actions if the WorldStateFrame meets its preconditions """

        legal_actions = [
            action for action in ALL_ACTIONS
            if world_state_frame.meets_precondition(action.precond)
        ]

        if verbose:
            print('All Legal Actions:\n', legal_actions, end="\n\n")

        return legal_actions

    def _get_legal_actions_avoid_idling(
        self, world: World, timestamp: int, verbose=False
    ) -> List[Action]:
        """ Grab a list of legal Actions, but choose an effective action if possible if there are no pending delayed effects """

        legal_actions = self._get_legal_actions(world[timestamp], verbose)

        if (
            # No pending delayed effects
            (world.last_timestamp == timestamp) and
            # If there are effective actions, which excludes ActionList.IDLE
            (len(legal_actions) > 1 and ActionList.IDLE in legal_actions)
        ):
            legal_actions.remove(ActionList.IDLE)

        return legal_actions


class RandomAgent(Agent):

    def policy(self,
               world: World,
               timestamp: int
               ) -> Action:
        """ Randomly select an Action from the list of legal actions """

        legal_actions = self._get_legal_actions(
            world[timestamp], verbose=True)

        return random.choice(tuple(legal_actions))


class ActionAgent(Agent):

    def policy(self,
               world_state: World,
               timestamp: int,
               ) -> Action:
        """ Randomly select an Action from the list of legal actions, preferring not to Do Nothing """

        legal_actions = self._get_legal_actions_avoid_idling(
            world_state, timestamp, verbose=True)

        return random.choice(tuple(legal_actions))


class BruteForceAgent(Agent):
    """Brute-Force Uninformed Depth-First-Search """

    def __init__(self, avoid_idling: bool) -> None:
        super().__init__()
        self.avoid_idling = avoid_idling

    def __repr__(self):
        classname = super().__repr__()
        if self.avoid_idling:
            return f"{classname} with avoid idling"
        return classname

    def precompute(self, recipe: Recipe, timeout: int):

        self.opened_nodes = 0
        self.success_nodes_found = 0
        self.timedout_nodes = 0

        self.goal_state: Condition = recipe.goal_state
        self.dummy_world: World = World({0: recipe.ingredients})
        # adjust for starting count at 0
        self.timeout: int = timeout
        self.best_depth: int = self.timeout

        self.success, best_depth, self.best_plan = \
            self.DFS_recursion(self.dummy_world, 0)

        if self.success:
            print("BEST:", best_depth, self.best_plan)
            print(f"Through {self.opened_nodes} iterations")
        else:
            print(f"{type(self).__name__ } did not find a solution throughout {self.opened_nodes} opened nodes within the timeout limit of {self.timeout}. Consider increasing the timeout?")
            sys.exit()

        return self.opened_nodes

    def DFS_recursion(self, world: World, depth: int) -> Tuple[bool, int, str]:

        self.opened_nodes += 1

        # If reached timeout, return back
        if depth > self.timeout:
            # print("TIMEDOUT")
            self.timedout_nodes += 1
            return False, depth, world.action_hist

        # If goal state, return action history
        elif world[depth].meets_precondition(self.goal_state):
            self.success_nodes_found += 1
            # print("success state")
            return True, depth, world.action_hist

        # Else, recurse
        else:

            # Generate duplicate world state and actions
            if self.avoid_idling:
                legal_actions = \
                    self._get_legal_actions_avoid_idling(world, depth)
            else:
                legal_actions = self._get_legal_actions(world[depth])

            best_depth_subtree = 9999999
            best_plan: List[Action] = None
            subtree_has_success = False

            # Over all legal actions
            while legal_actions:

                # New parallel world timeline
                sub_world = world.dupe()

                # Apply top action
                current_action = legal_actions.pop(0)
                sub_world.update_world(current_action)

                # Recurse
                (success, new_depth, new_action_hist) = \
                    self.DFS_recursion(sub_world, depth+1)

                # If subtree has new high score
                if success and (new_depth < best_depth_subtree):
                    # Update new best stats
                    subtree_has_success = True
                    best_depth_subtree = new_depth
                    best_plan = new_action_hist

                del sub_world  # Garbage collection

            return subtree_has_success, best_depth_subtree, best_plan

    def policy(self,
               world: World,
               timestamp: int,
               ) -> Action:

        # Print the legal actions, for consistency with other agents
        self._get_legal_actions(world[timestamp], verbose=True)

        return self.best_plan[timestamp]
