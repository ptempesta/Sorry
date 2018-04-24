import deck
import player

# This class is meant to simulate the board for the Sorry! board game. The board
# class contains between two to four total players upon initialization.

# Peter Tempesta, 4/11/2018

class board:

    # Note: sample parameters for constructor:
    # sampleBoard("red", 3, True, False, True, True)
    # This indicates that the user player is red, the first computer player is
    # skilled and nice, and the second computer player is skilled and mean.

    def __init__(self, playerColorChoice, enemyPlayerCount, comp1Skill = None, comp1Disp = None, comp2Skill = None, comp2Disp = None, comp3Skill = None, comp3Disp = None):
        
        colorChoiceList = ["green", "yellow", "blue", "red"]
        self.userPlayer = player.player(playerColorChoice)
        self.userPlayer.setUserPlayerFlag()
        colorChoiceList.remove(playerColorChoice)
        self.totalPlayerCount = enemyPlayerCount + 1

        # This hefty section sets the skill and disposition flags for individual
        # computer players based on the boolean input values in the constructor.
        
        if enemyPlayerCount == 3:
            self.compPlayer1 = player.player(colorChoiceList.pop())
            if comp1Skill == True and comp1Disp == True:
                self.compPlayer1.setSmartMeanCompFlag()
            elif comp1Skill == True and comp1Disp == False:
                self.compPlayer1.setSmartNiceCompFlag()
            elif comp1Skill == False and comp1Disp == True:
                self.compPlayer1.setDumbMeanCompFlag()
            else:
                self.compPlayer1.setDumbNiceCompFlag()
                
            self.compPlayer2 = player.player(colorChoiceList.pop())
            if comp2Skill == True and comp2Disp == True:
                self.compPlayer2.setSmartMeanCompFlag()
            elif comp2Skill == True and comp2Disp == False:
                self.compPlayer2.setSmartNiceCompFlag()
            elif comp2Skill == False and comp2Disp == True:
                self.compPlayer2.setDumbMeanCompFlag()
            else:
                self.compPlayer2.setDumbNiceCompFlag()
            
            self.compPlayer3 = player.player(colorChoiceList.pop())
            if comp3Skill == True and comp3Disp == True:
                self.compPlayer3.setSmartMeanCompFlag()
            elif comp3Skill == True and comp3Disp == False:
                self.compPlayer3.setSmartNiceCompFlag()
            elif comp3Skill == False and comp3Disp == True:
                self.compPlayer3.setDumbMeanCompFlag()
            else:
                self.compPlayer3.setDumbNiceCompFlag()

        elif enemyPlayerCount == 2:
            self.compPlayer1 = player.player(colorChoiceList.pop())
            if comp1Skill == True and comp1Disp == True:
                self.compPlayer1.setSmartMeanCompFlag()
            elif comp1Skill == True and comp1Disp == False:
                self.compPlayer1.setSmartNiceCompFlag()
            elif comp1Skill == False and comp1Disp == True:
                self.compPlayer1.setDumbMeanCompFlag()
            else:
                self.compPlayer1.setDumbNiceCompFlag()
                
            self.compPlayer2 = player.player(colorChoiceList.pop())
            if comp2Skill == True and comp2Disp == True:
                self.compPlayer2.setSmartMeanCompFlag()
            elif comp2Skill == True and comp2Disp == False:
                self.compPlayer2.setSmartNiceCompFlag()
            elif comp2Skill == False and comp2Disp == True:
                self.compPlayer2.setDumbMeanCompFlag()
            else:
                self.compPlayer2.setDumbNiceCompFlag()

        elif enemyPlayerCount == 1:
            self.compPlayer1 = player.player(colorChoiceList.pop())
            if comp1Skill == True and comp1Disp == True:
                self.compPlayer1.setSmartMeanCompFlag()
            elif comp1Skill == True and comp1Disp == False:
                self.compPlayer1.setSmartNiceCompFlag()
            elif comp1Skill == False and comp1Disp == True:
                self.compPlayer1.setDumbMeanCompFlag()
            else:
                self.compPlayer1.setDumbNiceCompFlag()
            
        # The common square list represents all 60 of the common white squares
        # of the board all of the individual pawns may occupy. There are also
        # individual red, blue, yellow, and green square lists which represent
        # the 5 squares of the safety ramp for their particular color. Each
        # color also has a start and end position from which pawns of their
        # respective color may be popped and pushed.
        
        self.commonSquareList = []
        self.redSquareList = []
        self.blueSquareList = []
        self.yellowSquareList = []
        self.greenSquareList = []
        
        for i in range(60):
            self.commonSquareList.append(self.square())

        for i in range(5):
            self.redSquareList.append(self.square())
            self.blueSquareList.append(self.square())
            self.yellowSquareList.append(self.square())
            self.greenSquareList.append(self.square())

        # Note: these start zone fields may be deprecated. I intend to simply
        # use the pawns' flags to determine whether they are in the start zone
        # or not, as such although these start zone fields may exist in the code,
        # they may not be used. They would be a great thing to refactor out.
        
        self.redStartZone = []
        self.blueStartZone = []
        self.yellowStartZone = []
        self.greenStartZone = []

        self.redEndZone = []
        self.blueEndZone = []
        self.yellowEndZone = []
        self.greenEndZone = []

        # The board class also has a deck which may be drawn from.

        self.cardDeck = deck.deck()

    # This is a lengthy movement algorithm for moving pawns across the board.
    def movePawn(self, chosenPawn, moveDistance):

        # Case 1: chosen pawn starts in the start zone.
        if chosenPawn.inStartZone:
            targetIndex = chosenPawn.colorCommonOffset + moveDistance - 1
            if targetIndex > 59:
                targetIndex -= 60
            if self.commonSquareList[targetIndex].occupBool:
                if self.commonSquareList[targetIndex].occupyingPawn.color != chosenPawn.color:
                    self.removePawn(targetIndex)
                    self.insertPawn(targetIndex, chosenPawn, moveDistance)
            elif not self.commonSquareList[targetIndex].occupBool:
                self.insertPawn(targetIndex, chosenPawn, moveDistance)

        # Case 2: chosen pawn starts on the common board or safety ramp.
        elif chosenPawn.onCommonBoard or chosenPawn.onSafetyRamp:
            if chosenPawn.score in range(1,60):
                previousPawnIndex = chosenPawn.score - 1
            elif chosenPawn.score in range(60,64):
                previousPawnIndex = chosenPawn.score - 60
            if chosenPawn.score + moveDistance > 59 and chosenPawn.score + moveDistance <= 65:
                if chosenPawn.score + moveDistance < 65:
                    self.placePawnOnRamp(chosenPawn, moveDistance)##
                elif chosenPawn.score + moveDistance == 65:
                    self.placePawnInEndZone(chosenPawn, moveDistance)
            elif chosenPawn.score + moveDistance <= 59:                
                targetIndex = chosenPawn.commonBoardPosition + moveDistance - 1
                if targetIndex > 59:
                    targetIndex -= 60
                if self.commonSquareList[targetIndex].occupBool:
                    if self.commonSquareList[targetIndex].occupyingPawn.color != chosenPawn.color:
                        self.removePawn(targetIndex)
                        self.insertPawn(targetIndex, chosenPawn, moveDistance)
                        self.removePawnGentle(previousPawnIndex)
                elif not self.commonSquareList[targetIndex].occupBool:
                    self.insertPawn(targetIndex, chosenPawn, moveDistance)
                    self.removePawnGentle(previousPawnIndex)

        # This section of the move method will cause a pawn to "slide" if it
        # lands on a valid sliding square. This is essentially a one-time
        # recursive call of the movePawn function.

        # 3 square slide:
        if chosenPawn.score == 13 or chosenPawn.score == 28 or chosenPawn.score == 43:
            self.movePawn(chosenPawn, 3)

        # 4 square slide:
        elif chosenPawn.score == 21 or chosenPawn.score == 36 or chosenPawn.score == 51:
            self.movePawn(chosenPawn, 4)

        # This part of the move method ensures the player scores are kept up
        # to date at the end of every move.
        self.updatePlayerScores()

    # This method will remove a pawn from a given square and append it to its
    # respective end area.
    def placePawnInEndZone(self, chosenPawn, moveDistance):
        if chosenPawn.color == "red":
            self.redEndZone.append(chosenPawn)
        elif chosenPawn.color == "blue":
            self.blueEndZone.append(chosenPawn)
        elif chosenPawn.color == "yellow":
            self.yellowEndZone.append(chosenPawn)
        elif chosenPawn.color == "green":
            self.greenEndZone.append(chosenPawn)
        chosenPawn.scorePosUpdate(moveDistance)
                
    # This method will remove a pawn from a given square and insert it into a
    # square in its respective safety ramp.
    def placePawnOnRamp(self, chosenPawn, moveValue):
        indexTarget = chosenPawn.score + moveValue - 60
        if chosenPawn.color == "red":
            if not self.redSquareList[indexTarget].occupBool:
                self.redSquareList[indexTarget].insertPawn(chosenPawn)
        elif chosenPawn.color == "blue":
            if not self.blueSquareList[indexTarget].occupBool:
                self.blueSquareList[indexTarget].insertPawn(chosenPawn)
        elif chosenPawn.color == "yellow":
            if not self.yellowSquareList[indexTarget].occupBool:
                self.yellowSquareList[indexTarget].insertPawn(chosenPawn)
        elif chosenPawn.color == "green":
            if not self.greenSquareList[indexTarget].occupBool:
                self.greenSquareList[indexTarget].insertPawn(chosenPawn)
        chosenPawn.scorePosUpdate(moveValue)

    # This method will reset a pawn's score, append it to its respective
    # start area, and remove it from a given square.
    def removePawn(self, indexParam):
        self.resetPawn(self.commonSquareList[indexParam].occupyingPawn)
        self.commonSquareList[indexParam].removePawn()

    # This method will insert a pawn into a square and update its score
    # and position.
    def insertPawn(self, indexParam, insertedPawn, moveValue):
        self.commonSquareList[indexParam].insertPawn(insertedPawn)
        insertedPawn.scorePosUpdate(moveValue)

    # This method will simply remove a pawn from its previously occupied
    # square. It is to be used when advancing a pawn across the board.
    def removePawnGentle(self, indexVal):
        self.commonSquareList[indexVal].removePawn()
    
    # This method will kick a pawn out of its square and place it back
    # in its respective start zone.
    def resetPawn(self, unluckyPawn):
        unluckyPawn.scorePosReset()
        if unluckyPawn.color == "red":
            self.redStartZone.append(unluckyPawn)
        elif unluckyPawn.color == "blue":
            self.blueStartZone.append(unluckyPawn)
        elif unluckyPawn.color == "yellow":
            self.yellowStartZone.append(unluckyPawn)
        elif unluckyPawn.color == "green":
            self.greenStartZone.append(unluckyPawn)

    # This method will update the scores of all players' pawns. It should
    # be called at the end of every move.
    def updatePlayerScores(self):
        self.userPlayer.updatePawnScores()
        self.compPlayer1.updatePawnScores()
        if self.totalPlayerCount == 3:
            self.compPlayer2.updatePawnScores()
        elif self.totalPlayerCount == 4:
            self.compPlayer2.updatePawnScores()
            self.compPlayer3.updatePawnScores()

    # This is an inner class which represents an individual square.
    class square:

        def __init__(self):
            self.occupBool = False
            self.occupyingPawn = None

        def insertPawn(self, insPawn):
            self.occupBool = True
            self.occupyingPawn = insPawn

        def removePawn(self):
            self.occupBool = False
            self.occupyingPawn = None

    # This section will deal with moves based on whether the player in question
    # is a user player or a computer player. The computer player's moves will
    # be determined based on whether they are smart, mean, or otherwise.
    def chooseMove(self):
        option1bool = False
        option2bool = False

