from intchef.session import WorldState
from .goap.abstract import Component, Recipe
from .goap.components import ComponentList


class RecipeBook:

    TOAST = Recipe(
        name="Toast",
        ingredients=WorldState({
            ComponentList.BREAD: 1
        }),
        goal_state=WorldState({
            ComponentList.TOAST: 1
        })
    )

    SIMPLE_TOAST_SANDWICH = Recipe(
        name="Toast Sandwich",
        ingredients=WorldState({
            ComponentList.BREAD: 2,
            ComponentList.HAM: 1,
            ComponentList.CHEESE: 1
        }),
        goal_state=WorldState({
            ComponentList.SIMPLE_TOAST_SANDWICH: 1
        })
    )
