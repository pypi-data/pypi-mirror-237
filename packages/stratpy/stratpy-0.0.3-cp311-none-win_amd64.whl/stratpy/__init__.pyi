from stratpy.stratpy import *

class Game:
    """
    The main class representing the game model.
    """
    def __new__(cls, title: str, player_number: int, gametype: Type) -> Variable: ...
    """
    :param title: optional title of the game, used when displaying the game
    :param player_number: the amount of players in the game (default: 2)
    :param gametype: optional parameter for the type of game. Either Type.Normal or Type.Extensive
    """

class Decision:
    """
    Class representing the decision nodes of a player.
    """
    def __new__(cls, player: Player, name: str) -> Decision: ...
    """
    :param player: the player who performs the action
    :param name: the name of the decision
    """

    def add_node(self, other: Decision) -> Decision: ...
    """
    Adds a new decision node as a child

    :param other: the decidion node to be added as a child
    :return: a reference to self for chaining further calls
    """
    def add_nodes(self, *args: Decision) -> Decision: ...
    """
    Adds a variable amount of new decision nodes as a child.

    :param args: the decidion noded to be added as a child seperating by commas ','
    :return: a reference to self for chaining further calls
    """

class Player:
    """
    Class representing players of a game.
    """
    def __new__(cls, name: str) -> Player: ...
    """
    :param name: the name of the player
    """

class Variable:
    """
    Class representing a variable utility of a player.
    """
    def __new__(cls, name: str) -> Variable: ...
    """
    :param name: the display name of the variable
    """
