"""
Definitions of every Component
"""
from intchef.goap.abstract import Chef, Component, Equipment


class ChefList:

    CHEF = Chef("Chef")


class EquipmentList:

    TOASTER_SLOT = Equipment("Toaster Slot")
    PAN = Equipment("Frying Pan")


class IngredientList:

    BREAD = Component("Bread", "slice")
    BUTTER = Component("Butter", "knob")
    HAM = Component("Ham", "slice")
    CHEESE = Component("Cheese", "slice")
    EGG = Component("Egg", "")


class ComponentList(IngredientList, ChefList, EquipmentList):

    TOAST = Component("Toast", "slice")

    SIMPLE_TOAST_SANDWICH = Component(
        "Simple Toast Sandwich",
        counter="",
        # state="buttered",
        # aggrg={
        #     TOAST: 2,
        #     HAM: 1,
        #     CHEESE: 1
        # }
    )

    FRIED_EGG = Component("Fried Egg", "")
