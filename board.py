import deck
import player

# This class is meant to simulate the board for the Sorry! board game. The board
# as designed in this class contains a list of squares, which will be defined
# within the board class. Each board can potentially have an occupying pawn.

# Peter Tempesta, 4/11/2018

class board:

    def __init__(self, playerColorChoice):

        # For organizational purposes, the board class has players. As such, the
        # board class has four separate players. The User Player has the color
        # of the user's choice.
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

        # The Square List represents all of the 60 individual squares which
        # pawns may occupy.
        self.squareList = []

        for i in range(60):
            self.squareList.append(self.square())

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
