import pawn

# This class is meant to simulate a player for the Sorry! board game.

# Peter Tempesta, 4/10/2018

class player:

    def __init__(self, colorChoice):
        self.playerColor = colorChoice
        self.pawnList = []
        self.pawnScores = []    # These are the scores for individual pawns.
        for i in range(3):
            self.pawnList.append(pawn.pawn(colorChoice))
            self.pawnScores.append(0)

    # This method is used to ensure that the positions and pawns of all players
    # are kept up to date elsewhere in the code.
    
    def updatePawnScores(self):
        self.pawnScores = []
        for i in range(3):
            self.pawnScores.append(self.pawnList[i].score)

    # These methods will set whether a player is a user or a computer as well as
    # set the skill and disposition of computer players. It simply sets flags.

    def setUserPlayerFlag(self):
        self.userPlayerBool = True
        self.smartBool = False
        self.meanBool = False

    def setSmartMeanCompFlag(self):
        self.userPlayerBool = False
        self.smartBool = True
        self.meanBool = True

    def setSmartNiceCompFlag(self):
        self.userPlayerBool = False
        self.smartBool = True
        self.meanBool = False

    def setDumbMeanCompFlag(self):
        self.userPlayerBool = False
        self.smartBool = False
        self.meanBool = True

    def setDumbNiceCompFlag(self):
        self.userPlayerBool = False
        self.smartBool = False
        self.meanBool = False

# A simple testing method.
def testBools():
    testPlayer = player("red")
    testPlayer.setUserPlayerFlag()
    print(testPlayer.userPlayerBool)
#testBools()
        
