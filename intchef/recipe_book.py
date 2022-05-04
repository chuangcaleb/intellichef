from intchef.session import WorldState
from .goap.abstract import Component, Recipe
from .goap.components import ComponentList


class RecipeBook:

    TOAST = Recipe(
        goal_state=WorldState({
            ComponentList.TOAST: 1
        }),
        ingredients=WorldState({
            ComponentList.BREAD: 1
        })
    )

    SIMPLE_TOAST_SANDWICH = Recipe(
        goal_state=WorldState({
            ComponentList.SIMPLE_TOAST_SANDWICH: 1
        }),
        ingredients=WorldState({
            ComponentList.BREAD: 10,
            ComponentList.HAM: 1,
            ComponentList.CHEESE: 1
        })
    )
