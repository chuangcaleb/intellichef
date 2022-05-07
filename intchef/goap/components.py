"""
Definitions of every Component
"""
from intchef.goap.abstract import Chef, Component, Equipment


class ChefList:

    CHEF = Chef("Chef")


class EquipmentList:

    TOASTER_SLOT = Equipment("Toaster Slot")
    PAN = Equipment("Frying Pan")
    KNIFE = Equipment("Knife")
    BOARD = Equipment("Chopping Board")


class IngredientList:

    BREAD = Component("Bread", "slice")
    BUTTER = Component("Butter", "knob")
    HAM = Component("Ham", "slice")
    CHEESE = Component("Cheese", "slice")
    EGG = Component("Egg", "")
    RAW_CHICKEN_THIGH = Component("Chicken Thigh", "")


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

    RAW_CHICKEN_FILLET = Component("Raw Chicken Fillet", "")

    FRIED_CHICKEN_FILLET = Component("Fried Chicken Fillet", "")
