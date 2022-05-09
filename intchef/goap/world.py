""" World State of the session at any one time, across time dimensions """

import operator
from typing import Dict
from intchef.goap.actions import Action, ActionList, Condition
from intchef.goap.components import ComponentList


class WorldStateFrame(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldStateFrame, self).__init__(initial_state, *args, **kw)

    def dupe(self) -> 'WorldStateFrame':
        # return copy.deepcopy(self)
        return WorldStateFrame(self.copy())

    def meets_precondition(self, preconditions: Condition) -> bool:

        # for component,value pair in precondition
        for component, value in preconditions.items():

            if (
                (component in self.keys())  # if world state has item and
                and (self[component] >= value)  # and also in enough quantity
            ):
                pass

            else:

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

    def __init__(self, initial_state: Dict[ComponentList, int], action_hist=None, *args, **kw):
        super(WorldState, self).__init__(initial_state, *args, **kw)

        if action_hist == None:
            self.action_hist = {}
        else:
            self.action_hist = action_hist

    def __repr__(self):
        return self._pretty_pformat(self, actions_h=True)

    def _pretty_pformat(self, states, actions_h=False):
        if actions_h == False:
            return "{" + "\n ".join([f"{k}: {v}"
                                     for k, v in states.items()]) + "}"
        else:
            action_timestamps = self.clean_action_hist.keys()
            return "{" + "\n ".join([

                # The timestamp and frame
                f"{ks}: {f}" +

                # The action, if any
                (f"\n → {self.clean_action_hist[ks]}" if ks in action_timestamps else "")

                for ks, f in states.items()

            ]) + "}"

    @property
    def _last_timestamp(self):
        return len(self) - 1

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

    def dupe(self) -> 'WorldState':
        # we can't deepcopy, because it also creates new references to constants
        # we want a deep copied Frame object with the shallow copied Foods
        return WorldState({key: frame.dupe() for key, frame in self.items()},
                          self.action_hist.copy())

    @property
    def clean_action_hist(self):
        return {k: v for k, v in self.action_hist.items()
                if v is not ActionList.IDLE}

    def get_repr(self, timestamp: int, ineq_op: operator, action_h=False) -> 'str':
        return self._pretty_pformat({time: frame
                                     for time, frame in self.items()
                                     if ineq_op(time, timestamp)},
                                    action_h)

    def meets_precondition(self, preconditions, timestamp: int) -> bool:

        frame = self[timestamp]

        return True if frame.meets_precondition(preconditions) else False

    def update_world(self, action: Action, root_timestamp: int):
        # TODO: Combine and clean

        self.action_hist.update({root_timestamp: action})

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

        # Init the last extra timestamp to process
        max_timestamp = max(self._last_timestamp+1, last_effect_timestamp)
        state_frame_offset = {}

        for timestamp in range(next_timestamp, max_timestamp):

            # Create frames if not already existent
            if timestamp > self._last_timestamp:
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


class World():

    def __init__(self, initial_state: WorldStateFrame = None):
        # super(WorldState, self).__init__(initial_state, *args, **kw)

        self.timeline = {}
        self.offsets = {}
        self.action_hist = {}

        if initial_state:
            self.timeline.update(WorldStateFrame(initial_state))
            self.offsets.update(WorldStateFrame(initial_state))

    def __getitem__(self, timestamp):
        return self.timeline[timestamp]

    def _clean_zero_entries(self):

        # Get list of zero entries
        zero_list = [comp
                     for comp, val
                     in self.timeline[self._last_timestamp].items()
                     if val == 0]

        # Pop those zero entries
        for comp in zero_list:
            self.timeline[self._last_timestamp].pop(comp)

    @property
    def _last_timestamp(self):
        return len(self.timeline) - 1

    def get_repr(self, timestamp: int, ineq_op: operator, action_h=False) -> 'str':
        # return {ts: frame for ts, frame in self.timeline if ts == _l}
        return self.timeline[self._last_timestamp]

    def meets_precondition(self, preconditions, timestamp: int) -> bool:

        current_frame = self.timeline[self._last_timestamp]

        # for component,value pair in precondition
        for component, value in preconditions.items():

            if (
                # if world state has item and
                (component in current_frame.keys())
                # and also in enough quantity
                and (current_frame[component] >= value)
            ):
                pass

            else:

                return False  # If it fails at all, instantly return False

        return True  # If it never fails, return True

    def update_world(self, action: Action, root_timestamp: int):

        self.action_hist.update({self._last_timestamp: action})

        next_timestamp = self._last_timestamp + 1

        # if action == ActionList.IDLE:  # If choosing to IDLE

        #     if next_timestamp not in self.keys():  # If next frame uncreated
        #         # Just clone for the next world state frame
        #         self._clone_frame(next_timestamp)

        all_effects_ts = [ts + self._last_timestamp
                          for ts in action.effect.keys()]
        print(all_effects_ts)
        last_effect_ts = max(all_effects_ts) if all_effects_ts \
            else self._last_timestamp + 1

        for timestamp in range(next_timestamp, last_effect_ts+1):
            if timestamp not in self.offsets:
                self.offsets[timestamp] = {}

        # print("Precond:", self.offsets)

        # Update preconditions
        next_offset = self.offsets[next_timestamp]
        for comp, modifier in action.precond.items():
            if (comp in next_offset):
                next_offset[comp] -= modifier
            else:
                next_offset.update({comp: -modifier})

        # print("Precond:", self.offsets)

        # Update offsets
        for timestamp, effects_list in action.effect.items():
            rel_offset = self.offsets[timestamp + self._last_timestamp]
            for comp, modifier in effects_list.items():
                if (comp in rel_offset):
                    rel_offset[comp] += modifier
                else:
                    rel_offset.update({comp: modifier})

        # print("Postcond:", self.offsets)
        self.update_timeline()

    def update_timeline(self):

        self.timeline[self._last_timestamp + 1] \
            = self.timeline[self._last_timestamp].dupe()

        for item, value in self.offsets[self._last_timestamp].items():
            if item in self.timeline[self._last_timestamp]:
                self.timeline[self._last_timestamp][item] += value
            else:
                self.timeline[self._last_timestamp][item] = value

        self._clean_zero_entries()
