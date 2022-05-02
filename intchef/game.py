from intchef.unit import Unit, UnitStates


class CivilGame():
    """ The Game object. """

    def __init__(self, num_initial_units: int = 3, max_cycles: int = 3000):
        """Initializes a game

        Args:
        num_initial_units (int, optional): Number of initial units. Defaults to 3.
        max_cycles (int, optional): Number of cycles before game ends. Defaults to 3000.
        """

        self.num_houses = 0
        self.num_cycles = 0
        self.max_cycles = max_cycles
        self.blackboard = Blackboard()

        # Init initial units
        self.units = set()
        for _ in range(num_initial_units):
            self.units.add(Unit())

    # Check for end of cycle
    def _check_end(self):
        """ Check if cycle has reached an end condition """

        # maximum cycles
        # no more units
        end_condition = (
                        (self.num_cycles >= self.max_cycles) or
                        (len(self.units) == 0)
        )

        return True if end_condition else False

    # Step cycle

    def step(self):
        """Step through one game cycle

        Returns:
        int: Current number of cycles
        bool: If the game has ended
        """

        # Run through units
        current_step_units = self.units.copy()
        for unit in current_step_units:

            unit.step()

            if unit.state == UnitStates.DEAD:
                self.units.remove(unit)

        # Increment num_cycles
        self.num_cycles += 1

        return self._check_end()
