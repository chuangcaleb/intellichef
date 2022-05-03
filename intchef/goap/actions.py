""" 
Defines all GOAP actions
"""


from .colors import red
from .components import Components, Ingredients


class Action:

    def __init__(self, name, precond, effect, time_elapsed):
        self.name = name
        self.precond = precond
        self.effect = effect
        self.time_elapsed = time_elapsed

    def __repr__(self):
        return red(self.name)


ALL_ACTIONS = {
    Action(
        name="Toast Bread",
        precond={Ingredients.BREAD: 1},
        effect={Components.TOAST: 1},
        time_elapsed=4,
    )
}
