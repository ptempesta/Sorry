import sorryCard
import twelveCard
import elevenCard
import tenCard
import eightCard
import sevenCard
import fiveCard
import fourCard
import threeCard
import twoCard
import oneCard

import random

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
                cardStack.append(sorryCard.sorryCard)
                cardStack.append(twelveCard.twelveCard)
                cardStack.append(elevenCard.elevenCard)
                cardStack.append(tenCard.tenCard)
                cardStack.append(eightCard.eightCard)
                cardStack.append(sevenCard.sevenCard)
                cardStack.append(fiveCard.fiveCard)
                cardStack.append(fourCard.fourCard)
                cardStack.append(threeCard.threeCard)
                cardStack.append(twoCard.twoCard)
            for i in range(0,5):
                cardStack.append(oneCard.oneCard)
            random.shuffle(cardStack)
            return cardStack.pop()
        else:
            return cardStack.pop()
    
            
# The following code is meant to test this class.    
#testCard = sorryCard.sorryCard
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
