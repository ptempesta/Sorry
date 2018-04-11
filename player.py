import pawn

# This class is meant to simulate a player for the Sorry! board game. A player
# has three pawns, a starting zone for his or her pawns, an ending zone for his
# or her pawns, and a "safety ramp" for these pawns as well.

# Peter Tempesta, 4/10/2018

class player:

    def __init__(self, colorChoice):
        self.pawn1 = pawn.pawn(colorChoice)
        self.pawn2 = pawn.pawn(colorChoice)
        self.pawn3 = pawn.pawn(colorChoice)

        # The Starting Zone is a list from which pawns may be pushed or popped.
        # By default (initially) the Starting Zone is populated with all three
        # of the player's pawns.
        self.startZone = []
        self.startZone.append(self.pawn1)
        self.startZone.append(self.pawn2)
        self.startZone.append(self.pawn3)

        # The Ending Zone is a list to which pawns may be pushed. If all of the
        # player's pawns end up in the Ending Zone, then that player wins.
        self.endZone = []
