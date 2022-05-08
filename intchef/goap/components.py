"""
Definitions of every Food
"""
from intchef.goap.abstract import Chef, Food, Equipment


class ChefList:

    CHEF = Chef("Chef")


class EquipmentList:

    TOASTER_SLOT = Equipment("Toaster Slot")
    PAN = Equipment("Frying Pan")
    KNIFE = Equipment("Knife")
    BOARD = Equipment("Chopping Board")
    POT = Equipment("Pot")
    RICE_COOKER = Equipment("Rice Cooker")


class IngredientList:

    BREAD = Food("Bread", "slice")
    BUTTER = Food("Butter", "knob")
    HAM = Food("Ham", "slice")
    CHEESE = Food("Cheese", "slice")
    EGG = Food("Egg", "")
    RAW_CHICKEN_THIGH = Food("Raw Chicken Thigh", "")
    RAW_RICE = Food("Raw Rice", "")


class ComponentList(IngredientList, ChefList, EquipmentList):

    TOAST = Food("Toast", "slice")
    RICE = Food("Rice", "")

    SIMPLE_TOAST_SANDWICH = Food(
        "Simple Toast Sandwich",
        counter="",
        # state="buttered",
        # aggrg={
        #     TOAST: 2,
        #     HAM: 1,
        #     CHEESE: 1
        # }
    )

    FRIED_EGG = Food("Fried Egg", "")

    WASHED_RICE = Food("Washed Rice", "")
    RICE = Food("Rice", "")

    RAW_CHICKEN_FILLET = Food("Raw Chicken Fillet", "")

    FRIED_CHICKEN_FILLET = Food("Fried Chicken Fillet", "")
