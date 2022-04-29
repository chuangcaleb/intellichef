import enum


class AgentStates(enum.Enum):
    IDLE = 0
    BUSY = 1


AGE_CEILING = 80


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

    def grow_older(self):
        """ Increment age """
        self.age += 1

    def is_max_age(self):
        """ Check if age has exceeded AGE_CEILING """
        return True if self.age >= AGE_CEILING else False
