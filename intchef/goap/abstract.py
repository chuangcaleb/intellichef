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
        return self.name.capitalize()


# WorldState = Set['States']
SubComponents = List['Component']


class Component(KitchenResource):

    def __init__(
            self,
            name: str,
            counter: str,
            # state: str = None,
            aggrg: SubComponents = None,
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
        name: str,
        ingredients: List[Component],
        goal_state: List[Component]
    ):
        super().__init__(name)
        self.ingredients = ingredients
        self.goal_state = goal_state

    def print_details(self):

        print()
        print("Recipe for:", green(self.name), "-----------------------------")

        print("Ingredients:", end=" ")
        print(self.ingredients)

        print("Goal State:", end=" ")
        print(self.goal_state)

    # def get_ingredients(self):
    #     return self.ingredients

    # def __repr__(self):
    #     return "Recipe({})".format(selef.name)
