"""
Definitions of every Component
"""
from .abstract import Component


class ComponentList:

    BREAD = Component("Bread", "slice")
    BUTTER = Component("Butter", "knob")
    HAM = Component("Ham", "slice")
    CHEESE = Component("Cheese", "slice")

    TOAST = Component("Toast", "slice")

    SIMPLE_TOAST_SANDWICH = Component(
        "Simple Toast Sandwich",
        counter="",
        # state="buttered",
        aggrg={
            TOAST: 2,
            HAM: 1,
            CHEESE: 1
        }
    )
