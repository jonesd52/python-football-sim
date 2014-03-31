__author__ = 'David'

"""The Player class, which sets up a basic player"""

class Player:
    def __init__(self, playerName, playerPosition):
        self.name = playerName
        """May want to use this as an array of positions, to allow players to play
           at multiple positions with no penalty."""
        self.position = playerPosition

