""" 
Contains the class definitions
"""

from abc import ABC, abstractmethod
from typing import List

from .colors import green, yellow


class KitchenResource(ABC):

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return yellow(self.display_name)

    @property
    def display_name(self):

        def to_camel_case(str):
            words = str.split()
            if len(str) == 0:
                return str
            return ''.join(w.capitalize() for w in words)

        return to_camel_case(self.name)


class Component(KitchenResource):

    def __init__(
            self,
            name: str,
            counter: str,
            # state: str = None,
            aggrg: List['Component'] = None,
            quantity: int = 1,
    ):
        super().__init__(name)
        self.counter = counter
        self.quantity = quantity
        # self.state = state
        self.aggrg = aggrg

    def __repr__(self):
        if self.aggrg == None:
            return yellow(self.display_name)
        else:
            return "{}({})".format(
                yellow(self.display_name),
                self.aggrg
            )


class Equipment(KitchenResource):

    def __init__(self, name: str):
        super().__init__(name)


class Recipe(KitchenResource):

    def __init__(
        self,
        goal_state: List[Component],
        ingredients: List[Component],
        name: str = None,
    ):

        if name:  # If name was set, set it as usual
            super().__init__(name)
        else:  # If name is unset, take the first & only goal state's comp name
            super().__init__(list(goal_state)[0].name)

        self.goal_state = goal_state
        self.ingredients = ingredients

    def print_details(self):

        print()
        print("Recipe for:", green(self.name), "#############################")

        print("Goal State:", end=" ")
        print(self.goal_state)

        print("Ingredients:", end=" ")
        print(self.ingredients)
