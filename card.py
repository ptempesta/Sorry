# The following set of classes simulate the individual card types for the Sorry!
# board game. Each of the cards has a field titled cardMessage which is a string
# denoting the effect of the card. The actual card effects are coded into the
# board class.

# Peter Tempesta, 4/4/2018

class sorryCard:
    cardMessage = "Move a pawn from\nyour start area\nto take the place\nof \
another\nplayer's pawn\nwhich must return\nto its own start\narea OR move\nforward \
4."

class twelveCard:
    cardMessage = "Move forward 12."

class elevenCard:
    cardMessage = "Move a pawn from\nyour start area\nto take the place\nof \
another\nplayer's pawn\nwhich must return\nto its own start\narea OR move\nforward \
11."

class tenCard:
    cardMessage = "Move forward 10\nOR move backward 1."

class eightCard:
    cardMessage = "Move forward 8."

class sevenCard:
    cardMessage = "Move forward 7."

class fiveCard:
    cardMessage = "Move forward 5."

class fourCard:
    cardMessage = "Move backward 4."

class threeCard:
    cardMessage = "Move forward 3."

class twoCard:
    cardMessage = "Move forward 2."

class oneCard:
    cardMessage = "Move forward 1."

# A simple test method.
def testCardMethod():
    testCard = sorryCard()
    print(testCard.cardMessage)
#testCardMethod()
