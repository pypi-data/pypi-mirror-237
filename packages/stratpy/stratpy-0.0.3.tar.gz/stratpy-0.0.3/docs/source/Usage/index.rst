Usage
=====

.. _installation:

Installation
------------

To use stratpy, first install it using pip:

.. code-block:: console

   $ pip install stratpy

Creating games
----------------

To create a new game use the ``Game()`` constructor:

.. autofunction:: statpy.Game()

| Optional parameters:
| ``title:`` title of the game which will be used during export.
| ``players:`` number of players in the game (default is 2)
| ``gametype:`` The type of game you want to model. Either Type.Normal for normal form games
| displayed in a matrix or Type.Extensive for extensive form games using tree structures.

Example:

>>> from stratpy import *
>>> my_game = Game(title="My Game", players=2, gametype=Type.Normal)
>>> game2 = Game("Prisoner's Dilemma")


Players
-------
| When the game is created the amount of players specified (default 2) are created as a vector in the game object.
| You can access these players with ``my_game.player[1]``

| ``my_game.player[0]`` is reserved for Nature.
| Player 1 is thus: ``my_game.player[1]`` and
| Player 2 is:      ``my_game.player[2]``

these references can also be store in variables for convenience:

>>> nature = game.player[0]
>>> p1 = game.player[1]
>>> p2 = game.player[2]

Further names can be set using the names field:

>>> p1.name = "Japan"
>>> game.player[2].name = "South Korea"


Decision Nodes
---------------
Decision nodes are created with the Decision(player, name) constructor:

.. autofunction:: statpy.Decision(player, name)

| parameters:
| ``player:`` The player the decision belongs to
| ``name:`` the name of the decision (used when displaying the game)

Example:

>>> d1 = Decision(p1, "Commit")
>>> d2 = Decision(game.player[2], "Renege")

Variables
---------

.. autofunction:: statpy.Variable()
To create variables to be used for the players utility, use the ``Variable()`` constructor.

| Variables require a name parameter used when displaying the payout.
| ``name:`` name of the variable as a string (e.x. "X")

Preference between variable utility can be ordered using the '>' and '==' operators.

Example:

>>> a = Variable("A")
>>> b = Variable("B")
>>> c = Variable("C")
>>> a > b == c

This results in players preferring a over b and c, and being indifferent to b and c.

