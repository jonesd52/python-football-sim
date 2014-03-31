__author__ = 'David'

"""The Player class, which sets up a basic player"""

class Player:
    def __init__(self, playerName, playerPosition):
        self.name = playerName
        self.position = playerPosition

    def getName(self):
        return self.name

    """May want to make this an array of positions, to allow players to play
    at multiple positions with no penalty."""
    def getPosition(self):
        return self.position

