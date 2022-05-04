"""
Defines all GOAP actions
"""

from .colors import red
from .components import ComponentList


class Action:

    def __init__(self, name: str, precond, effect):
        self.name = name
        self.precond = precond
        self.effect = effect

    def __repr__(self):
        return red(self.name)


class ActionList:

    IDLE = Action(
        name="Do Nothing",
        precond={},
        effect={}
    )
    TOAST_BREAD = Action(
        name="Toast Bread",
        precond={ComponentList.BREAD: 1},
        effect={3: {ComponentList.TOAST: 1}}
    )

    ASSEMBLE_SIMPLE_TOAST_SANDWICH = Action(
        name="Assemble Simple Toast Sandwich",
        precond={
            ComponentList.TOAST: 2,
            ComponentList.HAM: 1,
            ComponentList.CHEESE: 1
        },
        effect={1: {ComponentList.SIMPLE_TOAST_SANDWICH: 1}}
    )


ALL_ACTIONS = [v for k, v in ActionList.__dict__.items()
               if isinstance(v, Action)]
