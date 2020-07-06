# Scaffold for solution to DIT 852, Programming task 4
#
import random

def createDeck():
    # Return a deck of 52 cards, so that you can sample for it.
    # Either enumerate it or create it in a way requiring less typing
    # Your code below
    
    return result
    
def randomHand(deck, k):
    # Randomly select a hand of k cards from a deck, where deck is the
    # result from running createDeck
    # Your code below
    
    return hand
    
def averageAces(k, n):
    # Estimate the average number of aces in a randonly drawn hand of
    # k cards by sampling hands n times and counting aces
    deck = createDeck()
    # Your code below

    
    return average


def averageSuits(k, n):
    # Estimate the average number of distinct suits in a randonly drawn hand of 
    # k cards by sampling hands n times and counting suits
    deck = createDeck()
    # Your code below

    
    return average
    

def run(k, n):
    # Do not change this function
    print(f"Average number of aces in hands of size {k} in {n} trials is {averageAces(k, n)}") 
    print(f"Average number of distinct suits in hands of size {k} in {n} trials is {averageSuits(k, n)}")


# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    run(5,100)
    assert 0.2 < averageAces(5,100) < 0.6
    


    
