""" World State of the session at any one time, across time dimensions """

from turtle import update
from typing import Dict

from .actions import Action
from .components import ComponentList


class WorldStateFrame(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldStateFrame, self).__init__(initial_state, *args, **kw)
        # self.itemlist = super(WorldStateFrame, self).keys()

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

    def pop_conditions(self, preconds: Dict):
        # updated_frame = {}

        # Pop conditions from world state
        self.update({
            cond: (self[cond] - preconds[cond])
            for cond in preconds
        })

        # print(updated_frame)

        # self.update(updated_frame)


class WorldState(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldState, self).__init__({0: initial_state}, *args, **kw)
        # self.itemlist = super(WorldState, self).keys()

    def __repr__(self):
        return "{" + "\n ".join([str(k) + ": " + str(v) for k, v in self.items()]) + "}"

    def meets_precondition(self, preconditions, timestamp: int) -> bool:

        frame = self[timestamp]

        return True if frame.meets_precondition(preconditions) else False

    def update_world(self, action: Action, root_timestamp: int):

        # Initialize world state from afterwards
        updated_world_state = {state: frame for state, frame in self.items()
                               if state > root_timestamp}

        # If currently the latest timestamp, create new identical timestamp
        if not updated_world_state:
            updated_world_state.update(
                {root_timestamp+1: self[root_timestamp].dupe()})

        # Pop preconditions up till last state in dict
        # updated_world_state.update({
        #     state: old_frame.pop_conditions(action.precond)
        #     for state, old_frame in updated_world_state.items()
        # })

        self.update(updated_world_state)

        [
            self[timestamp].pop_conditions(action.precond)
            for timestamp, new_frame in updated_world_state.items()
        ]

        # Generate clone states up till last state in effect

        # Push effects recursively up till last state in dict

        # Calculate offset of all components
        self.update(updated_world_state)

        pass
