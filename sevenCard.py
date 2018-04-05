# This class will simulate a seven card for the Sorry! board game. Four
# instances of this class will populate a deck of Sorry! cards. This card has
# two move options to choose from, one is to move a pawn forward 7. The other
# option is to split the move between two of your pawns.

# Peter Tempesta, 4/4/2018

class sevenCard:
    def printText():
        message = "Move forward 7 OR split the move between two of your pawns."
        print(message)
    def option1():
        # Option 1: Move forward 7.
        print("Move forward 7.")    # Testing text.
    def option2():
        # Option 2: Split the move between two of your pawns.
        print("Split the move between two of your pawns.")  # Testing text.

# The following code is meant to test the sevenCard class.
#testCard = sevenCard
#testCard.printText()
#testCard.option1()
#testCard.option2()
