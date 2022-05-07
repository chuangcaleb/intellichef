from intchef.goap.world import WorldStateFrame
from intchef.goap.abstract import Recipe
from intchef.goap.components import ChefList, ComponentList, EquipmentList, IngredientList


class RecipeBook:

    TOAST = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.TOAST: 1
        }),
        initial_state=WorldStateFrame({
            ChefList.CHEF: 1,
            EquipmentList.TOASTER_SLOT: 1,
            IngredientList.BREAD: 1
        })
    )

    SIMPLE_TOAST_SANDWICH = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.SIMPLE_TOAST_SANDWICH: 1
        }),
        initial_state=WorldStateFrame({
            ChefList.CHEF: 1,
            EquipmentList.TOASTER_SLOT: 2,
            IngredientList.BREAD: 2,
            IngredientList.HAM: 1,
            IngredientList.CHEESE: 1
        })
    )

    FRIED_EGG = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.FRIED_EGG: 1
        }),
        initial_state=WorldStateFrame({
            ChefList.CHEF: 1,
            EquipmentList.PAN: 1,
            IngredientList.EGG: 1,
        })
    )
