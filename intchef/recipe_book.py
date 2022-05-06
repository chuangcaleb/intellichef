from .goap.world import WorldStateFrame
from .goap.abstract import Recipe
from .goap.components import ComponentList, EquipmentList, IngredientList


class RecipeBook:

    TOAST = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.TOAST: 1
        }),
        initial_state=WorldStateFrame({
            IngredientList.BREAD: 1,
            EquipmentList.TOASTER: 1
        })
    )

    SIMPLE_TOAST_SANDWICH = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.SIMPLE_TOAST_SANDWICH: 1
        }),
        initial_state=WorldStateFrame({
            IngredientList.BREAD: 3,
            IngredientList.HAM: 1,
            IngredientList.CHEESE: 1
        })
    )

    FRIED_EGG = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.FRIED_EGG: 1
        }),
        initial_state=WorldStateFrame({
            IngredientList.EGG: 1,
            EquipmentList.PAN: 1
        })
    )
