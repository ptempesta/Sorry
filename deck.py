import random
import card

# This class will simulate a deck of cards for the Sorry! board game. This class
# will be composed of a list of Sorry! board game cards. The list will consist
# of 45 cards, 4 of each card excepting the oneCard, of which there will be 5.

# Peter Tempesta, 4/4/2018

class deck:
    cardStack = []
    # The draw method will pop one card off from the end of the list, as if a
    # card was drawn from the deck and discarded. However, if there are no cards
    # left in the list, the list will be repopulated with cards and shuffled.
    def draw(cardStack):
        if len(cardStack) == 0:
            for i in range(0,4):
                cardStack.append(card.sorryCard)
                cardStack.append(card.twelveCard)
                cardStack.append(card.elevenCard)
                cardStack.append(card.tenCard)
                cardStack.append(card.eightCard)
                cardStack.append(card.sevenCard)
                cardStack.append(card.fiveCard)
                cardStack.append(card.fourCard)
                cardStack.append(card.threeCard)
                cardStack.append(card.twoCard)
            for i in range(0,5):
                cardStack.append(card.oneCard)
            random.shuffle(cardStack)
            return cardStack.pop()
        else:
            return cardStack.pop()
    
            
# The following code is meant to test this class.    
#testCard = card.sorryCard
#testCard.printText()

#testDeck = deck
#testDeck.cardStack[0].printText()
#print(len(testDeck.cardStack))
#testDeck.cardStack.pop().printText()
#print(len(testDeck.cardStack))

#testDeck = deck
#print(len(testDeck.cardStack))
#testDeck.draw(testDeck.cardStack).printText()
#print(len(testDeck.cardStack))
