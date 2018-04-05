# This class will simulate a Sorry! card for the Sorry! board game. Four
# instances of this class will populate a deck of Sorry! cards. This card has
# two move options to choose from, one is to move a pawn from your start area to
# take the place of another player's pawn and have that player's pawn return to
# its own start area. The other option is to simply move a pawn forward 4.

# Peter Tempesta, 4/4/2018

class sorryCard:
    def printText():
        message = "Move a pawn from your start area to take the place of " \
        "another player's pawn, which must return to its own start area. " \
        "OR move forward 4."
        print(message)
    def option1():
        # Option 1: Move a pawn from your start area to take the place of
        # another player's pawn which must return to its own start area.
        print("Sorry!")   # Testing text.
    def option2():
        # Option 2: Move forward 4.
        print("Move forward 4.")   # Testing text.

# The following code is meant to test the sorryCard class.
#testCard = sorryCard
#testCard.printText()
#testCard.option1()
#testCard.option2()
