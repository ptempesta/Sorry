import pawn

# This class is meant to simulate a player for the Sorry! board game. A player
# has three pawns, a starting zone for his or her pawns, an ending zone for his
# or her pawns, and a "safety ramp" for these pawns as well.

# Peter Tempesta, 4/10/2018

class player:
    pawn1 = pawn.pawn()
    pawn2 = pawn.pawn()
    pawn3 = pawn.pawn()

    # The Starting Zone is a list from which pawns may be pushed or popped. By
    # default (at the beginning of the game, when a player is initialized), the
    # Starting Zone is populated with all three of the player's pawns.
    startZone = []
    startZone.append(pawn1)
    startZone.append(pawn2)
    startZone.append(pawn3)

    # The Ending Zone is a list to which pawns may be pushed. If all of the
    # player's pawns end up in the Ending Zone, then that player wins.
    endZone = []

# The following code is for testing purposes.
testPlayer = player
testPlayer.pawn1.setColorRed()
testPlayer.pawn2.setColorRed()
testPlayer.pawn3.setColorRed()
print(testPlayer.pawn1.pawnColor)
print(testPlayer.pawn2.pawnColor)
print(testPlayer.pawn3.pawnColor)

print(testPlayer.startZone)
print(testPlayer.endZone)
print("Pushing one pawn from startZone to endZone:")
testPlayer.endZone.append(testPlayer.startZone.pop())
print(testPlayer.startZone)
print(testPlayer.endZone)

