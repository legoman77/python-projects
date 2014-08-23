import time


def badgers():
    badgers = 1
    while badgers <= 12:
        print(badgers,'badgers')
        badgers += 1
        time.sleep(0.3)

def mushrooms():
    for mushroom in range (2):
        print(mushroom+1,'mushrooms')
        time.sleep(0.7)
        
        



badgers()
mushrooms()
