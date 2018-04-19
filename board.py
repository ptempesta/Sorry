import deck
import player

# This class is meant to simulate the board for the Sorry! board game. The board
# as designed in this class contains a list of squares, which will be defined
# within the board class. Each board can potentially have an occupying pawn.

# Peter Tempesta, 4/11/2018

class board:

    def __init__(self, playerColorChoice, adversaryCount):

        # For organizational purposes, the board class has players. As such, the
        # board class has four separate players. The User Player has the color
        # of the user's choice. As of April 19th, an additional parameter has
        # been added to account for how many players the user would like to play
        # against. The user can now play against 3, 2, or just 1 computer
        # opponent.

        # Three computer opponents:
        if adversaryCount == 3:
            if playerColorChoice == "red":
                self.userPlayer = player.player("red")
                self.compPlayer1 = player.player("blue")
                self.compPlayer2 = player.player("yellow")
                self.compPlayer3 = player.player("green")
            elif playerColorChoice == "blue":
                self.userPlayer = player.player("blue")
                self.compPlayer1 = player.player("red")
                self.compPlayer2 = player.player("yellow")
                self.compPlayer3 = player.player("green")
            elif playerColorChoice == "yellow":
                self.userPlayer = player.player("yellow")
                self.compPlayer1 = player.player("red")
                self.compPlayer2 = player.player("blue")
                self.compPlayer3 = player.player("green")
            elif playerColorChoice == "green":
                self.userPlayer = player.player("green")
                self.compPlayer1 = player.player("red")
                self.compPlayer2 = player.player("blue")
                self.compPlayer3 = player.player("yellow")

        #Two computer opponents:
        elif adversaryCount == 2:
            if playerColorChoice == "red":
                self.userPlayer = player.player("red")
                self.compPlayer1 = player.player("blue")
                self.compPlayer2 = player.player("yellow")
            elif playerColorChoice == "blue":
                self.userPlayer = player.player("blue")
                self.compPlayer1 = player.player("red")
                self.compPlayer2 = player.player("yellow")
            elif playerColorChoice == "yellow":
                self.userPlayer = player.player("yellow")
                self.compPlayer1 = player.player("red")
                self.compPlayer2 = player.player("blue")
            elif playerColorChoice == "green":
                self.userPlayer = player.player("green")
                self.compPlayer1 = player.player("red")
                self.compPlayer2 = player.player("blue")

        #One computer opponent:
        elif adversaryCount == 1:
            if playerColorChoice == "red":
                self.userPlayer = player.player("red")
                self.compPlayer1 = player.player("blue")
            elif playerColorChoice == "blue":
                self.userPlayer = player.player("blue")
                self.compPlayer1 = player.player("red")
            elif playerColorChoice == "yellow":
                self.userPlayer = player.player("yellow")
                self.compPlayer1 = player.player("red")
            elif playerColorChoice == "green":
                self.userPlayer = player.player("green")
                self.compPlayer1 = player.player("red")

        # The Square List represents all of the 60 individual squares which
        # pawns of all colors may occupy.
        self.squareList = []

        for i in range(60):
            self.squareList.append(self.square())

    # The move method will move a pawn from one square to another.
    def movePawn(self, movingPlayer, selectedPawn, moveValue, otherPlayer1, otherPlayer2 = None, otherPlayer3 = None):
        # Moving a pawn out of the start position:
        if selectedPawn.inStartPos:
            targetCommonIndex = moveValue - 1 + selectedPawn.pawnPosOffset
            if targetCommonIndex > 59:
                targetCommonIndex -= 60
            # The target square is empty:
            if self.squareList[targetCommonIndex].occupBool == False:
                self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
            # The target square is occupied by another player's pawn:
            elif (self.squareList[targetCommonIndex].occupBool == True and
                  self.squareList[targetCommonIndex].occupyingPawn.pawnColor != selectedPawn.pawnColor):
                # The target square is occupied by one of otherPlayer1's pawns:
                if otherPlayer1.playerColor == self.squareList[targetCommonIndex].occupyingPawn.pawnColor:
                    # Case of pawn1:
                    if self.squareList[targetCommonIndex].occupyingPawn == otherPlayer1.pawn1:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer1.startZone.append(otherPlayer1.pawn1)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                    # Case of pawn2:
                    elif self.squareList[targetCommonIndex].occupyingPawn == otherPlayer1.pawn2:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer1.startZone.append(otherPlayer1.pawn2)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                    # Case of pawn3:
                    elif self.squareList[targetCommonIndex].occupyingPawn == otherPlayer1.pawn3:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer1.startZone.append(otherPlayer1.pawn3)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                # The target square is occupied by one of otherPlayer2's pawns:
                elif otherPlayer2.playerColor == self.squareList[targetCommonIndex].occupyingPawn.pawnColor:
                    # Case of pawn1:
                    if self.squareList[targetCommonIndex].occupyingPawn == otherPlayer2.pawn1:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer2.startZone.append(otherPlayer2.pawn1)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                    # Case of pawn2:
                    elif self.squareList[targetCommonIndex].occupyingPawn == otherPlayer2.pawn2:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer2.startZone.append(otherPlayer2.pawn2)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                    # Case of pawn3:
                    elif self.squareList[targetCommonIndex].occupyingPawn == otherPlayer2.pawn3:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer2.startZone.append(otherPlayer2.pawn3)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                # The target square is occupied by one of otherPlayer3's pawns:
                elif otherPlayer3.playerColor == self.squareList[targetCommonIndex].occupyingPawn.pawnColor:
                    # Case of pawn1:
                    if self.squareList[targetCommonIndex].occupyingPawn == otherPlayer3.pawn1:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer3.startZone.append(otherPlayer3.pawn1)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                    # Case of pawn2:
                    elif self.squareList[targetCommonIndex].occupyingPawn == otherPlayer3.pawn2:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer3.startZone.append(otherPlayer3.pawn2)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
                    # Case of pawn3:
                    elif self.squareList[targetCommonIndex].occupyingPawn == otherPlayer3.pawn3:
                        self.squareList[targetCommonIndex].removePawn()
                        otherPlayer3.startZone.append(otherPlayer3.pawn3)
                        self.squareList[targetCommonIndex].insertPawn(movingPlayer.startZone.pop())
        # Moving a pawn which starts on the common board:
                            
                        
                
            

    # This is an inner class which represents an individual square for the
    # common board shared among all players.
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

testBoard = board("red",1)
testBoard.movePawn(testBoard.userPlayer, testBoard.userPlayer.pawn1, 5, testBoard.compPlayer1)
print("Red start zone after first move:")
print(testBoard.userPlayer.startZone)
print("Blue start zone after first move:")
print(testBoard.compPlayer1.startZone)
print("Color of pawn at [4]:")
print(testBoard.squareList[4].occupyingPawn.pawnColor)
testBoard.movePawn(testBoard.compPlayer1, testBoard.compPlayer1.pawn1, 50, testBoard.userPlayer)
print("Red start zone after second move:")
print(testBoard.userPlayer.startZone)
print("Blue start zone after second move:")
print(testBoard.compPlayer1.startZone)
print("Color of pawn at [4] and the pawn itself:")
print(testBoard.squareList[4].occupyingPawn.pawnColor)
print(testBoard.squareList[4].occupyingPawn)
