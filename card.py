# The following set of classes simulate the individual card types for the Sorry!
# board game. Several of the card types have multiple movement options to choose
# from, and all card types follow the same general method option format.

# Peter Tempesta, 4/4/2018

class sorryCard:
    cardMessage = "Move a pawn from your start area to take the place of \
another player's pawn which must return to its own start area OR move forward \
4."

class twelveCard:
    cardMessage = "Move forward 12."

class elevenCard:
    cardMessage = "Move forward 11 OR change places with an opponent."

class tenCard:
    cardMessage = "Move forward 10 OR move backward 1."

class eightCard:
    cardMessage = "Move forward 8."

class sevenCard:
    cardMessage = "Move forward 7 OR split the move between two of \
your pawns."

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


def testCardMethod():
    testCard = sorryCard()
    print(testCard.cardMessage)

#testCardMethod()
