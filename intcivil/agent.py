from intcivil import constants as const
import enum


class AgentStates(enum.Enum):
    IDLE = 0
    BUSY = 1
    DEAD = 2


class Agent:
    '''Represents an agent.'''

    # A class variable, counting the number of agents
    population = 0

    def __init__(self):
        '''Initializes the agent.'''

        # Increment population and assign id
        Agent.population += 1
        self.id = Agent.population
        # print('Initializing Agent #{}'.format(self.id))

        # Other stats
        self.age = 0
        # self.skill = {}
        self.state = AgentStates.IDLE

    def __repr__(self):
        return 'Agent #{:d}'.format(self.id)

    def step(self):
        self.grow_older()

    def grow_older(self):
        """ Increment age """
        self.age += 1
        if self.is_max_age():
            self.state = AgentStates.DEAD

    def is_max_age(self):
        """ Check if age has exceeded AGE_CEILING """
        return True if self.age >= const.AGE_CEILING else False
