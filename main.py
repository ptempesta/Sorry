import board

# This is the main class for the Sorry! board game.

# Peter Tempesta, 4/21/2018

class main:

    def __init__(self, playerColorChoice, enemyPlayerCount):

        self.boardInstance = board.board(playerColorChoice, enemyPlayerCount)

testUserColor = "red"
testEnemyCount = 3

programInstance = main(testUserColor, testEnemyCount)
