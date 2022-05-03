from .goap.abstract import Recipe
from .goap.components import Components, Ingredients


class RecipeBook:

    TOAST = Recipe(
        name='Toast',
        ingredients=[Components.BUTTER_TOAST],
        goal_state=[Components.BUTTER_TOAST]
    )
