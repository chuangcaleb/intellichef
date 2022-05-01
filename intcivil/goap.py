import enum
from typing import List


class Action:

    def __init__(self, name: str, precon: List[str], effect: List[str]):
        self.name = name
        self.precon = precon
        self.effect = effect

    def __repr__(self):
        return(self.name)


if __name__ == "__main__":

    # a = Action('Chop Wood', [''])
    # The previous 2 lines can also be written as
    # Person('Swaroop').say_hi()
    pass


class IntelligentExpert:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if IntelligentExpert.__instance == None:
            IntelligentExpert()
        return IntelligentExpert.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if IntelligentExpert.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            IntelligentExpert.__instance = self


class RandomAgent:
    pass


s = IntelligentExpert()
print(s)
