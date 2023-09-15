import board
from random import randint

gameDict = {}

class game:
    def __init__(self):
        gameID = randint(1000, 9999)
        gameBoard = board()
        playerState = "x"
        gameDict.update(gameID, self)