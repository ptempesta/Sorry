# This class will simulate an eleven card for the Sorry! board game. Four
# instances of this class will populate a deck of Sorry! cards. This card has
# two move options to choose from, one is to move a pawn forward 11. The other
# option is to change one of your pawns' place with an opponent's pawn.

# Peter Tempesta, 4/4/2018

class elevenCard:
    def printText():
        message = "Move forward 11 OR change places with an opponent."
        print(message)
    def option1():
        # Option 1: Move forward 11.
        print("Move forward 11.")   # Testing text.
    def option2():
        # Option 2: Change places with an opponent.
        print("Change places with an opponent.")    # Testing text.

# The following code is meant to test the elevenCard class.
#testCard = elevenCard
#testCard.printText()
#testCard.option1()
#testCard.option2()