def testBooleans():
    testBoard = board("red", 3, True, False, True, True, False, False)
    print(testBoard.compPlayer1.smartBool)
    print(testBoard.compPlayer1.meanBool)
    print(testBoard.compPlayer2.smartBool)
    print(testBoard.compPlayer2.meanBool)
    print(testBoard.compPlayer3.smartBool)
    print(testBoard.compPlayer3.meanBool)

#testBooleans()
        
def chooseMoveTest():
    testBoard = board("red", 3)
    print("success")

#chooseMoveTest()
            
def slideTest():
    testBoard = board("red", 3)
    print("Red and Green initial pawnList[0] values:")
    print("Red: ", end = '')
    print(testBoard.userPlayer.pawnList[0].score)
    print("Green: ", end = '')
    print(testBoard.compPlayer3.pawnList[0].score)
    print("Red and Green values after green moves 28:")
    testBoard.movePawn(testBoard.compPlayer3.pawnList[0], 28)
    print("Red: ", end = '')
    print(testBoard.userPlayer.pawnList[0].score)
    print("Green: ", end = '')
    print(testBoard.compPlayer3.pawnList[0].score)
    print("Red and Green values after red moves 13:")
    testBoard.movePawn(testBoard.userPlayer.pawnList[0], 13)
    print("Red: ", end = '')
    print(testBoard.userPlayer.pawnList[0].score)
    print("Green: ", end = '')
    print(testBoard.compPlayer3.pawnList[0].score)
    print("Ending Red and Green total pawn scores:")
    print("Red: ", end = '')
    print(testBoard.userPlayer.pawnScores)
    print("Green: ", end = '')
    print(testBoard.compPlayer3.pawnScores)

#slideTest()

def drawTest():
    testBoard = board("red", 3)
    print(testBoard.cardDeck.draw(testBoard.cardDeck.cardStack).cardMessage)

#drawTest()
