import deck
import player

# This class is meant to simulate the board for the Sorry! board game. The board
# class contains between two to four total players upon initialization.

# Peter Tempesta, 4/11/2018

class board:

    def __init__(self, playerColorChoice, enemyPlayerCount):
        
        colorChoiceList = ["green", "yellow", "blue", "red"]
        self.userPlayer = player.player(playerColorChoice)
        colorChoiceList.remove(playerColorChoice)
        self.totalPlayerCount = enemyPlayerCount + 1
            
        if enemyPlayerCount == 3:
            self.compPlayer1 = player.player(colorChoiceList.pop())
            self.compPlayer2 = player.player(colorChoiceList.pop())
            self.compPlayer3 = player.player(colorChoiceList.pop())

        elif enemyPlayerCount == 2:
            self.compPlayer1 = player.player(colorChoiceList.pop())
            self.compPlayer2 = player.player(colorChoiceList.pop())

        elif enemyPlayerCount == 1:
            self.compPlayer1 = player.player(colorChoiceList.pop())
            
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
