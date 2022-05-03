"""
Definitions of every Component
"""
from .abstract import Component


class Ingredients():

    BREAD = Component("Bread", "slice")
    BUTTER = Component("Butter", "knob")


class Components(Ingredients):

    TOAST = Component("Toast", "slice")
    BUTTER_TOAST = Component(
        "Butter Toast",
        "slice",
        # state="buttered",
        aggrg=[Ingredients.BREAD, Ingredients.BUTTER]
    )
