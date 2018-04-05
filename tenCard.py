# This class will simulate a ten card for the Sorry! board game. Four instances
# of this class will populate a deck of Sorry! cards. This card has two move
# options to choose from, one is to move a pawn forward 10. The other option is
# to move a pawn backward 1.

# Peter Tempesta, 4/4/2018

class tenCard:
    def printText():
        message = "Move forward 10 OR move backward 1."
        print(message)
    def option1():
        # Option 1: Move forward 10.
        print("Move forward 10.")   # Testing text.
    def option2():
        # Option 2: Move backward 1.
        print("Move backward 1.")   # Testing text.

# The following code is meant to test the tenCard class.
#testCard = tenCard
#testCard.printText()
#testCard.option1()
#testCard.option2()
