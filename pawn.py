# This class is meant to simulate a pawn for the Sorry! board game. For each
# player there are three pawns. A pawn has a color and a position. A pawn can
# have an index position on the common board, an index position on the "safety
# ramp," or simply be in either the start or end zone. If the pawn is either not
# on the common board or not on the "safety ramp," its position in that respect
# will be indicated by a -1.

# Peter Tempesta, 4/10/2018

class pawn:

    # This class has a modified constructor which needs a string representing
    # a color, so that the pawns may be colored accordingly.
    def __init__(self, colorChoice):

        # Initially, color and position offset are None. The position offset
        # is an integer used to help determine a pawns position in regard to
        # another pawn, particularly of another color.
        self.pawnColor = None
        self.pawnPosOffset = None

        # When not on the board, the common position and safety position are set
        # as -1. They are initialized as -1 as well, since a pawn does not start
        # on the common board or the safety ramp.
        self.pawnCommonPosition = -1
        self.pawnSafetyPosition = -1

        # The position offset of the pawn depends on its color.
        if colorChoice == "red":
            self.pawnColor = "red"
            self.pawnPosOffset = 30
        elif colorChoice == "blue":
            self.pawnColor = "blue"
            self.pawnPosOffset = 30
        elif colorChoice == "yellow":
            self.pawnColor = "yellow"
            self.pawnPosOffset = 30
        elif colorChoice == "green":
            self.pawnColor = "green"
            self.pawnPosOffset = 30
