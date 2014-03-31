__author__ = 'David'

"""Coach class"""

class Coach:
    def __init__(self, coachName, coachRatings):
        self.name = coachName
        """ratings for coaching position, ordered by
           [QB, RB/FB, WR, TE, OL, DL, LB, CB/S, ST]"""
        self.ratings = coachRatings