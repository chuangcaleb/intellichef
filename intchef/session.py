

class CookingSession():
    """ An object to handle one session of cooking. """

    def __init__(self):
        """Initializes a cooking session

        Args:
        num_initial_units (int, optional): Number of initial units. Defaults to 3.
        """

        self.time_elapsed = 0
        # param to include washing equipment?

    # Check for end of cycle

    def _check_end(self):
        """ Check if cycle has reached an end condition """

        # end_condition is when (subset(world state) == goal state)
        end_condition = (
            False
        )

        return True if end_condition else False

    def run(self):
        return 0

    # Step cycle

    # def step(self):
    #     """Step through one

    #     Returns:
    #     bool: If the game has ended
    #     """

    #     # Run through units
    #     current_step_units = self.units.copy()
    #     for unit in current_step_units:

    #         unit.step()

    #         if unit.state == UnitStates.DEAD:
    #             self.units.remove(unit)

    #     # Increment num_cycles
    #     self.time_elapsed += 1

    #     return self._check_end()
