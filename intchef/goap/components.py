"""
Definitions of every Component
"""
from .abstract import Component


class Ingredients():

    BREAD = Component("Bread", "slice")


class Components(Ingredients):

    TOAST = Component("toast", "slice")
    BUTTER_TOAST = Component(
        "Butter Toast",
        "slice",
        # state="buttered",
    )
