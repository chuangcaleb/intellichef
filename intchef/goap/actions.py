""" 
Defines all GOAP actions
"""


class Action:
    def __init__(
        self,
        name: str,
        precond,
        effect,
        time_elapsed
    ):
        self.name = name,
        self.precond = precond,
        self.effect = effect
        self.time_elapsed = time_elapsed


ACTIONS = {
    Action(
        "Toast bread",
        precond=[]
    )
}
