from cxsim.actions.action_restrictions import ActionRestriction
from cxsim.agents.item import Item
from cxsim.agents.tools.tool import Tool
from cxsim.agents.traits.memory.long_term_memory import LongTermMemory
from cxsim.agents.traits.inventory import Inventory
from cxsim.agents.traits.memory.working_memory import WorkingMemory

from copy import deepcopy
from abc import abstractmethod


def before_turn(func):
    setattr(func, "_before_turn", True)
    return func


def after_turn(func):
    setattr(func, "_after_turn", True)
    return func


class Agent:
    """
    Represents an individual agent in the simulation, encapsulating attributes, behaviors, tools, and interactions.

    Attributes:
        name (str): Name of the agent.
        id (int): Unique identifier for the agent, initialized by the environment class.
        x_pos, y_pos (int): Positional coordinates of the agent.
        color (tuple): RGB color representation of the agent that would be used in the GUI
        role: Role of the agent.
        observations (list): List of observations made by the agent.
        messages (list): Messages received or sent by the agent.
        params (dict): Parameters or settings specific to the agent.
        action_history (list): Record of past actions taken by the agent.
        action_restrictions, query_restrictions (dict): Restrictions on actions and queries.
        action_space, query_space (dict): Available actions and queries for the agent.
        system_prompt (str): Prompt or message from the system.
        inventory (Inventory): Inventory of items held by the agent.
        long_term_memory (LongTermMemory): Long-term memory storage of the agent.
        tools (dict): Tools or utilities available to the agent.
    """
    def __init__(
            self,
            name: str = "default"
    ):
        """
        Initialize an agent with a given name and default attributes.

        :param name: Name of the agent.
        """
        self.name = name
        self.id = None  # None, initialized before the first episode by the environment class
        self.x_pos = None
        self.y_pos = None
        self.color: tuple = (0, 0, 0)
        self.role = None

        self.action_queue = []

        # holds the observations for each artifact
        self.observations = []

        # holds messages
        self.messages = []

        # holds agent parameters
        self.params = {}

        # records past actions
        self.action_history = []

        # action restrictions
        self.action_restrictions = {}

        # action space
        self.action_space = {}

        self.backend = None
        self.environment = None

        # other
        self.goal = ""
        self.tasks = []

        self.inbox = []
        self.inventory = Inventory()

        # agent traits
        self.long_term_memory = LongTermMemory(100)
        self.working_memory = WorkingMemory(self)

        # agent tools
        self.tools = {}

        self.before_turn_methods = [
            getattr(self, method_name) for method_name in dir(self)
            if callable(getattr(self, method_name))
            and getattr(getattr(self, method_name), "_before_turn", False)
        ]

        self.after_turn_methods = [
            getattr(self, method_name) for method_name in dir(self)
            if callable(getattr(self, method_name))
            and getattr(getattr(self, method_name), "_after_turn", False)
        ]

    def add_tool(self, tool: Tool):
        """
        Add a tool to the agent's collection of tools.

        :param tool: Tool object to be added.
        :raises KeyError: If the tool is already present.
        """
        if tool.name in self.tools:
            raise KeyError("Tool is already in the agent")
        else:
            self.tools[tool.name] = tool

#    def add_message(self, role: str, content: str, function_name: str = None):
#        """Add a message to the agents messaging dictionary"""
#        if function_name:
#            self.messages.append({"role": role, "name": function_name, "content": content})
#        else:
#            self.messages.append({"role": role, "content": content})

    @abstractmethod
    def step(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    @abstractmethod
    def reset(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_action_space(self):
        return self.action_space

    def capital(self):
        return self.inventory["capital"]

    def display_inventory(self):
        return str({key: value for key, value in self.inventory.items()})

    def update_inventory(self):
        self.inventory = {key: len(value) for key, value in self.inventory.items()}

    def compile(self):
        pass

    def __isub__(self, other):
        if not isinstance(other, Item):
            raise Warning("Can only add an Item class to the Agent")
        elif other.name in self.inventory.keys():
            self.inventory[other.name].append(other)
            return self
        else:
            pass

    def add(self, item):
        if isinstance(item, ActionRestriction):
            if item.action in self.action_restrictions:
                self.action_restrictions[item.action].append(item.restriction_function)
            else:
                self.action_restrictions[item.action] = [item.restriction_function]

    @property
    def action_space_list(self) -> list:
        action_space = []
        for artifact, action_list in self.action_space.items():
            for action in action_list:
                action_space.append(action)

        return action_space

    def __iadd__(self, other: Item):
        if not isinstance(other, Item):
            raise Warning("Can only add an Item class to the Agent")
        elif other.name in self.inventory.keys():
            self.inventory[other.name].append(other)
            return self
        else:
            pass

    def copy(self):
        return deepcopy(self)

    def __getitem__(self, item):
        if item in self.inventory.keys():
            return self.inventory[item]

        # if item does not exist, assume they 0 of it
        return 0

    def __repr__(self):
        return str(self.name)

    def __setitem__(self, key, value):
        if key == "capital":
            self.capital = value
        elif key in self.inventory.keys():
            self.inventory[key] = value
        else:
            self.inventory[key] = value

    def get_inventory(self, item):
        return self.inventory.get_quantity(item)

    def values(self):
        return self.inventory.values()

    def display(self):
        return \
            f"""
-----------------------------
Agent: {self.name} 
capital {self.get_inventory("capital")}
-----------------------------"""
