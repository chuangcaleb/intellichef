""" 
Contains the class definitions
"""
import pprint
from abc import ABC, abstractmethod
from typing import List, Set

pp = pprint.PrettyPrinter(width=10)


class KitchenResource(ABC):

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "{}".format(
            # type(self).__name__,
            self.display_name
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
        return "{}({})".format(
            # type(self).__name__,
            self.display_name,
            pp.pformat(self.aggrg)
        )

    # def prepr(self):
    #     return "{}({})".format(
    #         # type(self).__name__,
    #         self.display_name,
    #         pp.pformat(self.aggrg)
    #     )


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
        print("Recipe for:", self.name)

        print("Ingredients:", end=" ")
        print(self.ingredients)

        print("Goal State:", end=" ")
        print(self.goal_state)

    # def __repr__(self):
    #     return "Recipe({})".format(selef.name)
