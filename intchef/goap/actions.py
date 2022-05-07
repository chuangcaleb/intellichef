"""
Defines all GOAP actions
"""

from typing import Dict

from colours import Colour, colour
from intchef.goap.abstract import KitchenResource
from intchef.goap.components import ComponentList, EquipmentList, IngredientList


class Action:

    def __init__(self, name: str, precond: 'Condition', effect: 'Effect'):
        self.name = name
        self.precond = precond
        self.effect = effect

    def __repr__(self):
        return colour(Colour.PURPLE, self.name)


class Condition(Dict):

    def __init__(self, initial_state: Dict[KitchenResource, int], *args, **kw):
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

        precond=Condition({
            # ChefList.CHEF: 1,
            EquipmentList.TOASTER_SLOT: 1,
            IngredientList.BREAD: 1
        }),

        effect=Effect({
            # 1: {ChefList.CHEF: 1},
            3: {ComponentList.TOAST: 1,
                EquipmentList.TOASTER_SLOT: 1}}
        )
    )

    ASSEMBLE_SIMPLE_TOAST_SANDWICH = Action(
        name="Assemble Simple Toast Sandwich",
        precond=Condition({
            # ChefList.CHEF: 1,
            IngredientList.HAM: 1,
            IngredientList.CHEESE: 1,
            ComponentList.TOAST: 2
        }),
        effect=Effect({1: {
            # ChefList.CHEF: 1,
            ComponentList.SIMPLE_TOAST_SANDWICH: 1}})
    )

    WASH_RICE = Action(
        name="Wash Rice",
        precond=Condition({
            IngredientList.RAW_RICE: 1,
            EquipmentList.POT: 1
        }),
        effect=Effect({
            2: {ComponentList.WASHED_RICE: 1,
                EquipmentList.POT: 1}
        })
    )

    COOK_RICE = Action(
        name="Cook Rice",
        precond=Condition({
            ComponentList.WASHED_RICE: 1,
            EquipmentList.RICE_COOKER: 1
        }),
        effect=Effect({
            10: {ComponentList.RICE: 1, EquipmentList.RICE_COOKER: 1}
        })
    )

    FRY_EGG = Action(
        name="Fry Egg",
        precond=Condition({
            # ChefList.CHEF: 1,
            EquipmentList.PAN: 1,
            IngredientList.EGG: 1
        }),
        effect=Effect({2: {
            # ChefList.CHEF: 1,
            EquipmentList.PAN: 1,
            ComponentList.FRIED_EGG: 1
        }})
    )

    DEBONE_THIGH = Action(
        name="Debone Thigh",
        precond=Condition({
            # ChefList.CHEF: 1,
            IngredientList.RAW_CHICKEN_THIGH: 1,
            EquipmentList.KNIFE: 1,
            EquipmentList.BOARD: 1
        }),
        effect=Effect({1: {
            # ChefList.CHEF: 1,
            ComponentList.RAW_CHICKEN_FILLET: 1,
            EquipmentList.KNIFE: 1,
            EquipmentList.BOARD: 1
        }})
    )

    FRY_FILLET = Action(
        name="Fry Chicken Fillet",
        precond=Condition({
            # ChefList.CHEF: 1,
            ComponentList.RAW_CHICKEN_FILLET: 1,
            EquipmentList.PAN: 1
        }),
        effect=Effect({3: {
            # ChefList.CHEF: 1,
            ComponentList.FRIED_CHICKEN_FILLET: 1,
            EquipmentList.PAN: 1
        }})
    )


ALL_ACTIONS = [v for v in ActionList.__dict__.values()
               if isinstance(v, Action)]
