

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
        self.num_initial_agents = num_initial_agents
        self.max_cycles = max_cycles

        # Init initial agents

    # Step cycle
    def step(self):
        """Step through one game cycle

        Returns:
        int: Current number of cycles
        bool: If the game has ended
        """
        self.num_cycles += 1
        return self.num_cycles, self.check_end()

    # Check for end of cycle
    def check_end(self):
        return True if self.num_cycles >= self.max_cycles else False
