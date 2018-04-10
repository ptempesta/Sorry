# This class is meant to simulate a pawn for the Sorry! board game. For each
# player there are three pawns. A pawn has a color and a position. A pawn can
# have an index position on the common board, an index position on the "safety
# ramp," or simply be in either the start or end zone. If the pawn is either not
# on the common board or not on the "safety ramp," its position in that respect
# will be indicated by a -1.

# Peter Tempesta, 4/10/2018

class pawn:

    # Initially, color and position offset are negative. The position offset is
    # an integer used to help determine a pawns position in regard to another
    # pawn, particularly of another color.
    pawnColor = None
    pawnPosOffset = None

    # When not on the board, the common position and safety position are set
    # as -1. They are initialized as -1 as well, since a pawn does not start on
    # the common board or the safety ramp.
    pawnCommonPosition = -1
    pawnSafetyPosition = -1

    # Setting the color of a pawn also sets its offset.
    def setColorRed(self):
        self.pawnColor = "red"
        self.pawnPosOffset = 0
    def setColorBlue(self):
        self.pawnColor = "blue"
        self.pawnPosOffset = 15
    def setColorYellow(self):
        self.pawnColor = "yellow"
        self.pawnPosOffset = 30
    def setColorGreen(self):
        self.pawnColor = "green"
        self.pawnPosOffset = 45

    

# The following code is for testing purposes.
#testPawn = pawn
#print("Initial Values:")
#print(testPawn.pawnColor)
#print(testPawn.pawnPosOffset)
#print(testPawn.pawnCommonPosition)
#print(testPawn.pawnSafetyPosition)

#print("Red Pawn, No Offset:")
#testPawn.setColorRed(testPawn)
#print(testPawn.pawnColor)
#print(testPawn.pawnPosOffset)
#print("Blue Pawn, 15 Offset:")
#testPawn.setColorBlue(testPawn)
#print(testPawn.pawnColor)
#print(testPawn.pawnPosOffset)
