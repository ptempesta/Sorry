import board

# This class is meant to test the board class, and to simulate several of the
# methods and their functionalities within the board class.

# Peter Tempesta, 4/26/2018

class test:

    def __init__(self):

        # Test board, user is red, 3 enemy opponents.
        self.testBoard = board.board("red", 3)

testInstance = test()

# This method will demonstrate the sliding effect of the board. First, a blue
# pawn of the first computer player will move 10 out of its starting zone. Next,
# a red pawn of the user will move 21 out of its starting zone, slide 4 spaces
# according to a sliding square on the board, and eventually land up on the same
# position as the previous blue pawn, knocking it back to its start area.

def testSliding():
    
    print("Red pawn at position: ", end='')
    print(testInstance.testBoard.userPlayer.pawnList[0].commonBoardPosition)
    print("Blue pawn at position: ", end='')
    print(testInstance.testBoard.compPlayer1.pawnList[0].commonBoardPosition)

    print("\nMoving blue pawn a distance of 15 out of its starting area:")
    testInstance.testBoard.movePawn(testInstance.testBoard.compPlayer1.pawnList[0], 10)
    
    print("Red pawn at position: ", end='')
    print(testInstance.testBoard.userPlayer.pawnList[0].commonBoardPosition)
    print("Blue pawn at position: ", end='')
    print(testInstance.testBoard.compPlayer1.pawnList[0].commonBoardPosition)

    print("\nMoving red pawn a distance of 21 out of its starting area:")
    testInstance.testBoard.movePawn(testInstance.testBoard.userPlayer.pawnList[0], 21)

    print("Red pawn at position: ", end='')
    print(testInstance.testBoard.userPlayer.pawnList[0].commonBoardPosition)
    print("Blue pawn at position: ", end='')
    print(testInstance.testBoard.compPlayer1.pawnList[0].commonBoardPosition)

    print("\nFinal red and blue pawn scores:")
    print("Red pawn score: ", end='')
    print(testInstance.testBoard.userPlayer.pawnList[0].score)
    print("Blue pawn score: ", end='')
    print(testInstance.testBoard.compPlayer1.pawnList[0].score)

#testSliding()
    
# This method will demonstrate the drawing of a card from the deck, and the user pawn
# will move accordingly.

def testDraw():

    print("Red pawn at position: ", end='')
    print(testInstance.testBoard.userPlayer.pawnList[0].commonBoardPosition)

    for i in range(3):

        print("\nDrawing a card for the player and moving one of the player's red pawns:")
        testInstance.testBoard.drawAndMovePlayer(testInstance.testBoard.userPlayer.pawnList[0], testInstance.testBoard.compPlayer1.pawnList[0])
        print("Red pawn at position: ", end='')
        print(testInstance.testBoard.userPlayer.pawnList[0].commonBoardPosition)
        print("Red pawn with score: ", end='')
        print(testInstance.testBoard.userPlayer.pawnList[0].score)

testDraw()

    
