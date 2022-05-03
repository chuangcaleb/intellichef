from intchef.session import WorldState
from .goap.abstract import Recipe
from .goap.components import Components, Ingredients


class RecipeBook:

    TOAST = Recipe(
        name='Toast',
        ingredients=WorldState({
            Components.BREAD: 1
        }),
        goal_state=WorldState({
            Components.TOAST: 1
        })
    )
