from intcivil.agent import Agent, AgentStates
from intcivil.blackboard import Blackboard


class CivilGame():
    """ The Game object. """

    def __init__(self, num_initial_agents: int = 3, max_cycles: int = 3000):
        """Initializes a game

        Args:
        num_initial_agents (int, optional): Number of Initial Agents. Defaults to 3.
        max_cycles (int, optional): Number of cycles before game ends. Defaults to 3000.
        """

        self.num_houses = 0
        self.num_cycles = 0
        self.max_cycles = max_cycles
        self.blackboard = Blackboard()

        # Init initial agents
        self.agents = set()
        for _ in range(num_initial_agents):
            self.agents.add(Agent())

    # Check for end of cycle
    def _check_end(self):
        """ Check if cycle has reached max_cycles """

        end_condition = (self.num_cycles >= self.max_cycles) or (
            len(self.agents) == 0)

        return True if end_condition else False

    # Step cycle

    def step(self):
        """Step through one game cycle

        Returns:
        int: Current number of cycles
        bool: If the game has ended
        """

        # Run through agents
        current_step_agents = self.agents.copy()
        for agent in current_step_agents:

            agent.step()

            if agent.state == AgentStates.DEAD:
                self.agents.remove(agent)

        # Increment num_cycles
        self.num_cycles += 1

        return self._check_end()
