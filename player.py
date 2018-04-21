import pawn

# This class is meant to simulate a player for the Sorry! board game.

# Peter Tempesta, 4/10/2018

class player:

    def __init__(self, colorChoice):
        self.playerColor = colorChoice
        self.pawnList = []
        self.pawnScores = []
        for i in range(3):
            self.pawnList.append(pawn.pawn(colorChoice))
            self.pawnScores.append(0)

    def updatePawnScores(self):
        self.pawnScores = []
        for i in range(3):
            self.pawnScores.append(self.pawnList[i].score)
