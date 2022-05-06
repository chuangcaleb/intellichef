""" World State of the session at any one time, across time dimensions """

from logging import root
import operator
from typing import Dict

from intchef.goap.actions import Action, ActionList
from intchef.goap.components import ComponentList


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

    def _clean_zero_entries(self):

        # Get list of zero entries
        zero_list = [(frame, comp)
                     for frame in self.values()
                     for comp, val in frame.items()
                     if val == 0]

        # Pop those zero entries
        for frame, comp in zero_list:
            frame.pop(comp)

    def _clone_frame(self, new_timestamp):
        self.update(
            {new_timestamp: self[new_timestamp-1].dupe()}
        )

    def get_range(self, timestamp: int, ineq_op: operator) -> 'WorldState':
        return {time: frame
                for time, frame in self.items()
                if ineq_op(time, timestamp)}

    def get_repr(self, timestamp: int, ineq_op: operator) -> 'str':
        return self._pretty_pformat(
            self.get_range(timestamp, ineq_op))

    # def dupe(self) -> 'WorldState':
    #     return WorldState(self.copy())
    def get_last_frame(self) -> WorldStateFrame:
        return self[len(self)-1]

    def meets_precondition(self, preconditions, timestamp: int) -> bool:
        # """ Precondition is found in the frame of the next timestamp. We need to cumalatively dirty the next timestamp's frame. """

        # next_timestamp = timestamp + 1

        # if timestamp == len(self)-1:  # If timestamp is the last timestamp
        #     self._clone_frame(next_timestamp)  # Generate new frame

        # frame = self[timestamp + 1]  # select next frame
        frame = self[timestamp]

        return True if frame.meets_precondition(preconditions) else False

    def update_world(self, action: Action, root_timestamp: int):
        # TODO: Combine and clean

        # Next absolute timestamp value after current root
        next_timestamp = root_timestamp + 1

        if action == ActionList.IDLE:  # If choosing to IDLE

            if next_timestamp not in self.keys():  # If next frame uncreated
                # Just clone for the next world state frame
                self._clone_frame(next_timestamp)

            return  # Terminate early either ways

        # Get absolute timestamps when there is an effect to apply
        all_effect_timestamps = [root_timestamp + t
                                 for t in action.effect.keys()]
        # Get timestamp of last effect, or just next_timestamp + 1 if no effects
        last_effect_timestamp = (max(all_effect_timestamps) + 1
                                 if all_effect_timestamps
                                 else next_timestamp + 1)

        max_timestamp = len(self)
        state_frame_offset = {}

        for timestamp in range(next_timestamp, last_effect_timestamp):

            # Create frames if not already existent
            if timestamp >= max_timestamp:
                # Reset offset if duping, since dupe carries the offset already
                state_frame_offset = {}
                # For the current frame, dupe from the previous frame
                self._clone_frame(timestamp)

            # Pop the upcoming frame's conditions
            if timestamp == next_timestamp:
                state_frame_offset.update({
                    cond: (self[timestamp][cond] - value)
                    if cond in state_frame_offset else -value
                    for cond, value in action.precond.items()
                })

            # If timestamp has an effect
            if timestamp in all_effect_timestamps:

                # Get current relative timestamp
                rel_timestamp = timestamp - root_timestamp

                # Modify or create condition
                state_frame_offset.update(
                    {cond: (state_frame_offset[cond] + value
                     if cond in state_frame_offset.keys()
                     else value)
                     for cond, value in action.effect[rel_timestamp].items()}
                )

            # Apply offset to current frame
            current_frame_components = self[timestamp].keys()
            for ko, vo in state_frame_offset.items():

                current_world_state = self[timestamp]

                # Apply offset to frame, create component if doesn't exist
                self[timestamp][ko] = current_world_state[ko] + vo \
                    if ko in current_frame_components else vo

        self._clean_zero_entries()
