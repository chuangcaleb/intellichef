from typing import Dict

from .goap.actions import Action
from .goap.components import ComponentList


class WorldState(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(WorldState, self).__init__(initial_state, *args, **kw)
        self.itemlist = super(WorldState, self).keys()

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

    def update_condition(self, action: Action):

        updated_world_state = {}

        # Pop conditions from world state
        updated_world_state.update(
            {cond: (self[cond] - action.precond[cond])
             for cond in action.precond}
        )

        for cond in action.effect:

            # Push new condition into world state
            if cond in self.keys():  # Add to current count
                updated_world_state[cond] = (
                    self[cond] + action.effect[cond]
                )
            else:  # Or add a new component
                updated_world_state.update({cond: action.effect[cond]})

        self.update(updated_world_state)
