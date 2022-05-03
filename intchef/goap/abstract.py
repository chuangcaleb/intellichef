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
        return "{}".format(
            # type(self).__name__,
            yellow(self.display_name)
        )

    @property
    def display_name(self):

        def to_camel_case(str):
            # s = text.replace("-", " ").replace("_", " ")
            words = str.split()
            if len(str) == 0:
                return str
            return ''.join(w.capitalize() for w in words)

        return to_camel_case(self.name)


# WorldState = Set['States']
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
        # return "{}({}({}))".format(
        if self.aggrg == None:
            return "{}".format(
                # type(self).__name__,
                yellow(self.display_name)
            )
        else:
            return "{}({})".format(
                # type(self).__name__,
                yellow(self.display_name),
                # pp.pformat(self.aggrg)
                self.aggrg
            )


# class Ingredient(Component):

#     def __init__(self, name: str, counter: str):
#         super().__init__(name, counter)


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

        # XX If no name, just take the first and only goal state's comp name
        if name == None:
            # If only one item in goal state, take its name as recipe name
            # if len(goal_state) == 1:
            extracted_name = list(goal_state)[0].name
        else:
            extracted_name = name
        super().__init__(extracted_name)

        self.goal_state = goal_state
        self.ingredients = ingredients

    def print_details(self):

        print()
        print("Recipe for:", green(self.name), "#############################")

        print("Goal State:", end=" ")
        print(self.goal_state)

        print("Ingredients:", end=" ")
        print(self.ingredients)
