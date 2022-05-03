""" 
Defines all GOAP actions
"""


from .colors import red
from .components import ComponentList


class Action:

    def __init__(self, name, precond, effect, time_elapsed):
        self.name = name
        self.precond = precond
        self.effect = effect
        self.time_elapsed = time_elapsed

    def __repr__(self):
        return red(self.name)


ALL_ACTIONS = {
    Action(
        name="Toast Bread",
        precond={ComponentList.BREAD: 1},
        effect={ComponentList.TOAST: 1},
        time_elapsed=4,
    ),
    Action(
        name="Assemble Simple Toast Sandwich",
        precond={
            ComponentList.TOAST: 2,
            ComponentList.HAM: 1,
            ComponentList.CHEESE: 1
        },
        effect={ComponentList.TOAST: 1},
        time_elapsed=4,
    )
}
