# This class is meant to simulate a pawn for the Sorry! board game.

# Peter Tempesta, 4/10/2018

class pawn:

    def __init__(self, colorChoice):

        self.color = colorChoice
        if self.color == "red":
            self.colorCommonOffset = 0
        elif self.color == "blue":
            self.colorCommonOffset = 15
        elif self.color == "yellow":
            self.colorCommonOffset = 30
        elif self.color == "green":
            self.colorCommonOffset = 45

        self.score = 0
        self.commonBoardPosition = None
        self.safetyRampPosition = None
        self.flagInStartZone()

    # These are a series of flagging methods to determine where a particular
    # pawn is one the board, namely whether it is in one of the 4 general areas
    # it could be in.
    
    def flagInStartZone(self):
        self.inStartZone = True
        self.onCommonBoard = False
        self.onSafetyRamp = False
        self.inEndZone = False

    def flagOnCommonBoard(self):
        self.inStartZone = False
        self.onCommonBoard = True
        self.onSafetyRamp = False
        self.inEndZone = False
        
    def flagOnSafetyRamp(self):
        self.inStartZone = False
        self.onCommonBoard = False
        self.onSafetyRamp = True
        self.inEndZone = False
        
    def flagInEndZone(self):
        self.inStartZone = False
        self.onCommonBoard = False
        self.onSafetyRamp = False
        self.inEndZone = True

    # The following methods update the score of a pawn, whether it moves from
    # one area to another in general or it is reset to its starting zone.

    def scorePosUpdate(self, moveValue):

        # Case 1: moving a pawn onto the common board squares.
        if self.score + moveValue in range(1,60):
            self.score += moveValue
            self.commonBoardPosition = self.score + self.colorCommonOffset
            if self.commonBoardPosition > 60:
                self.commonBoardPosition -= 60
            self.safetyRampPosition = None
            self.flagOnCommonBoard()

        # Case 2: moving a pawn onto the safety ramp squares.
        elif self.score + moveValue in range(60,65):
            self.score += moveValue
            self.commonBoardPosition = None
            self.safetyRampPosition = self.score - 60
            self.flagOnSafetyRamp()

        # Case 3: moving a pawn onto its safety zone.
        elif self.score + moveValue == 65:
            self.score += moveValue
            self.commonBoardPosition = None
            self.safetyRampPosition = None
            self.flagInEndZone()

    # Case 4: reset a pawn to its starting position.
    def scorePosReset(self):
        self.score = 0
        self.commonBoardPosition = None
        self.safetyRampPosition = None
        self.flagInStartZone()
