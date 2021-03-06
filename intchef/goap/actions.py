"""
Defines all GOAP actions
"""

from typing import Dict

from colours import Colour, colour
from intchef.goap.components import ComponentList, EquipmentList, IngredientList


class Action:

    def __init__(self, name: str, precond: 'Condition', effect: 'Effect'):
        self.name = name
        self.precond = precond
        self.effect = effect

    def __repr__(self):
        return colour(Colour.PURPLE, self.name)


class Condition(Dict):

    def __init__(self, initial_state: Dict[ComponentList, int], *args, **kw):
        super(Condition, self).__init__(initial_state, *args, **kw)


class Effect(Dict):

    def __init__(self, effects: Dict[int, Condition], *args, **kw):
        super(Effect, self).__init__(effects, *args, **kw)


class ActionList:

    IDLE = Action(
        name="Do Nothing",
        precond=Condition({}),
        effect=Effect({})
    )

    TOAST_BREAD = Action(
        name="Toast Bread",

        precond=Condition({IngredientList.BREAD: 1,
                           EquipmentList.TOASTER_SLOT: 1}),

        effect=Effect(
            {3: {ComponentList.TOAST: 1,
                 EquipmentList.TOASTER_SLOT: 1}}
        )
    )

    ASSEMBLE_SIMPLE_TOAST_SANDWICH = Action(
        name="Assemble Simple Toast Sandwich",
        precond=Condition({
            ComponentList.TOAST: 2,
            ComponentList.HAM: 1,
            ComponentList.CHEESE: 1
        }),
        effect=Effect({1: {ComponentList.SIMPLE_TOAST_SANDWICH: 1}})
    )

    FRY_EGG = Action(
        name="Fry Egg",
        precond=Condition({ComponentList.EGG: 1,
                           EquipmentList.PAN: 1}),
        effect=Effect({1: {EquipmentList.PAN: 1},
                       2: {ComponentList.FRIED_EGG: 1}})
    )


ACTIVE_ACTIONS = [v for v in ActionList.__dict__.values()
                  if isinstance(v, Action)
                  if v is not ActionList.IDLE]  # Except IDLE
