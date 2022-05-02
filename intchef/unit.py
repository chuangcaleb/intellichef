from intchef import constants as const
import enum


class UnitStates(enum.Enum):
    IDLE = 0
    BUSY = 1
    DEAD = 2


class Unit:
    '''Represents an Unit.'''

    # A class variable, counting the number of units
    population = 0

    def __init__(self):
        '''Initializes the Unit.'''

        # Increment population and assign id
        Unit.population += 1
        self.id = Unit.population
        # print('Initializing Unit #{}'.format(self.id))

        # Other stats
        self.age = 0
        # self.skill = {}
        self.state = UnitStates.IDLE

    def __repr__(self):
        return 'Unit #{:d}'.format(self.id)

    def step(self):
        self.grow_older()

    def grow_older(self):
        """ Increment age """
        self.age += 1
        if self.is_max_age():
            self.state = UnitStates.DEAD

    def is_max_age(self):
        """ Check if age has exceeded AGE_CEILING """
        return True if self.age >= const.AGE_CEILING else False
