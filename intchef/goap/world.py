""" World State of the session at any one time, across time dimensions """

import operator
from typing import Dict

from .actions import Action
from .components import ComponentList


class WorldStateFrame(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldStateFrame, self).__init__(initial_state, *args, **kw)

    def dupe(self) -> 'WorldStateFrame':
        return WorldStateFrame(self.copy())

    def meets_precondition(self, preconditions) -> bool:

        # for precondition in precondition
        for condition, value in preconditions.items():

            if (
                # if world state has item
                (condition in self.keys()) and
                # and also in enough quantity
                (self[condition] >= value)
            ):
                pass

            else:
                # print(self, preconditions)
                return False  # If it fails at all, instantly return False

        return True  # If it never fails, return True

    def update_frame(self, action: Action):

        updated_frame = {}

        # Pop conditions from world state
        updated_frame.update(
            {cond: (self[cond] - action.precond[cond])
             for cond in action.precond}
        )

        for cond in action.effect:

            # Push new condition into world state frame
            if cond in self.keys():  # Add to current count
                updated_frame[cond] = (
                    self[cond] + action.effect[cond]
                )
            else:  # Or add a new component
                updated_frame.update({cond: action.effect[cond]})

        self.update(updated_frame)


class WorldState(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldState, self).__init__({0: initial_state}, *args, **kw)

    def __repr__(self):
        return self._pretty_pformat(self)

    def _pretty_pformat(self, dict):
        return "{" + "\n ".join([str(k) + ": " + str(v)
                                 for k, v in dict.items()]) + "}"

    def get_repr(self, timestamp: int, ineq_op: operator) -> 'str':
        return self._pretty_pformat({time: frame
                                     for time, frame in self.items()
                                     if ineq_op(time, timestamp)})

    def meets_precondition(self, preconditions, timestamp: int) -> bool:

        frame = self[timestamp]

        return True if frame.meets_precondition(preconditions) else False

    def update_world(self, action: Action, root_timestamp: int):
        # TODO: Combine and clean

        # Initialize world state from here onwards
        updated_world_state = {state: frame
                               for state, frame in self.items()
                               if state >= root_timestamp}

        # Next absolute timestamp value after current root
        next_timestamp = root_timestamp + 1
        # Get absolute timestamps where there is an effect
        all_effect_timestamps = [root_timestamp + t
                                 for t in action.effect.keys()]
        # Get timestamp of last effect, or just next_timestamp + 1 if no effects
        last_effect_timestamp = (max(all_effect_timestamps) + 1
                                 if all_effect_timestamps
                                 else next_timestamp + 1)

        # Clone yet-to-exist frames with previous frame
        for timestamp in range(next_timestamp, last_effect_timestamp):

            if timestamp not in updated_world_state.keys():
                updated_world_state.update(
                    {timestamp: updated_world_state[timestamp-1].dupe()}
                )

        if action.name == "Do Nothing":
            self.update(updated_world_state)
            return  # Terminate early after creating next WorldFrame

        for timestamp in range(next_timestamp, last_effect_timestamp):

            # Pop the upcoming frame's conditions
            updated_world_state[timestamp].update({
                cond: (updated_world_state[timestamp][cond] - value)
                for cond, value in action.precond.items()
            })

            # If timestamp has an effect
            if timestamp in all_effect_timestamps:

                # Get current relative timestamp
                rel_timestamp = timestamp - root_timestamp

                # Modify or create condition
                updated_world_state[timestamp].update(
                    {cond: (updated_world_state[timestamp][cond] + value
                     if cond in updated_world_state[timestamp] else value)
                     for cond, value in action.effect[rel_timestamp].items()}
                )

        # print(updated_world_state)
        self.update(updated_world_state)
        self._clean_zero_entries()

    def _clean_zero_entries(self):

        # Get list of zero entries
        zero_list = [(frame, comp)
                     for frame in self.values()
                     for comp, val in frame.items()
                     if val == 0]

        # Pop those zero entries
        for frame, comp in zero_list:
            frame.pop(comp)
