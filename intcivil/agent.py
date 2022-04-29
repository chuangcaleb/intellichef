import enum


class AgentStates(enum.Enum):
    IDLE = 0
    BUSY = 1


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

        # check death


if __name__ == "__main__":
    agent_1 = Agent()
    Agent.agent_count()
    agent_2 = Agent()
    print(agent_2.id)
    agent_3 = Agent()
