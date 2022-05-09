"""
Class definitions for Kitchen Resources
"""

from abc import ABC
from typing import List

from colours import Colour, colour


class KitchenResource(ABC):

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        """ Default representation without colour formatting"""
        # return colour(Colour.YELLOW, self.display_name)
        return self.display_name

    @property
    def display_name(self):

        def to_camel_case(str):
            words = str.split()
            if len(str) == 0:
                return str
            return ''.join(w.capitalize() for w in words)

        return to_camel_case(self.name)


class Chef(KitchenResource):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return colour(Colour.DARKCYAN, self.display_name)


class Equipment(KitchenResource):

    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return colour(Colour.BLUE, self.display_name)


class Food(KitchenResource):

    def __init__(
            self,
            name: str,
            counter: str,
            # state: str = None,
            aggrg: List['Food'] = None,
            quantity: int = 1,
    ):
        super().__init__(name)
        self.counter = counter
        self.quantity = quantity
        # self.state = state
        self.aggrg = aggrg

    def __repr__(self):
        if self.aggrg == None:
            return colour(Colour.YELLOW, self.display_name)
        else:
            return "{}({})".format(
                colour(Colour.YELLOW, self.display_name),
                self.aggrg
            )


class Recipe(KitchenResource):

    def __init__(
        self,
        goal_state: List[KitchenResource],
        initial_state: List[KitchenResource],
        name: str = None,
    ):

        if name:  # If name was set, set it as usual
            super().__init__(name)
        else:  # If name is unset, take the first & only goal state's comp name
            super().__init__(list(goal_state)[0].name)

        self.goal_state = goal_state
        self.ingredients = initial_state

    def __repr__(self):
        return colour(Colour.GREEN, self.display_name)

    def print_details(self):

        print(
            "\n########################################################################\n")
        print("Recipe for:", colour(Colour.GREEN, self.name))

        print("Goal State:", end=" ")
        print(self.goal_state)

        print("Ingredients:", end=" ")
        print(self.ingredients)
