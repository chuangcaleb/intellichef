# Intellichef - Asynchronous Goal Oriented Action Planning

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
<!-- - [Contributing](../CONTRIBUTING.md) -->

## About <a name = "about"></a>

A coursework assignment for the COMP3004 Designing Intelligent Agents module.

> Following a recipe is one thing, but managing your kitchen resources is another!

### Basics of GOAP

GOAP stands for Goal Oriented Action Planning. It is remarkably similar to working in the kitchen.

To create a plan, GOAP-Agents need to know:

- The list of actions that can be taken
- The current world state
- The desired goal state

Actions are specified with:

- The precondition
- The postcondition (or, effect)
- The cost of the action

<!-- To describe world state, we define a set of world state atoms. Each atom has a tag, and a boolean value. -->

The planner will then be able to formulate a plan of actions that takes the world to the desired state, provided such a path exists. The plan formulated is guaranteed to be the lowest cost plan.

<!-- This is appropriate for the kitchen because there are so many different  -->

### Asynchronous Scheduling

If recipe steps were done sequentially, it would take forever! Actions can be simultaneously occurring in the background, like having a chicken in the oven while chopping up the garnish.

Another big factor to be considered is that some actions will have a delayed effect on the world state; for example, boiling spaghetti will require you to drain the water when it's done cooking, because delaying would make pasta become too soft.

This is handled by adding a temporal dimension to the world state. A pot can be in use from timestamps 10-15, and then again later at 30-35.

### Search Optimization

<!-- The A* algorithm can be used to search for the optimal sequence of recipe steps.

(and later on, optimal ingredients)

The forward cost to minimize would simply be the time elapsed. This may or may not count the time in between recipe steps.

A reasonable backwards heuristic function could be the amount of time an action takes, not counting the idle time in between -->

<!-- Since the search space is not very big, it is not necessary to run an informed search. -->

### Study

This study aims to see if there's a difference in optimizing total time elapsed vs total time spent active.

<!-- After working, some agents will also need to rest. -->
## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

Clone the repo

```shell
git clone https://github.com/chuangcaleb/intellichef
```

### Prerequisites

Run the following command to install the required python packages:

```python
pip install requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
