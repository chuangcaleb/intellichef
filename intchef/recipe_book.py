from .goap.world import WorldStateFrame
from .goap.abstract import Recipe
from .goap.components import ComponentList


class RecipeBook:

    TOAST = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.TOAST: 1
        }),
        ingredients=WorldStateFrame({
            ComponentList.BREAD: 1
        })
    )

    SIMPLE_TOAST_SANDWICH = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.SIMPLE_TOAST_SANDWICH: 1
        }),
        ingredients=WorldStateFrame({
            ComponentList.BREAD: 3,
            ComponentList.HAM: 1,
            ComponentList.CHEESE: 1
        })
    )

    FRIED_EGG = Recipe(
        goal_state=WorldStateFrame({
            ComponentList.FRIED_EGG: 1
        }),
        ingredients=WorldStateFrame({
            ComponentList.EGG: 1
        })
    )
