"""
Definitions of every Component
"""

from .abstract import Component


class Ingredients:

    BREAD = Component("bread", "slice")


class Components:

    TOAST = Component("toast", "slice")
    BUTTER_TOAST = Component(
        "butter toast",
        "slice",
        # state="buttered",
    )
