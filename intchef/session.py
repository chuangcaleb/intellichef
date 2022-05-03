"""
The CookingSession class that handles each GOAP session.
"""


class CookingSession:
    """ An object to handle one entire cooking session. """

    def __init__(self):
        """Initializes a cooking session
        """

        self.time_elapsed = 0  # init: no time elapsed
        self.world_state = []  # init: empty world state

        # param to include washing equipment in final goal state?

    # Check for end of cycle

    def _check_end(self) -> bool:
        """ Check if cycle has reached an end condition """

        # end_condition is when (subset(world state) == goal state)
        end_condition = (
            False
        )

        return True if end_condition else False

    def run(self) -> bool:
        return self._check_end()

    # Step cycle

    # def step(self):
    #     """Step through one

    #     Returns:
    #     bool: If the game has ended
    #     """

    #     # Increment num_cycles
    #     self.time_elapsed += 1

    #     return self._check_end()
