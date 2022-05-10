""" World State of the session at any one time, across time dimensions """

import operator
from typing import Dict
from intchef.goap.actions import Action, ActionList, Condition
from intchef.goap.components import ComponentList


class WorldStateFrame(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldStateFrame, self).__init__(initial_state, *args, **kw)

    def dupe(self) -> 'WorldStateFrame':
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


class World():

    def __init__(self, initial_state: WorldStateFrame = None):

        self.timeline = {}
        self.offsets = {}
        self.action_hist = {}

        if initial_state:
            self.timeline.update(WorldStateFrame(initial_state))
            self.offsets.update(WorldStateFrame(initial_state))

    def __getitem__(self, timestamp):
        return self.timeline[timestamp]

    def __repr__(self):
        return self._pretty_pformat(self.timeline, actions_h=True)

    def _clean_zero_entries(self):

        # Get list of zero entries
        zero_list = [comp
                     for comp, val
                     in self.timeline[self.last_timestamp].items()
                     if val == 0]

        # Pop those zero entries
        for comp in zero_list:
            self.timeline[self.last_timestamp].pop(comp)

    @property
    def _clean_action_hist(self):
        return {k: v for k, v in self.action_hist.items()
                if v is not ActionList.CONTINUE}

    def _pretty_pformat(self, timeline, actions_h=False):
        if actions_h == False:
            return "{" + "\n ".join([f"{k}: {v}"
                                     for k, v in timeline.items()]) + "}"
        else:
            action_timestamps = self._clean_action_hist.keys()
            return "{" + "\n ".join([

                # The timestamp and frame
                f"{ks}: {f}" +

                # The action, if any
                (f"\n → {self._clean_action_hist[ks]}" if ks in action_timestamps else "")

                for ks, f in timeline.items()

            ]) + "}"

    @property
    def last_timestamp(self):
        return len(self.timeline) - 1

    def dupe(self) -> 'World':
        cop = World()
        cop.timeline = self.timeline.copy()
        cop.offsets = self.offsets.copy()
        cop.action_hist = self.action_hist.copy()
        return cop  # ? TODO : Why does it break when always Continue Previous?

    def get_repr(self, timestamp: int, ineq_op: operator, action_h=False) -> 'str':
        return self._pretty_pformat({time: frame
                                     for time, frame in self.timeline.items()
                                     if ineq_op(time, timestamp)},
                                    action_h)

    def meets_precondition(self, preconditions) -> bool:

        last_frame = self.timeline[self.last_timestamp]
        return last_frame.meets_precondition(preconditions)

    def update_world(self, action: Action):

        self.action_hist.update({self.last_timestamp: action})

        next_timestamp = self.last_timestamp + 1

        all_effects_ts = [ts + self.last_timestamp
                          for ts in action.effect.keys()]
        last_effect_ts = max(all_effects_ts) if all_effects_ts \
            else self.last_timestamp + 1

        for timestamp in range(next_timestamp, last_effect_ts+1):
            if timestamp not in self.offsets:
                self.offsets[timestamp] = {}

        # print("Initial:", self.offsets)

        # Update preconditions
        next_offset = self.offsets[next_timestamp]
        for comp, modifier in action.precond.items():
            if (comp in next_offset):
                next_offset[comp] -= modifier
            else:
                next_offset.update({comp: -modifier})

        # print("Precond:", self.offsets)

        # Update effects
        for timestamp, effects_list in action.effect.items():
            rel_offset = self.offsets[timestamp + self.last_timestamp]
            for comp, modifier in effects_list.items():
                if (comp in rel_offset):
                    rel_offset[comp] += modifier
                else:
                    rel_offset.update({comp: modifier})

        # print("Postcond:", self.offsets)
        self.update_timeline()

    def update_timeline(self):

        self.timeline[self.last_timestamp + 1] \
            = self.timeline[self.last_timestamp].dupe()

        for item, value in self.offsets[self.last_timestamp].items():
            if item in self.timeline[self.last_timestamp]:
                self.timeline[self.last_timestamp][item] += value
            else:
                self.timeline[self.last_timestamp][item] = value

        self._clean_zero_entries()
